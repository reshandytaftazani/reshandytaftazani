import os
import sys
import json
import urllib.request
import datetime

USERNAME = os.environ.get("GITHUB_USERNAME", "reshandytaftazani")
TOKEN = os.environ.get("GITHUB_TOKEN", None)
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "assets", "activity-compact.svg")

def fetch_contributions():
    # If GitHub token is provided, use GraphQL for 100% accurate calendar data
    if TOKEN:
        query = """
        query($login: String!) {
          user(login: $login) {
            contributionsCollection {
              contributionCalendar {
                totalContributions
                weeks {
                  contributionDays {
                    contributionCount
                    date
                  }
                }
              }
            }
          }
        }
        """
        req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=json.dumps({"query": query, "variables": {"login": USERNAME}}).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {TOKEN}",
                "User-Agent": "Antigravity-Velocity-Generator",
                "Content-Type": "application/json"
            }
        )
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
                all_days = []
                for w in weeks:
                    for d in w["contributionDays"]:
                        all_days.append((d["date"], d["contributionCount"]))
                # return last 30 days
                return all_days[-30:]
        except Exception as e:
            print(f"GraphQL request failed: {e}, falling back to REST events", file=sys.stderr)

    # Fallback: query public events
    req = urllib.request.Request(
        f"https://api.github.com/users/{USERNAME}/events?per_page=100",
        headers={"User-Agent": "Antigravity-Velocity-Generator"}
    )
    today = datetime.date.today()
    counts = { (today - datetime.timedelta(days=i)).isoformat(): 0 for i in range(30) }
    
    try:
        with urllib.request.urlopen(req) as resp:
            events = json.loads(resp.read().decode("utf-8"))
            for ev in events:
                if ev.get("type") in ("PushEvent", "PullRequestEvent", "PullRequestReviewEvent"):
                    created_at = ev.get("created_at", "")[:10]
                    if created_at in counts:
                        if ev.get("type") == "PushEvent":
                            counts[created_at] += len(ev.get("payload", {}).get("commits", [1]))
                        else:
                            counts[created_at] += 1
    except Exception as e:
        print(f"REST request failed: {e}", file=sys.stderr)

    # Sort ascending
    sorted_days = sorted(counts.items(), key=lambda x: x[0])
    return sorted_days

def generate_svg(days):
    if not days:
        return

    counts = [c for _, c in days]
    total_commits = sum(counts)
    avg_per_day = round(total_commits / len(counts), 1) if counts else 0
    peak_day = max(counts) if counts else 1
    max_scale = max(12, peak_day)

    # Generate bar elements
    # Chart area: width 440, 30 days -> slot ~14px, bar width 10px, gap 4px
    bars_svg = []
    baseline_y = 90
    max_bar_height = 90

    for i, (date_str, count) in enumerate(days):
        x = i * 14
        h = max(2, int((count / max_scale) * max_bar_height)) if count > 0 else 2
        y = baseline_y - h
        delay = round(0.04 + i * 0.02, 2)

        if count == 0:
            bars_svg.append(f'    <rect x="{x}" y="{baseline_y - 2}" width="10" height="2" rx="1" fill="#21262d" />')
        else:
            if count >= max_scale * 0.75:
                color = "#34D399"
                stroke = ' stroke="#10B981" stroke-width="1"'
            elif count >= max_scale * 0.5:
                color = "#10B981"
                stroke = ""
            elif count >= max_scale * 0.25:
                color = "#059669"
                stroke = ""
            else:
                color = "#047857"
                stroke = ""
            bars_svg.append(f'    <rect class="bar" style="animation-delay: {delay}s" x="{x}" y="{y}" width="10" height="{h}" rx="1.5" fill="{color}"{stroke} />')

    bars_content = "\n".join(bars_svg)

    # Average line Y coordinate
    avg_h = int((avg_per_day / max_scale) * max_bar_height) if max_scale > 0 else 0
    avg_y = baseline_y - avg_h

    # Date labels (5 evenly spaced)
    def fmt_date(d_str):
        try:
            dt = datetime.datetime.strptime(d_str, "%Y-%m-%d")
            return dt.strftime("%b %d")
        except:
            return d_str

    d0 = fmt_date(days[0][0])
    d7 = fmt_date(days[7][0])
    d15 = fmt_date(days[15][0])
    d22 = fmt_date(days[22][0])

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 495 195" width="100%" height="195" fill="none">
  <defs>
    <rect id="compact-card-bg" width="495" height="195" rx="8" fill="#0d1117" stroke="#30363d" stroke-width="1" />

    <style><![CDATA[
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap');

      text {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }}
      .mono {{
        font-family: 'Fira Code', monospace;
      }}

      .hdr-title {{
        font-size: 13px;
        font-weight: 600;
        fill: #10B981;
      }}
      .hdr-stat-lbl {{
        font-size: 9px;
        fill: #8b949e;
        text-transform: uppercase;
        letter-spacing: 0.04em;
      }}
      .hdr-stat-val {{
        font-size: 11px;
        font-weight: 600;
        fill: #f0f6fc;
      }}
      .axis-tick {{
        font-size: 9px;
        fill: #6e7681;
      }}
      .grid-line {{
        stroke: #21262d;
        stroke-width: 1px;
        stroke-dasharray: 2, 4;
      }}

      /* Bar Rise Animation */
      .bar {{
        transform-box: fill-box;
        transform-origin: bottom;
        animation: barGrow 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
      }}

      @keyframes barGrow {{
        from {{
          transform: scaleY(0);
          opacity: 0;
        }}
        to {{
          transform: scaleY(1);
          opacity: 1;
        }}
      }}
    ]]></style>
  </defs>

  <!-- Container -->
  <use href="#compact-card-bg" />

  <!-- Header -->
  <g transform="translate(20, 24)">
    <circle cx="4" cy="4" r="3.5" fill="#10B981" />
    <text x="14" y="8" class="hdr-title">Commit Velocity</text>
    <text x="125" y="8" class="mono" font-size="10" fill="#8b949e">// 30-Day Stream</text>

    <!-- Header Stats -->
    <g transform="translate(320, -5)">
      <text x="0" y="8" class="hdr-stat-lbl mono">Total</text>
      <text x="0" y="21" class="hdr-stat-val mono" fill="#10B981">{total_commits}</text>
      <text x="50" y="8" class="hdr-stat-lbl mono">Avg/D</text>
      <text x="50" y="21" class="hdr-stat-val mono">{avg_per_day}</text>
      <text x="100" y="8" class="hdr-stat-lbl mono">Peak</text>
      <text x="100" y="21" class="hdr-stat-val mono" fill="#38bdf8">{peak_day}</text>
    </g>
  </g>

  <!-- Hairline Divider -->
  <line x1="20" y1="42" x2="475" y2="42" stroke="#21262d" stroke-width="1" />

  <!-- Grid & Ticks (Chart Area: Y from 54 to 144) -->
  <g transform="translate(28, 54)">
    <text x="-6" y="4" class="axis-tick mono" text-anchor="end">{max_scale}</text>
    <line x1="0" y1="0" x2="440" y2="0" class="grid-line" />

    <text x="-6" y="34" class="axis-tick mono" text-anchor="end">{int(max_scale * 2 / 3)}</text>
    <line x1="0" y1="30" x2="440" y2="30" class="grid-line" />

    <text x="-6" y="64" class="axis-tick mono" text-anchor="end">{int(max_scale / 3)}</text>
    <line x1="0" y1="60" x2="440" y2="60" class="grid-line" />

    <text x="-6" y="94" class="axis-tick mono" text-anchor="end">0</text>
    <line x1="0" y1="90" x2="440" y2="90" stroke="#30363d" stroke-width="1" />
  </g>

  <!-- 30 Bars -->
  <g transform="translate(32, 54)">
{bars_content}

    <!-- Dashed Average Line -->
    <line x1="0" y1="{avg_y}" x2="420" y2="{avg_y}" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3, 3" opacity="0.8" />
  </g>

  <!-- X-Axis Labels -->
  <g transform="translate(32, 165)">
    <text x="0" y="0" class="axis-tick mono">{d0}</text>
    <text x="105" y="0" class="axis-tick mono">{d7}</text>
    <text x="210" y="0" class="axis-tick mono">{d15}</text>
    <text x="315" y="0" class="axis-tick mono">{d22}</text>
    <text x="405" y="0" class="axis-tick mono" fill="#10B981" font-weight="600">Today</text>
  </g>
</svg>"""

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {OUTPUT_FILE} successfully with {len(days)} days (Total: {total_commits}, Peak: {peak_day}, Avg: {avg_per_day})")

if __name__ == "__main__":
    days = fetch_contributions()
    generate_svg(days)

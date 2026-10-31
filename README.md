<div align="center">

# Reshandy Taftazani Aulya

<p align="center">
  <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=20&duration=3000&pause=1000&color=10B981&center=true&vCenter=true&width=650&height=45&lines=%3E+Machine+Learning+%26+Software+Engineer+%7C;%3E+Building+Reliable+%26+Reproducible+ML+Systems+%7C;%3E+Computer+Science+%40+Universitas+Indonesia+%7C" alt="Typing Indicator" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/reshandy-taftazani-aulya/"><img src="https://img.shields.io/badge/LinkedIn-reshandy--taftazani--aulya-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:reshandy.taftazani@ui.ac.id"><img src="https://img.shields.io/badge/Email-reshandy.taftazani%40ui.ac.id-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://cs.ui.ac.id/"><img src="https://img.shields.io/badge/Alma_Mater-Universitas_Indonesia-F7B500?style=flat-square&logo=academia&logoColor=black" alt="Universitas Indonesia" /></a>
  <img src="https://img.shields.io/badge/Focus-MLE_%26_Systems-10B981?style=flat-square" alt="Focus" />
</p>

*Machine Learning Engineering and Systems Programming &mdash; focused on leak-free pipelines, clean architecture, deterministic reproducibility, and local-first compute.*

---

</div>

## Overview

Computer Science student at **Universitas Indonesia** focusing on **Machine Learning Engineering (MLE)** and **Software Systems**.

My work focuses on production-grade machine learning systems developed with the discipline of systems software:
- **Clean Architecture and Explicit Contracts**: Enforcing strict boundaries between API specifications, supervisor routines, ML training engines, and persistent state.
- **Leak-Free Evaluation Protocols**: Ensuring all data transformations occur strictly within partition boundaries and that holdout sets remain isolated until final model evaluation.
- **Defensive Engineering and Verification**: Implementing comprehensive test suites that validate numerical accuracy, process lifecycles, cancellation handling, resource limits, and crash recovery.

---

## Engineering Principles

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Zero Data Leakage by Design</h3>
      <p>A benchmark metric is only meaningful when evaluation protocols are sound. Feature engineering, imputation, and categorical encodings are fitted exclusively inside training fold partitions. Holdout partitions are locked behind immutable tombstone guards and evaluated only once on the refitted, frozen candidate.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Rigorous Verification & TDD</h3>
      <p>Testing extends beyond standard happy paths. Systems are validated against unexpected child process termination, native interrupt signals, queue state contention, degenerate target distributions, and memory boundaries without mocking core operating system interfaces.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Clean Architecture & Contracts</h3>
      <p>Type safety and strict schema validation (Pydantic, TypeScript) protect internal domain logic from delivery mechanisms (FastAPI, Next.js) and persistence engines (SQLite, PostgreSQL). This separation guarantees maintainability and testability across independent components.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Local-First & Reproducible Compute</h3>
      <p>Maximizing utility from bounded local resources. Designing CPU-efficient workflows, deterministic seeding protocols, dataset SHA-256 fingerprinting, and local MLflow tracking so experiments can be verified independently without mandatory cloud dependencies.</p>
    </td>
  </tr>
</table>

---

## Technical Stack

<div align="center">

### Core Technologies

<p align="center">
  <img src="https://skillicons.dev/icons?i=cpp,py,java,js,ts,html,css,bash" alt="Languages" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=pytorch,sklearn,fastapi,nextjs,react,tailwind,docker,sqlite,postgres,git,linux,latex" alt="Frameworks and Tools" />
</p>

</div>

<br />

<div align="left">

#### Programming Languages
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white)](https://isocpp.org/)
[![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)](https://www.java.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white)](https://en.wikipedia.org/wiki/SQL)
[![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)

#### Machine Learning & Data
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/)
[![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)](https://mlflow.org/)
[![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white)](https://www.latex-project.org/)

#### Backend & Systems
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

#### Engineering Standards
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Test-Driven Development](https://img.shields.io/badge/Methodology-TDD%20%26%20Rigorous%20Testing-238636?style=flat-square&logo=checkmarx&logoColor=white)](https://en.wikipedia.org/wiki/Test-driven_development)
[![Clean Architecture](https://img.shields.io/badge/Architecture-Clean%20%26%20Hexagonal-6e40c9?style=flat-square)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
[![Reproducibility](https://img.shields.io/badge/ML%20Pipelines-Leakage--Free%20%26%20Deterministic-1f6feb?style=flat-square)](https://github.com/reshandytaftazani/modelarena)
[![uv](https://img.shields.io/badge/Package_Manager-uv-DE5FE9?style=flat-square)](https://github.com/astral-sh/uv)

</div>

---

## Featured Project

### [ModelArena](https://github.com/reshandytaftazani/modelarena) &mdash; *Fair Comparisons. Reproducible Experiments. Honest Evaluation.*

<p align="left">
  <img src="https://img.shields.io/badge/Verification-460%2B%20Tests%20Passing%20(0%20Skips)-16a34a?style=flat-square&logo=pytest&logoColor=white" alt="Test Status" />
  <img src="https://img.shields.io/badge/Design-Local--First%20CPU-2563eb?style=flat-square" alt="Design" />
  <img src="https://img.shields.io/badge/Backend-FastAPI%20%2B%20SQLite-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Frontend-Next.js%20%2B%20TypeScript-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/Engine-scikit--learn%20%2B%20PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="Engine" />
</p>

A local-first machine learning experimentation platform engineered for tabular datasets. It integrates classical estimators (`scikit-learn`) and neural network architectures (`PyTorch CPU MLP`) under a unified evaluation protocol, ensuring benchmark metrics reflect true generalizability rather than data leakage.

```
+---------------------------------------------------------------------------------------------------+
|                                      MODELARENA ARCHITECTURE                                      |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|   +-----------------------+                    HTTP / REST                    +---------------+   |
|   |  Next.js / TypeScript | <===============================================> |    FastAPI    |   |
|   |   (React, Tailwind,   |             JSON Schema Validation                |  API Gateway  |   |
|   |      shadcn/ui)       |             (Pydantic Type Guards)                +-------+-------+   |
|   +-----------------------+                                                           |           |
|                                                                                       | Enqueues  |
|                                                                                       v Jobs      |
|   +-------------------------------------------------------------------------------+   |           |
|   | WORKER SUPERVISOR                                                             |   |           |
|   | - Transactional Job Queue (SQLite)                                            | <-+           |
|   | - OS Process Lifecycle & Dead-Child Recovery                                  |               |
|   | - Native Cancellation & Orphan Process Mitigation                             |               |
|   +---------------------------------------+---------------------------------------+               |
|                                           | Spawns isolated execution                             |
|                                           v                                                       |
|   +-------------------------------------------------------------------------------+               |
|   | ISOLATED CPU EXECUTION WORKER (Subprocess)                                    |               |
|   |                                                                               |               |
|   |   +-------------------------+            +--------------------------------+   |               |
|   |   | Cross-Validation Engine |            | Fold-Local Preprocessing       |   |               |
|   |   | - Stratified Folds      | ---------> | - Scalers & Imputers fit ONLY  |   |               |
|   |   | - Dummy Baselines       |            |   on training fold             |   |               |
|   |   +-------------------------+            +--------------------------------+   |               |
|   |                                                                               |               |
|   |   +-----------------------------------------------------------------------+   |               |
|   |   | Model Candidates                                                      |   |               |
|   |   | - Classical: Logistic / Ridge, Random Forest, HistGradientBoosting    |   |               |
|   |   | - PyTorch CPU: Bounded MLP, Adam, Fold-Local Early Stopping           |   |               |
|   |   +-----------------------------------------------------------------------+   |               |
|   |                                       |                                       |               |
|   |                                       v Atomic publish                        |               |
|   |   +-----------------------------------------------------------------------+   |               |
|   |   | Auditable Artifacts & Experiment Records                              |   |               |
|   |   | - Local MLflow SQLite Tracking (Seeds, Fold Digests, Loss Curves)     |   |               |
|   |   | - Quarantined Holdout Evaluator (Evaluates frozen model exactly once) |   |               |
|   |   +-----------------------------------------------------------------------+   |               |
|   +-------------------------------------------------------------------------------+               |
+---------------------------------------------------------------------------------------------------+
```

#### Problem Statement
1. **Pervasive Data Leakage**: Standard experimental scripts frequently fit imputers or scalers across an entire dataset prior to splitting, or tune hyperparameters against holdout test data, yielding optimistic scores that fail in production.
2. **Process Instability**: Executing compute-heavy training runs inside web application threads leads to unhandled runtime crashes, resource exhaustion, and unkillable orphan threads.
3. **Optimistic Evaluation**: Evaluating candidate models without standardized dummy baselines conceals true performance gains over naive class distributions.

#### Engineering Highlights
- **Strict Leakage Isolation**: Data transformers are fitted exclusively inside each training fold partition. The 20% holdout split is locked behind immutable tombstone guards and can only be evaluated once after candidate selection is frozen.
- **Process Supervision & Fault Recovery**: Training executions run in isolated child processes. The supervisor handles Windows-compatible process spawning, cooperative cancellation (`SIGINT`/flags), orphan pruning, dead-child retries, and state reconciliation across server restarts.
- **Verification Without Mocking OS Boundaries**: Tested with `pytest` across >460 unit and integration tests. Worker lifecycles, memory guards, transactional SQLite locks, and PyTorch CPU convergence are validated through actual process execution rather than synthetic mocks.
- **Auditable & Local-First**: Experiment manifests capture dataset fingerprints (SHA-256), seeds, fold partitions, metrics, and training loss curves locally in MLflow SQLite. Zero external cloud dependencies or paid APIs.

**Repository:** [github.com/reshandytaftazani/modelarena](https://github.com/reshandytaftazani/modelarena)

---

## Contribution Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/pacman-contribution-graph-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/pacman-contribution-graph.svg">
  <img alt="pacman contribution graph" src="./assets/pacman-contribution-graph-dark.svg" width="100%">
</picture>

<br /><br />

<table>
  <tr>
    <td align="center" width="160">
      <div style="font-size:1.6rem; font-weight:600; color:#10B981;">460+</div>
      <div style="font-size:0.75rem; color:#888; letter-spacing:0.1em; text-transform:uppercase;">Tests Passed</div>
    </td>
    <td align="center" width="160">
      <div style="font-size:1.6rem; font-weight:600; color:#10B981;">0%</div>
      <div style="font-size:0.75rem; color:#888; letter-spacing:0.1em; text-transform:uppercase;">Data Leakage</div>
    </td>
    <td align="center" width="160">
      <div style="font-size:1.6rem; font-weight:600; color:#10B981;">Local</div>
      <div style="font-size:0.75rem; color:#888; letter-spacing:0.1em; text-transform:uppercase;">First Execution</div>
    </td>
  </tr>
</table>

</div>

---

## GitHub Analytics

<div align="center">

<table border="0">
  <tr>
    <td align="center" width="50%">
      <img src="https://github-readme-stats-eight-theta.vercel.app/api?username=reshandytaftazani&show_icons=true&theme=tokyonight&hide_border=true&bg_color=1a1b26&title_color=7aa2f7&icon_color=7dcfff&text_color=a9b1d6" alt="GitHub Stats" width="100%" />
    </td>
    <td align="center" width="50%">
      <img src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=reshandytaftazani&layout=compact&theme=tokyonight&hide_border=true&bg_color=1a1b26&title_color=7aa2f7&text_color=a9b1d6" alt="Top Languages" width="100%" />
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <img src="https://streak-stats.demolab.com/?user=reshandytaftazani&theme=tokyonight&hide_border=true&background=1a1b26&stroke=7aa2f7&ring=7aa2f7&fire=ff9e64&currStreakNum=c0caf5&sideNums=c0caf5&currStreakLabel=7aa2f7&sideLabels=7aa2f7&dates=a9b1d6" alt="GitHub Streak" width="100%" />
    </td>
  </tr>
</table>

</div>

---

## Contact

<p align="center">
  <a href="https://www.linkedin.com/in/reshandy-taftazani-aulya/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  &nbsp;&nbsp;
  <a href="mailto:reshandy.taftazani@ui.ac.id">
    <img src="https://img.shields.io/badge/Email-Contact_Me-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/reshandytaftazani">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

<p align="center">
  <sub>Reshandy Taftazani Aulya &middot; Universitas Indonesia</sub>
</p>

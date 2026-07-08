# Probabilistic Forecasting Evaluation with Large Language Models
## Training Curriculum: 10 Session Program

**Project:** Systematically evaluate the ability of LLMs to generate probabilistic and distributional forecasts, benchmarked against classical methods using proper scoring rules.

**Student level:** Complete beginner in probabilistic forecasting and LLM APIs.

**Supervisor:** Jude Ighomena, Janna-AI Research Labs

---

## How This Curriculum Works

Every session has three parallel components that connect to each other:

```
learn/   Read this first. Concepts, theory, intuition, diagrams in text.
  |
  | what you understood becomes your specification
  v
build/   Do this second. Open Claude Code desktop app and build the code.
  |
  | what you built becomes your evidence
  v
paper/   Do this third. Turn what you learned and built into a paper section.
```

By Session 10, you will have:
- A solid foundation in probabilistic forecasting and LLM evaluation
- A working end-to-end benchmarking pipeline built incrementally
- A complete research paper drafted section by section

Each session builds directly on the previous one. Do not skip ahead.

---

## The 10 Sessions

| Session | Topic | What You Build | Paper Contribution |
|---|---|---|---|
| 01 | Probability and Uncertainty | Python environment + distribution visualiser | Introduction |
| 02 | Forecasting: Point vs Probabilistic | Point and interval forecast functions | Problem Statement |
| 03 | LLMs and APIs | First LLM API call, parse a response | Related Work |
| 04 | Prompt Engineering for Structured Output | LLM forecaster module (quantiles + intervals) | Methodology: LLM Querying |
| 05 | Time Series Data and Benchmark Datasets | Data loaders for 2 benchmark datasets | Methodology: Data |
| 06 | Proper Scoring Rules (CRPS and Log-Score) | Scoring module: CRPS and Log-Score | Methodology: Evaluation Metrics |
| 07 | Calibration: PIT, Reliability, Sharpness | Calibration plots and PIT histogram | Methodology: Calibration |
| 08 | Classical Forecasting Baselines | Baseline models: ARIMA, Quantile Regression | Methodology: Baselines |
| 09 | Benchmarking Framework | Full pipeline: config-driven end-to-end run | Experiments |
| 10 | Results Analysis and Synthesis | Final results tables, plots, and report | Results, Conclusion |

---

## Folder Structure

```
PROBABILITY-PIPELINE-PROJECT-TRAINING/
|
|-- README.md                              (this file)
|
|-- Session_01_Probability_and_Uncertainty/
|   |-- learn/   session_01_learn.md
|   |-- build/   probability_demo.py
|   |-- paper/   paper_contribution.md
|
|-- Session_02_Forecasting_Types/
|-- Session_03_LLMs_and_APIs/
|-- Session_04_Prompt_Engineering/
|-- Session_05_Datasets/
|-- Session_06_Scoring_Rules/
|-- Session_07_Calibration/
|-- Session_08_Classical_Baselines/
|-- Session_09_Benchmarking_Framework/
|-- Session_10_Results_and_Synthesis/
|
|-- pipeline/                              (the growing codebase)
    |-- data/
    |-- models/
    |-- scoring/
    |-- results/
    |-- tests/
```

---

## The Pipeline

The `pipeline/` folder at the root is the living codebase. Every build task in every session adds a new piece to it. After Session 9, it is a complete, runnable benchmarking system.

```
pipeline/
|-- data/       loaders for benchmark datasets
|-- models/     LLM adapters and classical baseline implementations
|-- scoring/    CRPS, Log-Score, calibration metrics
|-- results/    output tables and plots (generated, not hand-written)
|-- tests/      one test per module, written alongside the module
```

---

## Tools Used

- **Python 3.11+** with numpy, scipy, pandas, matplotlib
- **Claude Code desktop app** for building pipeline code session by session
- **Anthropic API** (Claude Sonnet) as the primary LLM under evaluation
- **OpenAI API** (GPT-4o) as the secondary LLM
- **statsmodels** for ARIMA baseline
- **properscoring** library for CRPS computation

---

## Prerequisites

The student is expected to have:
- Python installed (any version 3.9+)
- A code editor or IDE (VS Code recommended)
- Claude Code desktop app installed
- API keys for Anthropic (and optionally OpenAI) stored in environment variables, never in code

Everything else is taught from scratch in the sessions.

---

## Reading List (from the project brief)

- Jordan, A., Kruger, F., Lerch, S. (2019). Evaluating Probabilistic Forecasts with scoringRules. Journal of Statistical Software, 90(12).
- Gneiting, T., Katzfuss, M. (2014). Probabilistic forecasting. Annual Review of Statistics and Its Application, 1, 125-151.
- Allen, S., et al. (2025). In-sample calibration yields conformal calibration guarantees. arXiv:2503.03841.

---

Start at Session 01. Read `learn/session_01_learn.md` first.

# CLAUDE.md: Project Instructions for Claude Code Desktop
# Probabilistic Forecasting Evaluation with Large Language Models
# Active version: Session 01

---

## What This Project Is

This is a school research project. The goal is to find out whether large language models like Claude, GPT-4o, and Llama can produce honest and accurate probability distributions when asked to make forecasts.

The project has three outputs that are built at the same time across ten sessions:

1. A working Python benchmarking pipeline that queries LLMs for probabilistic forecasts and scores their quality
2. A research paper documenting the method, experiments, and findings
3. A student who understands the theory and tools well enough to explain every part of what was built

---

## Who the Student Is

The student is a complete beginner. They have no prior experience with probability theory, machine learning, or research pipelines. They are intelligent and motivated, but they need concepts explained from first principles with real examples.

When helping the student, always:

- Use plain language. Never assume they know a term unless it appears in the vocabulary list at the bottom of this file.
- Give a real-world example for every abstract idea.
- Connect every coding task back to the concept it demonstrates.
- If they make an error, explain what went wrong and why before suggesting a fix.
- Encourage them to read the learn file for the current topic before asking you to write code for it.

---

## How This Project Is Structured

Each session has a folder. Inside each session folder there are four things:

- INTRO.md: the session overview, read first
- CLAUDE.md: the reference copy of this file for that session
- learn/: one file per topic, explaining the concept and how to apply it here
- build/: one Python file per topic, building the pipeline piece by piece
- paper/: one file per topic, drafting the corresponding section of the research paper

The learn file, build file, and paper file for each topic are numbered to match. Topic 1 has learn/01, build/01, and paper/01. They are a connected set.

---

## Rules That Apply to Every File in This Project

No em dashes anywhere. Not in code comments, not in markdown files, not in paper drafts. If you are about to type one, use a comma, a colon, or split it into two sentences instead.

No markdown bold syntax in prose. Do not write **word** in any student-facing document. Use plain text.

No backticks in prose. Only use backtick formatting inside actual code blocks.

API keys are never written into code files. Always read them from environment variables.

Every Python file must have a clear docstring at the top explaining what it does and which learn file it connects to.

---

## Current Session: Session 01

The student is working on Session 01: Probability and Uncertainty.

The seven topics in this session are:

1. What probability is
2. What a random variable is
3. What a probability distribution is
4. The three key distributions: Gaussian, Laplace, and Uniform
5. The difference between a point prediction and a predictive distribution
6. The two types of uncertainty: aleatoric and epistemic
7. What it means to ask an LLM to make a probabilistic forecast

When the student asks for help with code in this session, the code should demonstrate these concepts directly. Keep the code simple, readable, and well-commented. The student is learning to read and write Python for the first time in a research context.

---

## Pipeline Architecture So Far

The pipeline is being built from scratch across ten sessions. At the end of Session 01, the pipeline will have its first layer: a set of utility functions for working with probability distributions.

The pipeline lives in the pipeline/ folder at the project root. Code written in each session's build/ folder gets refined and moved into pipeline/ as the project matures.

Current pipeline folders:
- pipeline/data/: empty, will hold dataset loaders from Session 05
- pipeline/models/: empty, will hold LLM and baseline model adapters from Session 03
- pipeline/scoring/: empty, will hold CRPS and Log-Score functions from Session 06
- pipeline/results/: empty, will hold experiment outputs from Session 09
- pipeline/tests/: empty, will hold tests written alongside each module

---

## Vocabulary the Student Knows After Session 01

Add to this list at the end of each session.

- Probability: a number between 0 and 1 that measures how likely something is
- Random variable: a quantity whose value is uncertain before it is observed
- Probability distribution: a description of all possible values and how likely each is
- PDF: probability density function, the curve that describes a continuous distribution
- Gaussian distribution: a bell-shaped distribution defined by a mean and standard deviation
- Laplace distribution: a peaked distribution with heavier tails than Gaussian
- Uniform distribution: a flat distribution where every value in a range is equally likely
- Mean: the expected value, the centre of a distribution
- Standard deviation: how spread out a distribution is around its mean
- Point prediction: a single number forecast with no uncertainty information
- Predictive distribution: a full probability distribution over possible future outcomes
- Aleatoric uncertainty: randomness that is built into the world and cannot be reduced
- Epistemic uncertainty: uncertainty from lack of knowledge that can be reduced with more data
- Calibration: whether a forecaster's stated confidence matches how often they are right

---

## How to Update This File

At the end of each session, this file is updated with:
- The new active session number and topic list
- Any new pipeline folders or modules added
- New vocabulary terms the student has learned
- Any new rules or decisions made during the session

The updated version is then saved as the reference CLAUDE.md inside the next session folder.

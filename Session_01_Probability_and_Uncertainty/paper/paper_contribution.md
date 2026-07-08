# Paper Contribution — Session 01
## Section: Introduction

This file contains your contribution to the research paper for Session 01.
Complete this AFTER reading the learn file and AFTER running the build code.

---

## Your Task

Write the Introduction section of your research paper.

The Introduction must answer four questions, in this order:

1. Why does probabilistic forecasting matter?
2. What do current approaches do well and where do they fall short?
3. What is the gap this project fills?
4. What will the reader find in the rest of the paper?

Each question corresponds to one paragraph. You will write all four below.

---

## Paragraph 1 — Why Probabilistic Forecasting Matters

This paragraph makes the case for the whole project. It should open with a
concrete real-world scenario that shows the cost of a wrong forecast.

Guidance: Think about a hospital, an electricity grid, or a financial market.
What happens when the forecast says "22 degrees" but does not say "with 80%
uncertainty"? What decision gets made wrong as a result?

Write 4 to 6 sentences.

[WRITE YOUR PARAGRAPH HERE]

---

## Paragraph 2 — What Exists and Where It Falls Short

This paragraph sets up the problem by acknowledging what already exists.
It should mention that LLMs are powerful general-purpose reasoners, and that
they are beginning to be used for forecasting tasks, but that their ability
to produce calibrated probabilistic forecasts has not been rigorously evaluated.

Key phrases to include:
- "probabilistic forecasting"
- "uncertainty quantification"
- "calibration"
- "proper scoring rules"

Write 4 to 6 sentences.

Starter sentence: "Large language models (LLMs) have demonstrated strong
performance across a wide range of intellectual tasks, including mathematical
reasoning, text generation, and knowledge retrieval. However, their ability
to produce reliable probabilistic forecasts — outputs that capture the full
distribution of possible future values — remains largely unevaluated."

[WRITE YOUR PARAGRAPH HERE]

---

## Paragraph 3 — The Gap This Project Fills

This paragraph states clearly what the project does that has not been done
before. Be specific: you will benchmark multiple LLMs against classical
probabilistic models using proper scoring rules on real benchmark datasets.

Write 3 to 4 sentences.

Starter sentence: "This project addresses this gap by developing a systematic
evaluation pipeline that benchmarks the probabilistic forecasting ability of
several state-of-the-art LLMs against established classical and machine
learning forecasting methods."

[WRITE YOUR PARAGRAPH HERE]

---

## Paragraph 4 — Paper Outline

This paragraph tells the reader what they will find in each section.
You will fill this in properly once all sections exist.
For now, write a placeholder that lists the sections you know you will have.

Structure: "The remainder of this paper is organised as follows. Section 2...
Section 3... Section 4... Section 5..."

Sections to plan for:
- Related Work (Session 03)
- Methodology: LLM querying, datasets, scoring rules, baselines (Sessions 04-08)
- Experiments (Session 09)
- Results and Discussion (Session 10)
- Conclusion (Session 10)

[WRITE YOUR PARAGRAPH HERE]

---

## Figure to Include

After running `build/probability_demo.py`, a file called
`session_01_distributions.png` will be saved in the build folder.

Copy it here or reference it with this caption:

**Figure 1:** The four panels illustrate (a) the Gaussian distribution under
varying levels of confidence, (b) the heavier tails of the Laplace distribution
compared to the Gaussian, (c) the Uniform distribution as a representation of
maximum uncertainty, and (d) the key distinction between a point prediction
and a full predictive distribution. The remainder of this paper is concerned
with evaluating how well LLMs produce forecasts of the type shown in panel (d).

---

## Key Terms to Define in the Paper

Include a short definition of each of these terms the first time they appear
in your Introduction. Do not assume the reader knows them.

| Term | Your Definition (write in your own words) |
|---|---|
| Probabilistic forecasting | |
| Predictive distribution | |
| Calibration | |
| Proper scoring rule | |
| Point prediction | |

---

## Self-Review Checklist

Before marking this session complete, check:

- [ ] Paragraph 1 opens with a concrete real-world scenario
- [ ] Paragraph 2 mentions LLMs and the calibration gap
- [ ] Paragraph 3 states clearly what this project does
- [ ] Paragraph 4 previews the structure of the paper
- [ ] Figure 1 is referenced in the text
- [ ] All five key terms are defined on first use
- [ ] No em dashes, bold markdown, or backticks in any prose
- [ ] All sentences are your own words, not copied from the learn file

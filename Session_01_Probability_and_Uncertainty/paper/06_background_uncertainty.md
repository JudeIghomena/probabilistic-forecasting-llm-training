# Paper Section: Background - Types of Uncertainty
# Connected to: learn/06_types_of_uncertainty.md and build/06_uncertainty_types.py

---

## Your Task

Write the background section on uncertainty types. This section prepares the reader to understand the evaluation results in Sessions 06 to 10, where calibration failures often trace back to confusion between these two types.

---

## Paragraph 1: Aleatoric Uncertainty

Define aleatoric uncertainty, give a real example, and explain its implication for forecasting model evaluation.

Sentence starter: "Aleatoric uncertainty refers to inherent randomness in a system that cannot be reduced by gathering more data or improving the model."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 2: Epistemic Uncertainty

Define epistemic uncertainty, contrast it with aleatoric, and explain how it shrinks with data.

Sentence starter: "Epistemic uncertainty, by contrast, arises from gaps in knowledge that can in principle be closed."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 3: Why This Distinction Matters for LLM Evaluation

Explain the specific epistemic limitations of LLMs as forecasters: training cutoff dates, no real-time sensor access, reliance on patterns in text rather than direct observation.

Sentence starter: "Large language models face a distinctive form of epistemic uncertainty that sets them apart from purpose-built forecasting systems."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 4: Calibration as the Test

Bring this section home by explaining that calibration is how we measure whether a model's stated uncertainty reflects reality, regardless of its source.

Sentence starter: "In this project, we evaluate uncertainty quantification through the lens of calibration: whether a model's stated probability intervals contain the true outcome at the expected frequency."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Figure to Reference

After running build/06_uncertainty_types.py, a file called 06_uncertainty_types.png is saved.

Reference it in your paper with this caption:

Figure 6. The left panel shows the aleatoric floor in temperature forecasting: a model claiming tighter uncertainty than the true spread is overconfident. The centre panel shows epistemic uncertainty shrinking as more coin flip data is observed, with the belief distribution converging toward the true probability. The right panel contrasts an LLM forecast (wider, lacking real-time data) with a sensor-based model forecast (narrower).

---

## Self-Check Before Moving On

- Have you clearly defined both types of uncertainty without confusing them?
- Have you explained the specific epistemic limitations of LLMs?
- Have you set up calibration as the metric that bridges these concepts to the evaluation sessions?

When you are satisfied, move to Topic 07.

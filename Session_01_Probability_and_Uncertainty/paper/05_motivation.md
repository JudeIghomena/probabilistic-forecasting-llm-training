# Paper Section: Motivation
# Connected to: learn/05_point_vs_predictive.md and build/05_point_vs_predictive.py

---

## Your Task

Write the motivation section of your paper. This is the section that makes the reader feel the problem viscerally. Use the farmer scenario from the build file. Make it concrete and specific.

---

## Paragraph 1: The Hidden Information Problem

Use the farmer example to show what a point prediction hides. Do not be abstract. Describe the situation, the decision, and the cost of having only a point prediction.

Sentence starter: "Consider a farmer deciding whether to harvest a crop this week. A weather forecast predicts 19 degrees for tomorrow. Based on this single number, the farmer proceeds."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 2: What the Distribution Reveals

Continue the farmer scenario. Show how the predictive distribution from Model B changes the decision. Use the actual numbers from the build file output (16 percent frost risk).

Sentence starter: "A probabilistic forecast, however, reveals a 16 percent probability that the temperature will fall below the frost threshold of 14 degrees."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 3: Generalising the Problem

Step back from the farmer scenario and generalise. This problem applies to hospitals, electricity grids, financial markets, and anywhere else that decisions depend on uncertain future quantities.

Sentence starter: "This gap between point predictions and distributional forecasts is not specific to agricultural planning."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 4: Why LLMs Specifically

Bring the motivation back to the specific research question. LLMs are being increasingly used in decision-support contexts. If they cannot produce reliable distributional forecasts, this is a problem worth documenting.

Sentence starter: "Large language models are increasingly deployed in contexts where their outputs influence real decisions."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Figure to Reference

After running build/05_point_vs_predictive.py, a file called 05_point_vs_predictive.png is saved.

Reference it in your paper with this caption:

Figure 5. The left panel shows two forecasting models with the same point prediction (19 degrees) but very different uncertainty levels. The centre panel shows the quantile format representation of the confident model's distribution. The right panel shows the frost risk scenario: the same point prediction hides a 2 percent frost risk under Model A but a 16 percent frost risk under Model B.

---

## Self-Check Before Moving On

- Have you used a specific, concrete scenario rather than abstract language?
- Have you used real numbers from the build file output?
- Have you clearly connected the motivation back to the LLM evaluation problem?

When you are satisfied, move to Topic 06.

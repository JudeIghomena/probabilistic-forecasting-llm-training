# Paper Section: Background - Distribution Families
# Connected to: learn/04_key_distributions.md and build/04_key_distributions.py

---

## Your Task

Write the background section that introduces the three distribution families used in this project. This section should read like a concise technical reference. Each distribution gets its own paragraph.

---

## Paragraph 1: The Gaussian Distribution

Introduce the Gaussian distribution, its parameters, its shape, and when it is appropriate. Mention its main limitation (thin tails).

Sentence starter: "The Gaussian distribution, also known as the normal distribution, is the most widely used continuous probability distribution in scientific forecasting."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 2: The Laplace Distribution

Introduce the Laplace distribution, contrast it with the Gaussian, and explain when it is a better choice.

Sentence starter: "The Laplace distribution, also known as the double exponential distribution, shares the symmetric bell shape of the Gaussian but assigns substantially more probability to values far from the centre."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 3: The Uniform Distribution

Introduce the Uniform distribution and its role in this project as a no-information baseline.

Sentence starter: "The Uniform distribution assigns equal probability to all values within a bounded range and zero probability outside it."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 4: Why These Three

Explain why these three distributions were chosen for this project and how they will be used in evaluation.

Sentence starter: "These three distribution families are not exhaustive, but they represent distinct regimes of forecasting behaviour: confident and symmetric, heavy-tailed, and maximally uninformative."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Figure to Reference

After running build/04_key_distributions.py, a file called 04_key_distributions.png is saved.

Reference it in your paper with this caption:

Figure 4. The three panels compare the Gaussian, Laplace, and Uniform distributions. The left panel shows their PDFs, illustrating differences in shape and peak. The centre panel shows their CDFs, highlighting how probability accumulates differently across the three. The right panel shows the PDFs on a logarithmic scale, making the heavier tails of the Laplace distribution visible compared to the Gaussian.

---

## Self-Check Before Moving On

- Have you defined each distribution's parameters clearly?
- Have you explained what makes the Laplace different from the Gaussian in plain language?
- Have you justified why these three distributions were chosen rather than others?

When you are satisfied, move to Topic 05.

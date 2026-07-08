# Paper Section: Background - Probability Distributions
# Connected to: learn/03_probability_distributions.md and build/03_distributions.py

---

## Your Task

Write the background section on probability distributions. This section gives your reader the technical vocabulary they need to follow the rest of the paper.

Write as if your reader is intelligent but has not studied statistics. Every technical term must be explained the first time it appears.

---

## Paragraph 1: What a Distribution Is

Introduce the concept of a probability distribution for a continuous random variable. Explain what the shape of the distribution communicates. Use the temperature forecast as your concrete example.

Sentence starter: "For a continuous random variable such as tomorrow's maximum temperature, a probability distribution describes the full range of values that variable might take and assigns a likelihood to each region of that range."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 2: The PDF

Explain what a probability density function is, what the curve represents, and the rule that the total area under the curve equals 1. Explain how areas correspond to probabilities.

Sentence starter: "The probability density function, or PDF, is the curve that describes a continuous distribution. At any point on the curve, the height represents how densely the probability is concentrated near that value."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 3: The CDF and Percentiles

Explain the cumulative distribution function and why it is useful. Explain what a percentile is in this context. This is important because later sections of the paper will discuss quantile forecasts and scoring rules that rely on the CDF.

Sentence starter: "The cumulative distribution function, or CDF, provides a complementary view. For any value x, the CDF gives the probability that the random variable is less than or equal to x."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 4: Why Shape Matters

Explain that two distributions can have the same expected value but very different shapes, and that this difference matters enormously for decision-making. Reference the three distributions from the build file with different standard deviations.

Sentence starter: "Two forecasts with the same expected value can represent very different levels of confidence depending on the spread of their distributions."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Figure to Reference

After running build/03_distributions.py, a file called 03_distributions.png is saved.

Reference it in your paper with this caption:

Figure 3. The left panel shows the PDF for a Gaussian temperature model with the probability of falling between 13 and 23 degrees shaded in orange. The centre panel shows the corresponding CDF, rising from 0 to 1 as temperature increases. The right panel shows three distributions with the same mean but different standard deviations, illustrating how spread communicates forecast confidence.

---

## Self-Check Before Moving On

- Have you explained PDF and CDF in plain language without losing precision?
- Have you shown why the area-equals-probability rule matters?
- Have you made clear that shape, not just the mean, carries important information?

When you are satisfied, move to Topic 04.

# Paper Section: Problem Statement
# Connected to: learn/02_random_variables.md and build/02_random_variables.py

---

## Your Task

Write the problem statement section of your research paper. This section formally defines what the project is trying to solve.

A good problem statement does three things:

1. Defines the forecasting task precisely using the vocabulary you have learned
2. Explains what makes a forecast good or bad in this context
3. States the specific gap in the literature that this project addresses

---

## Paragraph 1: Defining the Forecasting Task

Use the concept of a random variable to define what a forecast is. Explain that a forecast target (such as temperature, energy demand, or a financial return) is a random variable. Explain what it would mean for a model to describe that random variable well.

Sentence starter: "In this work, we define a forecasting task as the problem of characterising a random variable X that represents some real-world quantity of interest at a future point in time."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 2: Point Predictions Are Not Enough

Use the distinction between discrete and continuous random variables to make the case that a single number cannot fully describe a continuous quantity. Explain what information is lost when you reduce a full distribution to one number.

Sentence starter: "A point prediction collapses the full uncertainty of a random variable into a single value. For a continuous random variable, this means discarding information about the spread, the tails, and the shape of the distribution."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 3: What a Good Model Should Produce

Describe what an ideal probabilistic forecasting model would produce. Use the temperature example from the build file as a concrete case. Reference the expected value and the probability of falling in a range.

Sentence starter: "An ideal probabilistic forecasting model does not predict a single temperature value. Instead, it produces a distribution over all possible values, from which a forecaster can extract not only the most likely outcome but also the probability of any specific event."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 4: The Research Problem

State clearly what is unknown and what this project sets out to investigate. The research problem is whether large language models can produce the kind of full distributional forecast described in paragraph 3.

Sentence starter: "It remains an open question whether large language models, which are trained on natural language and not optimised for probabilistic reasoning, are capable of producing calibrated distributional forecasts."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Figure to Reference

After running build/02_random_variables.py, a file called 02_random_variables.png is saved.

Reference it in your paper with this caption:

Figure 2. The three panels illustrate key properties of random variables. The left panel shows a discrete random variable (die roll) with its expected value marked. The centre panel shows a continuous random variable (temperature) modelled as a Gaussian distribution, with the probability of falling between 18 and 22 degrees shaded. The right panel shows 20 samples drawn from the temperature model, demonstrating how individual observations relate to the underlying distribution.

---

## Key Terms to Use in This Section

Make sure you have used these terms correctly at least once in your paragraphs:

- random variable
- continuous random variable
- expected value
- probability distribution
- point prediction
- distributional forecast

---

## Self-Check Before Moving On

- Does your problem statement use precise mathematical language alongside plain explanations?
- Have you made clear why point predictions are insufficient without being vague?
- Is your research problem stated as a question that can actually be investigated?

When you are satisfied, move to Topic 03.

# Topic 03: Probability Distributions

Build file for this topic: build/03_distributions.py
Paper file for this topic: paper/03_background_distributions.md

---

## Start Here

In Topic 02 you learned that a random variable is a quantity whose value is uncertain. But knowing that X is uncertain is not very useful on its own. You need to know something more specific: which values are likely, which are unlikely, and how the chances spread across the full range?

That full picture is called a probability distribution. It is the most important tool in this entire project.

---

## What a Probability Distribution Is

A probability distribution describes every possible value a random variable can take and assigns a probability to each one.

For a discrete random variable, like a die roll, the distribution is a list: outcome 1 happens with probability 1/6, outcome 2 with probability 1/6, and so on. You can draw it as a bar chart, with one bar per possible outcome and the height of each bar showing the probability.

For a continuous random variable, like temperature, you cannot list every value because there are infinitely many. Instead, the distribution is described by a curve called a probability density function, or PDF for short. The curve sits over the number line. A tall section of the curve means values in that region are likely. A low section means they are unlikely.

Think of the PDF like a hill over a number line. The highest part of the hill is where the random variable is most likely to land. The tails of the hill, where it slopes down toward the ground, are where unlikely outcomes live.

---

## How to Read a PDF

Here is what different shapes tell you:

A narrow, tall peak means the random variable is very likely to be near the centre. There is not much uncertainty. The forecaster is confident.

A wide, flat shape means the random variable could be almost anywhere in the range. There is a lot of uncertainty. The forecaster is not very confident.

A shape that is taller on one side than the other (called skewed) means the random variable is more likely to end up on one side of the centre than the other. Rain totals are often skewed because you can have zero rain or a little rain on most days, but occasionally have a very large amount.

---

## The Key Rule: Area Under the Curve Equals 1

For any probability distribution, the total area under the PDF curve must equal exactly 1. This is not a coincidence. It is the mathematical expression of a simple idea: something must happen.

If you add up all the probabilities across every possible outcome, you always get 1. This is as true for a continuous distribution as it is for a discrete one.

This rule is useful because it lets you interpret areas as probabilities. If you shade the area under the curve between 18 and 22 degrees, the area of that shaded region equals the probability that the temperature falls in that range.

---

## The Cumulative Distribution Function

Alongside the PDF, there is a related function called the cumulative distribution function, or CDF. While the PDF tells you the density at a particular value, the CDF tells you the probability that the random variable is less than or equal to some value.

Formally: CDF(x) = P(X is less than or equal to x)

The CDF starts at 0 on the far left (nothing is smaller than negative infinity) and rises to 1 on the far right (everything is smaller than positive infinity). It is always an S-shaped curve, going from 0 to 1 as you move left to right.

The CDF is extremely useful for this project. When you want to know what value corresponds to the 90th percentile of a forecast, you use the CDF. When you score a probabilistic forecast using the proper scoring rules introduced in Session 06, the CDF is involved in the calculation.

---

## Why This Matters for the Project

When we ask an LLM to make a probabilistic forecast, we are asking it to produce something that behaves like a PDF. It should tell us the full shape of the distribution over possible future values.

In practice, we will ask LLMs to express this distribution in different formats: as a list of quantiles, as the parameters of a named distribution, or as a set of samples. All of these are ways of communicating the shape of the distribution without drawing the curve itself.

The better an LLM's distribution matches the true distribution of outcomes, the better its forecasts. Measuring that match is what Sessions 06 and 07 are about.

---

## Check Your Understanding

1. What is the difference between a PDF and a CDF?
2. What does it mean for a PDF curve to be narrow and tall?
3. If the area under a PDF between 15 and 20 degrees is 0.4, what does that tell you?
4. What must the total area under any PDF equal? Why?
5. You look at a PDF and notice the right tail is much longer than the left. What does this tell you about the distribution?

---

## What to Do Next

Open build/03_distributions.py in Claude Code Desktop and run it.

When you are done, open paper/03_background_distributions.md and write your draft.

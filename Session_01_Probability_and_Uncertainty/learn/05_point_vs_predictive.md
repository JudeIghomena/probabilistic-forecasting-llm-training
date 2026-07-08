# Topic 05: Point Predictions vs Predictive Distributions

Build file for this topic: build/05_point_vs_predictive.py
Paper file for this topic: paper/05_motivation.md

---

## Start Here

This is the most important topic in Session 01. Everything else in this project exists because of the problem you are about to learn.

Up until now you have been learning tools: probability, random variables, distributions. This topic shows you what is at stake when those tools are not used.

---

## What a Point Prediction Is

A point prediction is a single number given as the forecast for something uncertain.

"The temperature tomorrow will be 19 degrees."
"This patient has a 7 percent chance of readmission." (This is actually a probability, not a point prediction.)
"The train arrives at 14:32."
"The stock will close at 142.50."

Every forecast you have seen in everyday life is almost certainly a point prediction. They are familiar, easy to communicate, and easy to check after the fact.

But they are hiding something.

---

## What a Point Prediction Cannot Tell You

Suppose two different forecasting models both predict 19 degrees for tomorrow.

Model A made this prediction because 19 degrees is a very typical day in this location at this time of year. The model is highly confident. It would be very surprised by anything below 14 or above 24 degrees.

Model B made this prediction because it had almost no useful data for this location. It picked 19 degrees as a rough guess. It thinks the temperature could easily be anywhere between 5 and 33 degrees.

Both models say 19. Neither point prediction tells you which situation you are in.

If you are a farmer deciding whether to harvest this week, those two situations lead to completely different decisions. If you are a utility company managing power demand, they mean very different things for how much reserve capacity you need.

The point prediction gives you the same number in both cases. The predictive distribution gives you the full picture.

---

## What a Predictive Distribution Gives You Instead

A predictive distribution replaces the single number with a full probability distribution over all possible outcomes.

Instead of saying "the temperature will be 19 degrees," a probabilistic forecast says "the temperature is most likely around 19 degrees, with a 90 percent chance of falling between 14 and 24 degrees, and a small but real chance of being above 28 or below 10."

This forecast contains the point prediction (19 degrees) as a special case. But it also contains:

- A measure of confidence. How wide or narrow is the distribution?
- Information about the tails. What is the chance of extreme outcomes?
- A principled way to make decisions under uncertainty. You can use the distribution to weigh costs and benefits of different actions.

The predictive distribution is strictly more informative than the point prediction. It is never less useful. It is always at least as useful, and usually much more so.

---

## How This Connects to Evaluating LLMs

In this research project, we are asking large language models to produce predictive distributions, not point predictions.

This is an unusual request. LLMs are primarily trained to produce text, and their training does not explicitly teach them to output calibrated probability distributions. When you ask an LLM "what is the probability that the temperature tomorrow will be between 18 and 22 degrees," it might give a number, but whether that number is trustworthy is exactly what this project is investigating.

A model that says "90 percent chance" when it should say "60 percent chance" is overconfident. A model that says "50 percent chance" for everything is under-informative. In both cases, the point prediction extracted from the model might look reasonable, but the distribution reveals the problem.

This is why we evaluate distributions, not just point predictions.

---

## Three Formats for Expressing a Predictive Distribution

When we query LLMs in this project, we will ask them to express their forecast distributions in three different formats. You will build these in Sessions 04 and 05.

The first format is quantiles. A quantile forecast gives specific percentile values. For example: "the 10th percentile is 13 degrees, the 50th is 19, and the 90th is 25." These three numbers sketch the shape of the distribution.

The second format is parametric. The model names a distribution family and gives its parameters. For example: "I believe the temperature follows a Gaussian distribution with mean 19 and standard deviation 4." This is very compact but assumes the model knows which family to use.

The third format is samples. The model provides a list of possible values drawn from its implied distribution. For example: "18.2, 21.4, 17.8, 23.1, 15.6..." A set of samples can be analysed to recover the full shape.

All three formats are ways of communicating a distribution. All three will be used and compared in this project.

---

## Check Your Understanding

1. Two models both predict 19 degrees. Model A is highly confident and Model B is very uncertain. Can you tell the difference from their point predictions alone?
2. What does a predictive distribution tell you that a point prediction does not?
3. What does it mean for a model to be overconfident?
4. Name the three formats for expressing a predictive distribution.
5. Why is a predictive distribution said to be strictly more informative than a point prediction?

---

## What to Do Next

Open build/05_point_vs_predictive.py in Claude Code Desktop and run it.

When you are done, open paper/05_motivation.md and write your draft.

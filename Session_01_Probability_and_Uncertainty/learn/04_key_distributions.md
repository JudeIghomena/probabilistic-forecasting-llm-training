# Topic 04: The Three Key Distributions

Build file for this topic: build/04_key_distributions.py
Paper file for this topic: paper/04_background_families.md

---

## Start Here

Now that you understand what a probability distribution is, you need to meet the three specific distributions that appear throughout this project. You will see them in the code, in the paper, and in how we interpret LLM forecast outputs.

Each one has a different shape and a different character. Think of them as three different personalities, each suited to a different type of uncertainty.

---

## Distribution 1: The Gaussian (Normal) Distribution

The Gaussian distribution is the most common distribution in science and statistics. You have probably seen its shape before: a symmetric bell curve, highest in the middle and tapering off equally on both sides.

It is defined by two numbers:

- The mean (written as the Greek letter mu). This is the centre of the bell. The most likely value.
- The standard deviation (written as the Greek letter sigma). This controls how wide or narrow the bell is. A small sigma means the distribution is narrow and confident. A large sigma means it is wide and uncertain.

The notation for a Gaussian distribution is X ~ N(mu, sigma squared). The squiggly symbol means "is distributed as."

Real-world examples of Gaussian distributions: heights of adult humans, measurement errors in physical experiments, returns on financial assets over short time periods.

Why it matters for this project: the Gaussian is our default model when we believe an LLM's forecast should cluster around a central value with symmetric uncertainty. It is the simplest and most well-understood distribution for continuous forecasting targets.

Its main weakness: it has thin tails. The Gaussian assigns very low probability to extreme events. In reality, extreme events often happen more frequently than a Gaussian would predict. This is where the Laplace distribution becomes useful.

---

## Distribution 2: The Laplace Distribution

The Laplace distribution looks similar to the Gaussian at first glance. It has a peak in the middle and tapers off on both sides. But there is an important difference: it has heavier tails.

Heavier tails means that values far from the centre are more likely under a Laplace than under a Gaussian with the same spread. If you are forecasting something where large surprises happen more often than a Gaussian would predict, the Laplace is a more honest model.

It is defined by two numbers:

- The location parameter mu. The centre and most likely value.
- The scale parameter b. Controls the spread.

The notation is X ~ Laplace(mu, b).

Real-world examples: differences in daily temperature between consecutive days, log returns of financial assets over longer periods, prediction errors in language model outputs.

Why it matters for this project: when we score LLM forecasts, we will compare them against both Gaussian and Laplace models. If an LLM's forecast behaves more like a Laplace (heavier tails), that tells us something about how it reasons about unlikely events.

---

## Distribution 3: The Uniform Distribution

The Uniform distribution is the simplest possible distribution. Every value in a range is equally likely. The curve is a flat horizontal line between two points and zero everywhere else.

It is defined by two numbers:

- The lower bound a. The smallest possible value.
- The upper bound b. The largest possible value.

The notation is X ~ Uniform(a, b).

A uniform distribution says: I know the value is somewhere between a and b, but I have no idea where in that range. Every point is equally likely. This represents maximum uncertainty within a bounded range.

Real-world examples: the minute within an hour when a bus arrives at a stop with no schedule, the outcome of a perfectly randomised lottery draw.

Why it matters for this project: the Uniform distribution is our baseline for what a completely uninformed forecast looks like. If an LLM gives us a forecast that looks uniform, it is essentially saying it has no useful information about the target. A model that performs no better than a uniform distribution over a sensible range is a poor probabilistic forecaster.

---

## Comparing the Three

| Property | Gaussian | Laplace | Uniform |
|---|---|---|---|
| Shape | Bell curve, symmetric | Peaked, heavier tails | Flat |
| Parameters | Mean, standard deviation | Location, scale | Lower bound, upper bound |
| Tail behaviour | Thin tails | Heavy tails | No tails (cut off at bounds) |
| Best for | Symmetric, well-behaved uncertainty | Uncertainty with occasional large surprises | Complete ignorance within a range |
| Used in this project as | Default forecast model | Alternative forecast model | Baseline (no-information) benchmark |

---

## Check Your Understanding

1. Which distribution has the heaviest tails?
2. If an LLM gives you a forecast that looks like a Uniform distribution over a very wide range, what does that tell you about its confidence?
3. You are forecasting daily electricity demand. You expect it to cluster around a typical value but occasionally have very high or very low days. Which distribution is a better fit, Gaussian or Laplace?
4. What does it mean for a distribution to have thin tails?

---

## What to Do Next

Open build/04_key_distributions.py in Claude Code Desktop and run it.

When you are done, open paper/04_background_families.md and write your draft.

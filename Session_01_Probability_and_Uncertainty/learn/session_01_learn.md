# Session 01 — Probability and Uncertainty

**Read this before opening any code or writing any paper.**

---

## What This Session Covers

By the end of this session you will understand:

1. What probability is and why it matters for forecasting
2. What a random variable is
3. What a probability distribution is and how to read one
4. The difference between discrete and continuous distributions
5. Three distributions you will use throughout this project
6. Why point predictions are not enough and what to do instead

---

## 1. What Is Probability?

Probability is a number between 0 and 1 that describes how likely something is to happen.

- 0 means impossible. It will not happen.
- 1 means certain. It will definitely happen.
- 0.5 means equally likely to happen or not happen.

### The Two Ways to Think About It

**Frequentist:** Probability is what fraction of the time something happens if you repeat the experiment many times. If you flip a fair coin 1000 times, it comes up heads about 500 times. So the probability of heads is 500/1000 = 0.5.

**Bayesian:** Probability is a degree of belief. Before seeing data, how confident are you that tomorrow will rain? You assign a number based on your knowledge. As you get more information, you update that number.

In this project we will use both interpretations, but the Bayesian framing will be more natural when thinking about what an LLM "believes" about the future.

---

## 2. Random Variables

A **random variable** is a quantity whose value is not yet known but could take several possible values, each with some probability.

Examples:
- Tomorrow's maximum temperature in London
- The closing price of a stock on Friday
- The number of customers who arrive at a shop in one hour

We usually call a random variable X. When we say X = 25 we mean the temperature turned out to be 25 degrees. But before it happens, X is uncertain.

---

## 3. Probability Distributions

A **probability distribution** describes all the possible values a random variable can take and how likely each one is.

Think of it as a shape drawn over a number line. The higher the shape at a particular number, the more likely the variable is to land near that number.

### Reading a Distribution

```
Probability
density
   |        /\
   |       /  \
   |      /    \
   |     /      \
   |____/        \____
   0   10   20   30   40    Temperature (degrees C)
```

In this shape, temperatures around 20 degrees are most likely. Very cold or very hot days are unlikely. The shape is a bell curve (Gaussian distribution).

The key rule: the total area under the curve always equals 1. All probabilities must sum to 100%.

---

## 4. Discrete vs Continuous Distributions

**Discrete** distributions apply to things that can only take specific values: number of goals scored (0, 1, 2, 3...), number of emails received today.

**Continuous** distributions apply to things that can take any value in a range: temperature, wind speed, stock price. These are described by a smooth curve called a probability density function (PDF).

For this project, we will mostly work with continuous distributions because we are forecasting things like temperature, energy demand, and stock prices.

---

## 5. Three Distributions You Will Use Throughout This Project

### 5.1 The Gaussian (Normal) Distribution

This is the most common distribution in nature. Many real measurements cluster around a middle value and become less likely the further away you go.

It is defined by two numbers:
- **Mean (mu):** where the centre of the bell is
- **Standard deviation (sigma):** how spread out the bell is

```
Narrow bell (sigma = 1)        Wide bell (sigma = 5)
      |                               |
      |    /\                         |  /          \
      |   /  \                        | /            \
      |  /    \                       |/              \
      |_/      \_                     /                \___
```

A small sigma means the variable is predictable. A large sigma means it is uncertain.

**Notation:** X ~ N(mu, sigma^2)

**Example:** If we think tomorrow's temperature is about 20 degrees and we are fairly confident, we might say X ~ N(20, 4). This means the mean is 20 and the standard deviation is 2.

### 5.2 The Laplace Distribution

Similar shape to the Gaussian, but with heavier tails. This means extreme values are more likely than a Gaussian would suggest.

- **Mean (mu):** where the centre is
- **Scale (b):** controls the spread

**When it matters:** In financial forecasting, extreme market moves happen more often than a Gaussian predicts. The Laplace distribution handles this better.

**Notation:** X ~ Laplace(mu, b)

### 5.3 The Uniform Distribution

Every value in a range is equally likely. There is no centre, no preferred value.

**Example:** You have no idea what the temperature will be tomorrow and you think it could be anything between 10 and 30 degrees.

**Notation:** X ~ Uniform(a, b) where a is the lower bound and b is the upper bound.

**When it matters:** Uniform distributions represent maximum uncertainty. If an LLM gives a forecast that looks uniform, it is telling you it has no idea.

---

## 6. Why Point Predictions Are Not Enough

Most of the forecasting you have seen in everyday life is a **point prediction**: one single number.

- "Tomorrow will be 22 degrees."
- "The company will earn 3.5 million this quarter."
- "The train arrives at 9:15."

Point predictions are convenient but they throw away critical information: **how confident is the forecaster?**

### The Problem in Practice

Imagine two weather forecasters:

- Forecaster A says: "22 degrees tomorrow."
- Forecaster B says: "22 degrees tomorrow, but it could be anywhere from 18 to 26."

If you are planning an outdoor wedding, these two forecasts lead to very different decisions. Forecaster B has given you much more useful information.

Now imagine the same comparison for a hospital deciding how much to stock emergency medicine, or an electricity grid deciding how much power to generate. Getting the distribution wrong can have serious consequences.

### The Solution: Predictive Distributions

Instead of giving one number, a good forecaster gives a **predictive distribution**: the full shape of all the possible outcomes and their probabilities.

This is what we will ask LLMs to do in this project. And then we will measure how good their distributions are using the scoring rules you will learn in Session 06.

---

## 7. Uncertainty vs Ignorance

One more important distinction:

**Aleatoric uncertainty:** randomness that is genuinely built into the world. Even if you had all the data, you could not predict the outcome exactly. The roll of a fair die is aleatoric.

**Epistemic uncertainty:** uncertainty that comes from not having enough information. In principle, with more data or better models, you could reduce this. An LLM that has never seen weather data from Antarctica has high epistemic uncertainty about Antarctic temperatures.

Both types of uncertainty need to appear in a good probabilistic forecast. A model that only captures one is incomplete.

---

## 8. Key Terms — Quick Reference

| Term | Meaning |
|---|---|
| Probability | A number 0-1 measuring how likely an event is |
| Random variable | A quantity whose value is uncertain |
| Distribution | The full description of all possible values and their probabilities |
| PDF | Probability density function, the curve describing a continuous distribution |
| Mean | The expected value, the centre of a distribution |
| Standard deviation | How spread out a distribution is |
| Point prediction | A single number forecast with no uncertainty information |
| Predictive distribution | A full probability distribution over future outcomes |
| Aleatoric uncertainty | Irreducible randomness in the world |
| Epistemic uncertainty | Uncertainty from lack of information or data |

---

## 9. What You Do Next

Go to the `build/` folder and open `probability_demo.py` in your code editor.

Run it step by step using Claude Code. Each function you see there directly corresponds to a concept in this document.

Then go to the `paper/` folder and open `paper_contribution.md`. Your task is to write the Introduction section of the research paper, guided by the template there.

---

## Check Your Understanding

Before moving to the build task, ask yourself these questions. If you cannot answer any of them, re-read the relevant section.

1. What is the difference between a discrete and a continuous distribution?
2. If X ~ N(10, 9), what is the mean and what is the standard deviation?
3. Why is a point prediction less informative than a predictive distribution?
4. In the weather forecasting example, which forecaster gave more useful information? Why?
5. What does aleatoric uncertainty mean? Give your own example.

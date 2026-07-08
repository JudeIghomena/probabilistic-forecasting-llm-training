# Topic 02: Random Variables

Build file for this topic: build/02_random_variables.py
Paper file for this topic: paper/02_problem_statement.md

---

## Start Here

Imagine you are about to flip a coin. Before the flip, you do not know if it will land heads or tails. The outcome is uncertain. Now imagine someone asks you to write a formula that captures that uncertainty.

That is exactly what a random variable is. It is a way of giving a name to something that has not happened yet but could take one of several values.

Random variables are the foundation of everything in probability and statistics. Once you understand them, the rest of this session will click into place quickly.

---

## What a Random Variable Is

A random variable is a quantity whose value depends on something uncertain, like the outcome of an experiment or a measurement that has not been taken yet.

We usually name random variables with capital letters like X, Y, or Z.

Here are some examples:

- X could represent the outcome of a die roll. X might be 1, 2, 3, 4, 5, or 6.
- Y could represent tomorrow's maximum temperature in London. Y might be 14.2 or 19.7 or 23.1.
- Z could represent the number of customers who walk into a shop this afternoon. Z might be 0, 12, or 47.

The key idea is that before the uncertain event happens, X is not a fixed number. It is a placeholder that represents the full range of possibilities.

Once the event happens, X takes a specific value. We write this as a lowercase letter. If the die lands on four, we write x = 4.

---

## Two Types of Random Variables

Random variables come in two flavours, and the type matters because it changes how you describe the probabilities.

The first type is discrete. A discrete random variable can only take specific, separate values. You can list them. The number of goals scored in a football match is discrete because it can be 0, 1, 2, 3, and so on, but never 1.7 or 2.3.

The second type is continuous. A continuous random variable can take any value in a range. Temperature is continuous because it could be 19.0 or 19.01 or 19.001. There are infinitely many possible values between any two numbers.

This distinction matters for how you calculate probabilities. For a discrete variable, you can ask "what is the probability that X equals exactly 3?" and get a meaningful answer. For a continuous variable, the probability of landing on any single exact value is essentially zero. Instead, you ask "what is the probability that X falls between 18 and 20?"

In this project, most of the quantities we are forecasting (temperature, energy demand, financial returns) are continuous. The tools we will use are designed for continuous random variables.

---

## Notation You Will See

In the research paper and in code, you will see this notation regularly.

X is the random variable. It represents the uncertain quantity before it is observed.

P(X = x) is the probability that X takes the specific value x. This notation is used for discrete variables.

P(a < X < b) is the probability that X falls between a and b. This notation is used for continuous variables.

E[X] is the expected value of X. This is the average outcome you would expect over many repetitions. For a fair die, E[X] = (1+2+3+4+5+6)/6 = 3.5.

Var(X) is the variance of X. This measures how spread out the possible values are. A large variance means X could end up far from its expected value.

---

## Why This Matters for the Project

In this research project, every forecast target is a random variable. When we ask an LLM to forecast the temperature tomorrow, we are asking it to describe the random variable X = "maximum temperature in London tomorrow."

A good LLM should not just give us one number. It should describe the full probability distribution of X. That distribution tells us the most likely value, but also how much uncertainty surrounds it.

In later sessions, you will see how we translate this idea into code and how we measure whether the distribution an LLM gives us is honest and accurate.

---

## Check Your Understanding

1. What is the difference between a random variable and a regular variable?
2. Is "the number of text messages received today" discrete or continuous?
3. Is "the exact time a train arrives at a station" discrete or continuous?
4. If X represents the outcome of a fair die roll, what is E[X]?
5. Why can you not ask "what is the probability that temperature equals exactly 20.0 degrees" for a continuous variable?

---

## What to Do Next

Open build/02_random_variables.py in Claude Code Desktop and run it.

When you are done, open paper/02_problem_statement.md and write your draft.

# Topic 01: What Is Probability?

Build file for this topic: build/01_probability_basics.py
Paper file for this topic: paper/01_introduction.md

---

## Start Here

Think about the last time someone told you it would rain tomorrow. They did not say "it will definitely rain" or "it will definitely not rain." They said something like "there is a 70 percent chance of rain."

That number, 70 percent, is a probability. And it contains more useful information than a simple yes or no ever could.

Probability is the mathematical tool we use to describe uncertainty honestly. It does not pretend to know things it does not know. Instead, it gives you a number that tells you exactly how confident someone is.

This project is built on probability. Every technique you will learn, every piece of code you will write, and every section of your research paper traces back to this one idea.

---

## What Probability Actually Is

Probability is a number that lives between 0 and 1.

- A probability of 0 means something is impossible. It will not happen.
- A probability of 1 means something is certain. It will definitely happen.
- A probability of 0.5 means something is equally likely to happen or not happen.
- A probability of 0.7 means something is more likely to happen than not.

You will also see probabilities written as percentages. A probability of 0.7 is the same as a 70 percent chance. Both mean the same thing.

Here are some examples to make this concrete:

| Situation | Probability | What It Means |
|---|---|---|
| Flipping a fair coin and getting heads | 0.5 | Equally likely either way |
| Rolling a six on a standard die | 0.167 | One outcome out of six possible |
| The sun rising tomorrow | 0.9999 | Nearly certain, but we write a small uncertainty |
| A randomly chosen person being taller than 2.5 metres | 0.001 | Very unlikely |

Notice that in everyday speech we sometimes say things like "it will definitely rain" or "there is no chance." In probability, we are more careful. We try to assign numbers instead of words, because numbers force us to be precise.

---

## Two Ways to Think About Probability

There are two main ways people interpret what a probability actually means. You will encounter both in this project.

The first way is called the frequentist interpretation. Under this view, a probability tells you what fraction of the time something happens if you repeat the same situation many times. If you flip a fair coin one million times, it comes up heads about 500,000 times. So the probability of heads is 0.5.

This interpretation works well when you can actually repeat an experiment. It does not work as well when you are making a one-time forecast. You cannot repeat tomorrow.

The second way is called the Bayesian interpretation. Under this view, a probability represents your degree of belief, based on the information you currently have. When a weather forecaster says there is a 70 percent chance of rain, they are not saying it rains on 70 percent of identical days. They are saying: given everything I know right now, I believe rain is 70 percent likely.

This is the interpretation we will use most in this project. When we ask a large language model to forecast the temperature tomorrow, we are asking it to express its degree of belief. The more honest and accurate that belief, the better the forecast.

---

## Why Probability Matters for This Project

In this research project, we are evaluating whether large language models can produce useful probability estimates. This is not a simple question.

A model might give a wrong answer and not know it is wrong. Or it might hedge too much and claim everything is uncertain even when it is not. Or it might be overconfident and give a very precise number when the reality is much less predictable.

Probability gives us the vocabulary to describe all of these failures precisely. And in later sessions, you will learn the mathematical tools to measure and score them.

For now, the important thing to understand is this: a good forecaster does not just give you a number. They give you a number with honest uncertainty attached to it.

---

## Check Your Understanding

Before moving to the build file, answer these questions in your head. If you cannot answer one, reread the relevant section above.

1. What does a probability of 0 mean? What does 1 mean?
2. What is the difference between the frequentist and Bayesian interpretations?
3. You say "I am 90 percent sure it will rain tomorrow." Which interpretation are you using?
4. Why is a weather forecast that says "70 percent chance of rain" more useful than one that says "it might rain"?

---

## What to Do Next

Open build/01_probability_basics.py in Claude Code Desktop. Read the comments at the top, then run the file. Ask Claude Code to explain any line you do not understand.

When you have run the build file and understood what it produces, open paper/01_introduction.md and write your draft.

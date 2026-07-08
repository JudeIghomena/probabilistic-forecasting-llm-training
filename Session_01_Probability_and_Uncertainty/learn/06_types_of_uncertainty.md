# Topic 06: Types of Uncertainty

Build file for this topic: build/06_uncertainty_types.py
Paper file for this topic: paper/06_background_uncertainty.md

---

## Start Here

Not all uncertainty is the same. Some uncertainty is permanent, built into the fabric of the world. Some uncertainty is temporary, caused by a lack of information that could in principle be filled in.

This distinction matters because it tells you what to expect from any forecasting model, including an LLM. A model cannot eliminate permanent uncertainty, no matter how good it is. But it should be able to reduce temporary uncertainty if it has access to the right information.

Understanding this distinction will also help you interpret results later in the project when some LLMs appear to be well-calibrated on certain tasks but poorly calibrated on others.

---

## The First Type: Aleatoric Uncertainty

Aleatoric uncertainty is randomness that is genuinely built into the world. Even with perfect information and a perfect model, you cannot predict the exact outcome. The uncertainty is irreducible.

The name comes from the Latin word for dice. A die roll is the classic example. Even if you know the exact weight distribution of the die, the exact force of the throw, and the exact surface it lands on, quantum-level effects make the outcome in principle unpredictable. The randomness is real.

In practice, aleatoric uncertainty appears whenever a system is sensitive to tiny variations that cannot be measured precisely enough. Weather beyond a few days is largely aleatoric. The exact tick-by-tick movement of a stock price is largely aleatoric. The precise time a radioactive atom will decay is entirely aleatoric.

For a forecasting model, aleatoric uncertainty sets a performance ceiling. No model, however sophisticated, should be expected to produce a perfectly narrow distribution around the true outcome for a quantity that is genuinely random. A model that claims too much confidence in this case is overconfident, not good.

---

## The Second Type: Epistemic Uncertainty

Epistemic uncertainty is uncertainty caused by a lack of knowledge or information. In principle, it can be reduced. Get more data, use a better model, or gather more relevant information, and the uncertainty shrinks.

The name comes from the Greek word for knowledge. The classic example is flipping a coin and not knowing whether it is fair. If you have never seen the coin before, you might assign 50/50 odds. But if you flip it a hundred times and it comes up heads 80 times, your uncertainty about its bias has reduced substantially. You now believe it is biased toward heads.

Your original uncertainty was epistemic: caused by not having enough data. Once you had more flips, the uncertainty shrank.

In forecasting, epistemic uncertainty often dominates in situations where data is scarce, the model has not been trained on relevant examples, or the question involves something genuinely novel.

For an LLM forecasting the temperature in a well-studied location with decades of historical data, most of the uncertainty it faces is aleatoric. For an LLM forecasting the economic output of a country that emerged from a civil war last year, much of the uncertainty is epistemic, because the situation is novel and the model has little relevant training data.

---

## Why Both Types Matter for This Project

When we evaluate an LLM's probabilistic forecast, we need to be careful about what kind of uncertainty we are measuring.

A good LLM should produce wide distributions for questions that are genuinely uncertain, whether due to aleatoric noise or epistemic gaps. A good LLM should produce narrow distributions for questions it can answer confidently.

The failure modes are:

Overconfidence: the LLM gives narrow distributions even when the question is genuinely uncertain. It is claiming to know more than it does. This will show up as a calibration failure in the scoring sessions.

Underconfidence: the LLM gives very wide distributions even for questions where it should be able to be precise. It is hedging more than necessary. This is honest but not very useful.

The goal is calibration: the LLM's stated uncertainty should match the actual frequency of outcomes. A distribution that says "90 percent interval is 14 to 24 degrees" should contain the true temperature about 90 percent of the time across many forecasts.

---

## A Key Insight About LLMs

Large language models have a particular kind of epistemic uncertainty that is different from classical models. They were trained on text up to a certain date and have no access to events after that date. They also have no access to real-time data like current sensor readings, financial prices, or today's weather measurements.

This means that when an LLM forecasts the temperature tomorrow, it is not starting from today's atmospheric measurements. It is starting from patterns in training text. Its epistemic uncertainty should therefore be large, reflecting genuine ignorance of current conditions.

Whether LLMs account for this limitation honestly in their probabilistic outputs is one of the questions this project investigates.

---

## Check Your Understanding

1. What is the difference between aleatoric and epistemic uncertainty?
2. You have a coin of unknown fairness. Is your uncertainty about the next flip aleatoric, epistemic, or both?
3. After flipping the coin 1000 times, your uncertainty about its bias has reduced. Which type of uncertainty changed?
4. Why should a model not claim a very narrow distribution when forecasting the weather ten days ahead?
5. What does calibration mean in the context of uncertainty?

---

## What to Do Next

Open build/06_uncertainty_types.py in Claude Code Desktop and run it.

When you are done, open paper/06_background_uncertainty.md and write your draft.

# Topic 07: LLMs as Forecasters

Build file for this topic: build/07_llm_concept.py
Paper file for this topic: paper/07_research_question.md

---

## Start Here

You have now learned the tools: probability, random variables, distributions, the three key distribution families, the difference between point and distributional forecasts, and the two types of uncertainty.

This final topic in Session 01 pulls everything together into the specific research question this project is trying to answer.

What exactly are we asking a large language model to do when we ask it to forecast? And why is it not obvious that it can do this well?

---

## What an LLM Actually Is

A large language model is a system trained on enormous amounts of text. Given some input text, it predicts what the most likely next token is, then the next, then the next, until it has produced a response.

The key word is predicts. An LLM is in some sense always making predictions. But those are predictions about text, trained on patterns in language.

When we ask an LLM to make a weather forecast or a financial forecast, we are asking it to repurpose those language patterns as probabilistic reasoning about the real world. Whether it can do this accurately is not guaranteed. It depends on what patterns are in the training data, how well those patterns reflect the true statistical structure of the world, and whether the model has learned to express its uncertainty honestly.

---

## What We Are Asking an LLM to Do in This Project

In Sessions 03 and 04, you will write code that queries LLMs for probabilistic forecasts. The requests will look something like this:

"The average daily temperature in London in October over the last 30 years has been 13 degrees Celsius with a standard deviation of 3 degrees. Given this, what is your probabilistic forecast for the average temperature this October? Please express your answer as: (1) a 90 percent prediction interval, (2) your best point estimate, and (3) the name of the distribution you believe best describes your uncertainty."

When the LLM answers, it is doing several things at once. It is retrieving relevant patterns from its training data. It is reasoning about what those patterns imply for the distribution of the forecast target. And it is expressing that reasoning as numbers.

Each of those steps can go wrong. The LLM might retrieve the wrong patterns, reason poorly about distributions, or express its uncertainty inaccurately even if its reasoning was correct.

---

## Three Things That Could Go Wrong

The first failure mode is factual error. The LLM might simply have wrong information in its training data, or no relevant information at all. If it has no reliable knowledge about a forecasting target, its distribution will be essentially a guess.

The second failure mode is poor calibration. Even with correct factual knowledge, an LLM might systematically state too much or too little confidence. It might say "95 percent interval" when the true coverage of its intervals is only 70 percent. This kind of calibration failure is what the scoring sessions in this project are designed to detect.

The third failure mode is format errors. The LLM might refuse to give a distribution, give an ambiguous response that cannot be parsed into numbers, or give a distribution that is mathematically invalid (for example, probabilities that do not sum to 1). These practical issues are part of what Session 04 addresses when building the prompt engineering module.

---

## The Three LLMs in This Project

This project benchmarks three large language models:

Claude is developed by Anthropic. It is a commercial, closed-source model designed for safety, accuracy, and nuanced reasoning. It is the model running inside Claude Code Desktop as you work through this curriculum.

GPT-4o is developed by OpenAI. It is another commercial, closed-source model and one of the most widely used LLMs in the world. You will query it through the OpenAI API.

Llama is developed by Meta. It is an open-source model, which means its weights are publicly available. You will query it through the Hugging Face Inference API. Because it is open-source, it can also be run locally on a machine with a GPU.

All three will receive the same forecasting prompts on the same datasets and will be scored by the same metrics. Any differences in their performance reveal genuine differences in their probabilistic reasoning.

---

## What This Project Will Contribute

By the end of this project, you will have:

A benchmarking pipeline that can query any of the three LLMs and score their distributional forecasts systematically and reproducibly.

Quantitative results showing how Claude, GPT-4o, and Llama compare to each other and to classical forecasting baselines on standard benchmark datasets.

A research paper that documents the methodology, results, and interpretation clearly enough that another researcher could reproduce the work.

This is what the next nine sessions build toward, one layer at a time.

---

## Check Your Understanding

1. In your own words, what is a large language model?
2. Why is it not obvious that an LLM can produce a calibrated probabilistic forecast?
3. Name the three failure modes for LLM probabilistic forecasting described in this topic.
4. What makes Llama different from Claude and GPT-4o?
5. What are the three outputs this project will produce?

---

## What to Do Next

Open build/07_llm_concept.py in Claude Code Desktop and run it. This file does not make real API calls yet. It builds a mock of what the querying pipeline will look like, so you can see the structure before the real thing is built in Sessions 03 and 04.

When you are done, open paper/07_research_question.md and write your draft.

After completing Topic 07, you have finished Session 01. Go back to the INTRO.md file and read the final checklist to confirm everything is done before moving to Session 02.

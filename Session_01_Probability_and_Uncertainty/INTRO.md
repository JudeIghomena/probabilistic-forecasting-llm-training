# Session 01: Probability and Uncertainty
# Introduction and Session Overview

Welcome to Session 01. This is where everything begins.

Before you write a single line of code or draft a single sentence of your research paper, you need to understand one big idea: forecasting is not about predicting the future with certainty. It is about honestly describing how uncertain you are.

This session gives you the foundation for that idea. Everything you build in later sessions grows from what you learn here.

---

## What This Session Is About

Most people think of a forecast as a single number. A weather app says 22 degrees. A financial report says earnings will be 3.5 million. A train schedule says the train arrives at 9:15.

But a single number hides something important: how confident is the person making that prediction? Are they nearly certain, or are they just guessing?

In this session, you will learn the mathematical tools that let you express not just what you expect to happen, but how sure you are about it. These tools are called probability distributions, and they are the language of honest forecasting.

You will also start to think about a question that runs through this entire project: can a large language model, a system trained on text, produce honest and accurate probability distributions? That question is what this research is trying to answer.

---

## What You Will Know by the End

By the time you complete all seven topics in this session, you will be able to:

- Explain what probability is and what it measures
- Describe a random variable in plain language and with proper notation
- Read a probability distribution and explain what its shape tells you
- Identify and compare the three key distributions used in this project
- Explain clearly why a single number forecast is less useful than a full distribution
- Distinguish between two types of uncertainty and explain why both matter
- Describe what it means to ask an LLM to make a probabilistic forecast

---

## What You Will Have Built by the End

Your build folder will contain seven Python files. Each one is a working piece of code that demonstrates one of the seven topics. Together they form the very first layer of the benchmarking pipeline you will build across all ten sessions.

Every file you write today will be reused and extended in later sessions. You are not writing throwaway examples. You are writing the foundation of a real research tool.

---

## What You Will Have Written by the End

Your paper folder will contain seven files, each one a draft of a section of your research paper. You will not write perfect prose today. You will write first drafts that you will refine in later sessions. The goal is to get your ideas down in your own words while the concepts are fresh.

By the end of this session, the introduction, problem statement, background, and research question sections of your paper will have working drafts.

---

## How to Work Through This Session

Work through the topics in order. Each one builds on the previous.

For each topic, follow this sequence:

Step 1. Read the learn file in full before opening any code.

Step 2. Open the linked build file in Claude Code Desktop and work through it. Ask Claude Code to explain anything you do not understand.

Step 3. Open the linked paper file and write your draft section. Use the prompts in the paper file to guide you. Write in your own words.

Do not move to the next topic until you have completed all three steps for the current one.

---

## What You Need Before Starting

Make sure you have completed all nine foundation guides. You should have:

- Python installed with all required libraries
- VS Code open with this project folder loaded
- Claude Code Desktop installed and connected to this project folder
- Git configured and this repository cloned
- Jupyter installed and working
- Your Anthropic API key stored as an environment variable

If any of these are missing, go back to the foundation folder and complete that guide before continuing.

---

## How Long This Session Takes

Expect to spend two to three hours on this session if you are working carefully and writing your paper sections as you go. Do not rush the paper sections. They are as important as the code.

---

## The Seven Topics

| Topic | File | What You Learn |
|---|---|---|
| 1 | learn/01_what_is_probability.md | What probability is and how to read it |
| 2 | learn/02_random_variables.md | What a random variable is |
| 3 | learn/03_probability_distributions.md | What a distribution is and how to read its shape |
| 4 | learn/04_key_distributions.md | The three distributions you will use all project |
| 5 | learn/05_point_vs_predictive.md | Why one number is never enough |
| 6 | learn/06_types_of_uncertainty.md | Two kinds of uncertainty and why both matter |
| 7 | learn/07_llms_as_forecasters.md | What we are asking an LLM to do |

Start with Topic 1. Open learn/01_what_is_probability.md now.

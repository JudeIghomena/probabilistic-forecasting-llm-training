# Paper Section: Research Question and Scope
# Connected to: learn/07_llms_as_forecasters.md and build/07_llm_concept.py

---

## Your Task

Write the research question section of your paper. This is the section that tells the reader exactly what question this project is answering and why it is worth asking. A good research question is specific, testable, and important.

---

## Paragraph 1: From Motivation to Question

Take everything you wrote in the motivation section (paper/05_motivation.md) and sharpen it into a precise research question. The reader should finish this paragraph knowing exactly what is being tested.

Sentence starter: "This paper asks a specific and testable question: can large language models produce probabilistic forecasts that are well-calibrated, as measured by proper scoring rules applied to held-out observations?"

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 2: Why This Question Has Not Been Answered

Explain the gap in existing research. LLMs are increasingly used in advisory and decision-support roles, but their distributional forecasting ability has not been rigorously benchmarked against classical methods. Point out what is missing.

Sentence starter: "Despite the rapid adoption of LLMs in analytical and advisory roles, their ability to produce calibrated probabilistic distributions rather than point predictions remains largely untested against quantitative baselines."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 3: The Three Hypotheses

State three specific hypotheses that the benchmarking pipeline will test. A hypothesis is a clear prediction that can be confirmed or refuted by data. Your hypotheses should follow this pattern: state what you predict and what evidence would change your mind.

Sentence starter: "This project tests three specific hypotheses."

Example hypotheses to adapt (rewrite them in your own voice):

H1. LLMs will produce wider-than-necessary distributions on benchmark forecasting tasks, reflecting epistemic uncertainty that is greater than the irreducible aleatoric floor.

H2. Commercial closed-source models (Claude, GPT-4o) will be better calibrated than the open-source Llama model on standard benchmark tasks, because their RLHF training may have improved uncertainty expression.

H3. All three LLMs will underperform classical statistical baselines (ARIMA, quantile regression) on the CRPS metric, because classical models are trained directly on the statistical structure of the data.

Write your adapted paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 4: Scope and Limitations

Every good research question comes with a clear statement of what is and is not being tested. This protects the reader from expecting too much and helps future researchers know where to extend the work.

Sentence starter: "The scope of this study is deliberately narrow."

Points to include (rewrite in your own words):

- The study uses benchmark datasets where ground truth is known, not real-time forecasting scenarios.
- It tests the three distributions described in Topic 04 (Gaussian, Laplace, Uniform).
- It does not fine-tune any of the models or modify their prompts beyond the standard format.
- It does not test all possible LLMs, only the three selected for their diversity of provenance.

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Figure to Reference

Run build/07_llm_concept.py before completing this section.

There is no output image from this build file. Instead, reference the console output directly in your text if useful. You may describe the structure of the prompt shown in Section 1 of the build file, or the calibration simulation result from Section 3.

---

## Self-Check Before Moving On

- Have you stated a research question that a reader could describe in one sentence?
- Have you stated at least two hypotheses that could be confirmed or refuted by data?
- Have you acknowledged at least two limitations of the study scope?
- Have you connected this section back to the motivation and background sections written earlier in this session?

When you are satisfied, you have completed Session 01.

Go back to INTRO.md and work through the Session 01 completion checklist.

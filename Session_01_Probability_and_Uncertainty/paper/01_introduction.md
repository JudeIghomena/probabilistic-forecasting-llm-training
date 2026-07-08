# Paper Section: Introduction
# Connected to: learn/01_what_is_probability.md and build/01_probability_basics.py

---

## Your Task

Write the opening of your research paper. This section introduces the reader to the problem and makes the case for why the project matters.

A strong introduction does four things in order:

1. Opens with a real situation that shows the cost of uncertainty
2. Explains what probabilistic forecasting is and why it is better than point predictions
3. Introduces LLMs and the gap in the research
4. Ends with a clear statement of what this paper does

Write each paragraph below. Sentence starters are provided to help you begin. Replace or extend them in your own words.

---

## Paragraph 1: A Real Situation

Start with a concrete scenario that makes the cost of uncertainty visible to the reader. This could be a hospital managing medical supplies, an electricity grid balancing power demand, or a financial institution managing risk. Choose one and describe what goes wrong when the forecast is just a number with no uncertainty attached.

Sentence starter: "When a hospital needs to decide how many units of emergency blood supply to stock for the coming week, a single predicted number is not enough."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 2: What Probabilistic Forecasting Is

Explain the difference between a point prediction and a probabilistic forecast in plain language. Tell the reader why the second is more useful. Reference the visualisation you produced in the build file.

Sentence starter: "A point prediction gives one number. A probabilistic forecast gives a full picture of what might happen and how likely each outcome is."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 3: The Research Gap

Explain that LLMs have shown impressive abilities across many tasks, but their ability to produce honest, calibrated probability estimates has not been rigorously studied. This is the gap your project fills.

Sentence starter: "Large language models have demonstrated strong performance on tasks involving text generation, reasoning, and knowledge retrieval. However, their ability to generate reliable probabilistic forecasts has received little systematic evaluation."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Paragraph 4: What This Paper Does

End the introduction with a clear, specific statement of what this research project sets out to do. Be direct. One or two sentences.

Sentence starter: "This paper presents a systematic evaluation pipeline that benchmarks the probabilistic forecasting ability of three large language models against established classical forecasting methods."

Write your paragraph here:

[YOUR PARAGRAPH]

---

## Figure to Reference

After running build/01_probability_basics.py, a file called 01_probability_basics.png is saved in your build folder.

Reference it in your paper with this caption:

Figure 1. The left panel shows the uniform probability distribution over outcomes of a fair six-sided die, illustrating the fundamental property that all probabilities sum to 1. The right panel shows how the frequentist estimate of the probability of heads converges to the true value of 0.5 as the number of coin flips increases, demonstrating the law of large numbers.

---

## Self-Check Before Moving On

Read back what you wrote and ask yourself:

- Does the opening paragraph make a real person in a real situation care about this problem?
- Have you used the words "probabilistic forecast" and "point prediction" correctly?
- Is your research gap paragraph honest about what has and has not been studied?
- Is your final statement specific enough that a reader knows exactly what to expect?

If you answered yes to all four, you are ready to move to Topic 02.

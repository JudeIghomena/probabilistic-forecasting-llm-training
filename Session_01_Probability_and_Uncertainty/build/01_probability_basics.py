"""
Build File 01: Probability Basics
Session 01, Topic 01: What Is Probability?

Connected learn file: learn/01_what_is_probability.md
Connected paper file: paper/01_introduction.md

What this file does:
    This file gives you hands-on experience with probability as a number.
    You will see how probabilities are calculated, how they behave, and
    why expressing uncertainty as a number is more powerful than using words.

How to use this file:
    Open it in Claude Code Desktop. Run it section by section.
    After each section, read the printed output carefully.
    Ask Claude Code to explain anything that is not clear.

Pipeline contribution:
    The functions written here are the first building blocks of the pipeline.
    They will be imported and reused in later sessions.
"""

import numpy as np
import matplotlib.pyplot as plt


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1: Probability as a Number
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 1: Probability as a Number")
print("=" * 60)

# A probability is just a number between 0 and 1.
# Let us define some simple probabilities and print them.

prob_coin_heads    = 0.5     # fair coin, heads
prob_die_six       = 1 / 6   # standard six-sided die, rolling a six
prob_sun_rises     = 0.9999  # the sun rising tomorrow
prob_snow_july     = 0.001   # snow in London in July

print(f"Probability of heads on a fair coin:     {prob_coin_heads:.4f}")
print(f"Probability of rolling a six:            {prob_die_six:.4f}")
print(f"Probability the sun rises tomorrow:      {prob_sun_rises:.4f}")
print(f"Probability of snow in London in July:   {prob_snow_july:.4f}")

print()
print("Notice: all of these are between 0 and 1.")
print("A probability outside this range is always a mistake.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2: The Law of Total Probability
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 2: Probabilities of All Outcomes Must Sum to 1")
print("=" * 60)

# If you list every possible outcome, their probabilities must add up to 1.
# This is called the law of total probability.

# For a six-sided die, there are six outcomes.
outcomes = [1, 2, 3, 4, 5, 6]
probabilities = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

print("Six-sided die outcomes and their probabilities:")
for outcome, prob in zip(outcomes, probabilities):
    print(f"  Rolling a {outcome}: {prob:.4f}")

print(f"\nTotal: {sum(probabilities):.4f}")
print("The probabilities sum to 1.0, as they always must.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3: The Frequentist View in Action
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 3: The Frequentist View")
print("=" * 60)

# The frequentist view says: probability is the long-run fraction of times
# an outcome occurs when you repeat an experiment many times.

# Let us simulate coin flips and see if the fraction approaches 0.5.

np.random.seed(42)

for n_flips in [10, 100, 1000, 10000, 100000]:
    flips = np.random.randint(0, 2, size=n_flips)  # 0 = tails, 1 = heads
    fraction_heads = flips.mean()
    print(f"  {n_flips:>7} flips: heads {fraction_heads:.4f} (true probability: 0.5000)")

print()
print("As the number of flips grows, the fraction gets closer to 0.5.")
print("This is what the frequentist view predicts.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4: The Bayesian View in Action
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 4: The Bayesian View")
print("=" * 60)

# The Bayesian view says: probability represents your current degree of belief,
# which you update as new evidence arrives.

# Imagine you are trying to guess whether a coin is fair.
# You start with no knowledge (prior belief: 50/50).
# Each flip updates your belief.

print("Bayesian coin example:")
print("You suspect a coin might be biased toward heads.")
print("You start with the belief that P(heads) = 0.5.")
print()

# We simulate a biased coin (true P(heads) = 0.7) and update belief after each flip
true_prob = 0.7
np.random.seed(0)

# Start with equal prior (alpha=1, beta=1 in a Beta distribution)
alpha = 1  # number of heads observed + prior
beta  = 1  # number of tails observed + prior

print(f"{'Flip':>6}  {'Outcome':>8}  {'Estimated P(heads)':>20}")
print("-" * 40)

for i in range(1, 11):
    flip = 1 if np.random.random() < true_prob else 0
    alpha += flip
    beta  += (1 - flip)
    estimated_prob = alpha / (alpha + beta)
    outcome_label = "Heads" if flip == 1 else "Tails"
    print(f"{i:>6}  {outcome_label:>8}  {estimated_prob:>20.4f}")

print()
print(f"After 10 flips, estimated P(heads) = {alpha / (alpha + beta):.4f}")
print(f"True P(heads) = {true_prob:.4f}")
print("With more flips, the estimate would get even closer.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5: Visualising Probabilities
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 5: Visualising Probability")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
fig.suptitle("Session 01, Topic 01: Probability Basics", fontsize=13)

# Left plot: Die roll probabilities as a bar chart
ax1 = axes[0]
ax1.bar(outcomes, probabilities, color="steelblue", edgecolor="white", linewidth=1.5)
ax1.set_title("Probability of Each Die Outcome")
ax1.set_xlabel("Outcome")
ax1.set_ylabel("Probability")
ax1.set_xticks(outcomes)
ax1.set_ylim(0, 0.3)
ax1.axhline(y=1/6, color="red", linestyle="--", linewidth=1, label="True P = 1/6")
ax1.legend()
ax1.grid(axis="y", alpha=0.3)

# Right plot: Convergence of coin flip frequency to true probability
flip_counts = [10, 50, 100, 500, 1000, 5000, 10000]
estimated_probs = []

np.random.seed(42)
for n in flip_counts:
    flips = np.random.randint(0, 2, size=n)
    estimated_probs.append(flips.mean())

ax2 = axes[1]
ax2.plot(flip_counts, estimated_probs, marker="o", color="steelblue", linewidth=2, label="Estimated P(heads)")
ax2.axhline(y=0.5, color="red", linestyle="--", linewidth=1.5, label="True P = 0.5")
ax2.set_title("Frequentist View: Convergence to True Probability")
ax2.set_xlabel("Number of Coin Flips")
ax2.set_ylabel("Estimated P(heads)")
ax2.set_xscale("log")
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("01_probability_basics.png", dpi=150, bbox_inches="tight")
plt.show()

print("Plot saved as 01_probability_basics.png")
print("Use this image in your paper/01_introduction.md file.")
print()
print("You have completed Topic 01.")
print("Next: open learn/02_random_variables.md")

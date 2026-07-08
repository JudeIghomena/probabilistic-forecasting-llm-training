"""
Build File 02: Random Variables
Session 01, Topic 02: What Is a Random Variable?

Connected learn file: learn/02_random_variables.md
Connected paper file: paper/02_problem_statement.md

What this file does:
    Shows you the difference between discrete and continuous random variables.
    Demonstrates expected value and variance with real calculations.
    Produces visualisations that connect the maths to intuition.

How to use this file:
    Run it section by section in Claude Code Desktop.
    Pay attention to the printed output. Each number connects to
    something explained in the learn file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1: A Discrete Random Variable
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 1: Discrete Random Variable (Die Roll)")
print("=" * 60)

# X = outcome of a six-sided die roll
# Possible values: 1, 2, 3, 4, 5, 6
# Each equally likely with probability 1/6

outcomes = np.array([1, 2, 3, 4, 5, 6])
probs    = np.array([1/6] * 6)

# Expected value: the average outcome over many rolls
expected_value = np.sum(outcomes * probs)
print(f"Random variable X: outcome of a fair die roll")
print(f"Possible values: {outcomes.tolist()}")
print(f"Expected value E[X]: {expected_value:.4f}")

# Variance: how spread out the outcomes are around the expected value
variance = np.sum(probs * (outcomes - expected_value) ** 2)
std_dev  = np.sqrt(variance)
print(f"Variance Var(X): {variance:.4f}")
print(f"Standard deviation: {std_dev:.4f}")
print()

# Simulate 10,000 rolls and verify the expected value holds
np.random.seed(42)
simulated_rolls = np.random.choice(outcomes, size=10000, p=probs)
print(f"Simulated mean after 10,000 rolls: {simulated_rolls.mean():.4f}")
print(f"True expected value:                {expected_value:.4f}")
print("These are very close, as the law of large numbers predicts.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2: A Continuous Random Variable
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 2: Continuous Random Variable (Temperature)")
print("=" * 60)

# Y = maximum temperature in London tomorrow (in degrees Celsius)
# We model this as a Gaussian distribution with mean 18 and std 5
# (A rough model for a typical day in London)

mean_temp = 18.0
std_temp  = 5.0

# For continuous variables, we cannot ask P(Y = exactly 20.0)
# But we CAN ask P(18 < Y < 22), meaning: what is the chance the temperature
# falls between 18 and 22 degrees?

lower = 18
upper = 22
prob_in_range = stats.norm.cdf(upper, loc=mean_temp, scale=std_temp) - \
                stats.norm.cdf(lower, loc=mean_temp, scale=std_temp)

print(f"Random variable Y: tomorrow's max temperature in London")
print(f"Model: Gaussian with mean = {mean_temp}, std = {std_temp}")
print(f"P({lower} < Y < {upper}) = {prob_in_range:.4f}")
print(f"There is a {prob_in_range * 100:.1f}% chance the temperature falls between {lower} and {upper} degrees.")
print()

# Probability of extremely high temperature (above 30 degrees)
prob_above_30 = 1 - stats.norm.cdf(30, loc=mean_temp, scale=std_temp)
print(f"P(Y > 30) = {prob_above_30:.4f}")
print(f"There is only a {prob_above_30 * 100:.2f}% chance of the temperature exceeding 30 degrees.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3: Sampling from a Random Variable
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 3: Drawing Samples from a Random Variable")
print("=" * 60)

# Sampling means asking: if I ran this uncertain situation many times,
# what values would I observe? Each draw is one possible outcome.

np.random.seed(7)
temperature_samples = np.random.normal(loc=mean_temp, scale=std_temp, size=20)

print("20 possible temperature values drawn from our model:")
for i, temp in enumerate(temperature_samples, 1):
    print(f"  Day {i:>2}: {temp:.1f} degrees C")

print()
print(f"Mean of these 20 samples: {temperature_samples.mean():.2f}")
print(f"True mean of the distribution: {mean_temp}")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4: Visualisation
# ─────────────────────────────────────────────────────────────────────────────

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle("Session 01, Topic 02: Random Variables", fontsize=13)

# Plot 1: Discrete random variable
ax1 = axes[0]
ax1.bar(outcomes, probs, color="steelblue", edgecolor="white", linewidth=1.5)
ax1.axvline(x=expected_value, color="red", linewidth=2, linestyle="--",
            label=f"E[X] = {expected_value:.1f}")
ax1.set_title("Discrete: Die Roll Probabilities")
ax1.set_xlabel("Outcome (X)")
ax1.set_ylabel("Probability P(X = x)")
ax1.set_xticks(outcomes)
ax1.legend()
ax1.grid(axis="y", alpha=0.3)

# Plot 2: Continuous random variable
x_range = np.linspace(-5, 40, 500)
y_density = stats.norm.pdf(x_range, loc=mean_temp, scale=std_temp)

ax2 = axes[1]
ax2.plot(x_range, y_density, color="steelblue", linewidth=2.5)
ax2.axvline(x=mean_temp, color="red", linewidth=2, linestyle="--",
            label=f"E[Y] = {mean_temp}")
x_fill = np.linspace(lower, upper, 300)
y_fill = stats.norm.pdf(x_fill, loc=mean_temp, scale=std_temp)
ax2.fill_between(x_fill, y_fill, alpha=0.3, color="orange",
                 label=f"P({lower} < Y < {upper}) = {prob_in_range:.2f}")
ax2.set_title("Continuous: Temperature Distribution")
ax2.set_xlabel("Temperature (degrees C)")
ax2.set_ylabel("Probability Density")
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)

# Plot 3: Samples from the continuous distribution
ax3 = axes[2]
ax3.hist(temperature_samples, bins=8, color="steelblue", edgecolor="white",
         linewidth=1.5, density=False)
ax3.axvline(x=temperature_samples.mean(), color="red", linewidth=2,
            linestyle="--", label=f"Sample mean = {temperature_samples.mean():.1f}")
ax3.set_title("20 Samples from the Temperature Model")
ax3.set_xlabel("Temperature (degrees C)")
ax3.set_ylabel("Count")
ax3.legend()
ax3.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("02_random_variables.png", dpi=150, bbox_inches="tight")
plt.show()

print("Plot saved as 02_random_variables.png")
print("Use this image in your paper/02_problem_statement.md file.")
print()
print("You have completed Topic 02.")
print("Next: open learn/03_probability_distributions.md")

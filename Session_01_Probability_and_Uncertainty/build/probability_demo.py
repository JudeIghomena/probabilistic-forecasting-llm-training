"""
Session 01 Build, Probability and Uncertainty
===============================================
Run this file using Claude Code or directly with: python probability_demo.py

What this file does:
- Creates and visualises the three core distributions from the learn document
- Shows the difference between a point prediction and a predictive distribution
- Gives you your first hands-on experience with numpy and matplotlib

Instructions for Claude Code:
  Open this file in Claude Code. Run each section one at a time.
  Ask Claude Code to explain any line you do not understand.
  When you are done, copy the plots into your paper/paper_contribution.md
  as described in the caption comments below.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1: Set up the plotting environment
# ─────────────────────────────────────────────────────────────────────────────

# We will produce one figure with four panels (subplots)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Session 01, Probability Distributions and Uncertainty", fontsize=14)


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2: The Gaussian (Normal) Distribution
# ─────────────────────────────────────────────────────────────────────────────

# x is a range of values we will evaluate the distribution at
x = np.linspace(-10, 40, 500)

# Three Gaussians with the same mean but different standard deviations
# This shows how sigma controls confidence: small sigma = confident, large = uncertain
gaussian_narrow  = stats.norm.pdf(x, loc=20, scale=2)   # mean=20, std=2
gaussian_medium  = stats.norm.pdf(x, loc=20, scale=5)   # mean=20, std=5
gaussian_wide    = stats.norm.pdf(x, loc=20, scale=10)  # mean=20, std=10

ax1 = axes[0, 0]
ax1.plot(x, gaussian_narrow, label="std = 2 (confident)",  color="blue",  linewidth=2)
ax1.plot(x, gaussian_medium, label="std = 5 (uncertain)",  color="orange", linewidth=2)
ax1.plot(x, gaussian_wide,   label="std = 10 (very uncertain)", color="red", linewidth=2)
ax1.set_title("Gaussian Distribution (mean = 20)")
ax1.set_xlabel("Temperature (degrees C)")
ax1.set_ylabel("Probability Density")
ax1.legend()
ax1.grid(alpha=0.3)

# PAPER CAPTION: Use this plot in Section 1 (Introduction) to illustrate
# how the same point prediction (20 degrees) can represent very different
# levels of forecaster confidence depending on the spread.


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3: The Laplace Distribution
# ─────────────────────────────────────────────────────────────────────────────

# Comparing Gaussian and Laplace with the same mean and similar spread
# The key difference is in the tails: Laplace has heavier tails
laplace_pdf  = stats.laplace.pdf(x, loc=20, scale=4)
gaussian_pdf = stats.norm.pdf(x, loc=20, scale=5)

ax2 = axes[0, 1]
ax2.plot(x, gaussian_pdf, label="Gaussian (std=5)",   color="blue",  linewidth=2)
ax2.plot(x, laplace_pdf,  label="Laplace (scale=4)",  color="green", linewidth=2)
ax2.set_title("Gaussian vs Laplace, Heavy Tails")
ax2.set_xlabel("Value")
ax2.set_ylabel("Probability Density")
ax2.legend()
ax2.grid(alpha=0.3)

# PAPER CAPTION: Use this plot to explain why Gaussian is not always the right
# choice. In financial or extreme-weather forecasting, the Laplace distribution
# captures rare events more honestly.


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4: The Uniform Distribution
# ─────────────────────────────────────────────────────────────────────────────

# Uniform means: we have no idea. Every value in the range is equally likely.
uniform_pdf = stats.uniform.pdf(x, loc=10, scale=20)  # from 10 to 30

ax3 = axes[1, 0]
ax3.plot(x, uniform_pdf,  label="Uniform (10 to 30)", color="purple", linewidth=2)
ax3.plot(x, gaussian_narrow, label="Gaussian (confident)",  color="blue",  linewidth=2, linestyle="--")
ax3.set_title("Uniform vs Gaussian, Maximum vs Minimum Uncertainty")
ax3.set_xlabel("Value")
ax3.set_ylabel("Probability Density")
ax3.legend()
ax3.grid(alpha=0.3)

# PAPER CAPTION: A uniform distribution is the baseline of no information.
# If an LLM returns forecasts that look uniform, it is essentially saying
# it cannot make a meaningful prediction for this task.


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5: Point Prediction vs Predictive Distribution
# ─────────────────────────────────────────────────────────────────────────────

# This is the most important plot in Session 01.
# It shows the core argument of the entire project visually.

ax4 = axes[1, 1]

# The predictive distribution: what a good probabilistic forecaster gives
ax4.plot(x, gaussian_medium, color="blue", linewidth=2, label="Predictive distribution")
ax4.fill_between(x, gaussian_medium, alpha=0.2, color="blue", label="90% prediction interval")

# The point prediction: just a single vertical line at the mean
ax4.axvline(x=20, color="red", linewidth=2, linestyle="--", label="Point prediction (20 degrees)")

# Shade the 90% prediction interval (5th to 95th percentile)
lower = stats.norm.ppf(0.05, loc=20, scale=5)
upper = stats.norm.ppf(0.95, loc=20, scale=5)
x_interval = np.linspace(lower, upper, 300)
y_interval = stats.norm.pdf(x_interval, loc=20, scale=5)
ax4.fill_between(x_interval, y_interval, alpha=0.4, color="blue")

ax4.set_title("Point Prediction vs Predictive Distribution")
ax4.set_xlabel("Temperature (degrees C)")
ax4.set_ylabel("Probability Density")
ax4.legend()
ax4.grid(alpha=0.3)

# PAPER CAPTION: This figure captures the core motivation of this project.
# The red line (point prediction) provides one number but no uncertainty.
# The blue curve (predictive distribution) provides the full picture:
# the most likely outcome AND how confident the forecaster is.


# ─────────────────────────────────────────────────────────────────────────────
# SAVE AND SHOW
# ─────────────────────────────────────────────────────────────────────────────

plt.tight_layout()
plt.savefig("session_01_distributions.png", dpi=150, bbox_inches="tight")
plt.show()

print("Plot saved as session_01_distributions.png")
print("Use this image in your paper_contribution.md for Session 01.")


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 6: Quick Exercises
# ─────────────────────────────────────────────────────────────────────────────

def exercise_1_sampling():
    """
    Exercise: Sample from a Gaussian and see how the samples cluster.
    Ask Claude Code to run this function and explain what you observe.
    """
    np.random.seed(42)
    samples = np.random.normal(loc=20, scale=5, size=1000)

    print("=== Exercise 1: Sampling from a Gaussian ===")
    print(f"Mean of samples:              {samples.mean():.2f}  (expected: 20)")
    print(f"Std deviation of samples:     {samples.std():.2f}   (expected: 5)")
    print(f"Fraction between 15 and 25:   {((samples > 15) & (samples < 25)).mean():.2%}")
    print(f"Fraction below 10:            {(samples < 10).mean():.2%}")
    print()


def exercise_2_compare_tails():
    """
    Exercise: Compare how often extreme values appear in Gaussian vs Laplace.
    This demonstrates the heavy-tail property of the Laplace distribution.
    """
    np.random.seed(42)
    gaussian_samples = np.random.normal(loc=0, scale=5, size=10000)
    laplace_samples  = np.random.laplace(loc=0, scale=4, size=10000)

    threshold = 15  # "extreme" is defined as more than 15 units from the mean

    print("=== Exercise 2: Tail Behaviour ===")
    print(f"Gaussian extremes beyond {threshold}:  {(np.abs(gaussian_samples) > threshold).mean():.2%}")
    print(f"Laplace extremes beyond {threshold}:   {(np.abs(laplace_samples) > threshold).mean():.2%}")
    print("Laplace produces more extreme values, this is what 'heavy tails' means.")
    print()


# Run the exercises
exercise_1_sampling()
exercise_2_compare_tails()

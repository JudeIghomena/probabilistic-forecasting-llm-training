"""
Build File 05: Point Predictions vs Predictive Distributions
Session 01, Topic 05

Connected learn file: learn/05_point_vs_predictive.md
Connected paper file: paper/05_motivation.md

What this file does:
    Demonstrates the information gap between a point prediction and a
    predictive distribution using a concrete forecasting scenario.
    Shows all three formats for expressing a predictive distribution:
    quantiles, parametric, and samples.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1: Two Models, Same Point Prediction, Different Confidence
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 1: Two Models, Same Point Prediction")
print("=" * 60)

# Both models predict 19 degrees. But their distributions are very different.

point_prediction = 19.0

model_a = stats.norm(loc=point_prediction, scale=2)   # confident
model_b = stats.norm(loc=point_prediction, scale=8)   # uncertain

print(f"Point prediction (both models): {point_prediction} degrees")
print()
print("Model A (confident, std = 2):")
print(f"  90% interval: ({model_a.ppf(0.05):.1f}, {model_a.ppf(0.95):.1f}) degrees")
print(f"  P(temperature above 25) = {1 - model_a.cdf(25):.4f}")
print(f"  P(temperature below 14) = {model_a.cdf(14):.4f}")
print()
print("Model B (uncertain, std = 8):")
print(f"  90% interval: ({model_b.ppf(0.05):.1f}, {model_b.ppf(0.95):.1f}) degrees")
print(f"  P(temperature above 25) = {1 - model_b.cdf(25):.4f}")
print(f"  P(temperature below 14) = {model_b.cdf(14):.4f}")
print()
print("Same point prediction. Very different pictures of uncertainty.")
print("The point prediction alone cannot tell you which model to trust.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2: Three Formats for Expressing a Predictive Distribution
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 2: Three Formats for a Predictive Distribution")
print("=" * 60)

# Format 1: Quantiles
print("Format 1: Quantile Forecast")
quantile_levels = [0.10, 0.25, 0.50, 0.75, 0.90]
quantile_values = model_a.ppf(quantile_levels)
for level, value in zip(quantile_levels, quantile_values):
    print(f"  {int(level * 100)}th percentile: {value:.2f} degrees")
print()

# Format 2: Parametric
print("Format 2: Parametric Forecast")
print(f"  Distribution family: Gaussian")
print(f"  Mean (mu):            {model_a.mean():.2f}")
print(f"  Std deviation (sigma):{model_a.std():.2f}")
print()

# Format 3: Samples
print("Format 3: Sample Forecast (20 draws)")
np.random.seed(42)
samples = model_a.rvs(size=20)
print("  Samples:", [f"{s:.1f}" for s in samples])
print(f"  Sample mean: {samples.mean():.2f}")
print(f"  Sample std:  {samples.std():.2f}")
print()
print("All three formats describe the same underlying distribution.")
print("In Sessions 04 and 09, LLMs will be asked to produce all three.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3: The Decision Problem
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 3: How the Distribution Changes the Decision")
print("=" * 60)

# Scenario: a farmer needs to decide whether to harvest this week.
# Harvesting is risky if temperature drops below 14 (frost risk).
# A point prediction of 19 does not tell you the frost risk.

frost_threshold = 14.0

frost_risk_a = model_a.cdf(frost_threshold)
frost_risk_b = model_b.cdf(frost_threshold)

print("Scenario: a farmer is deciding whether to harvest.")
print(f"Frost threshold: below {frost_threshold} degrees causes crop damage.")
print()
print(f"Point prediction from both models: {point_prediction} degrees")
print(f"Based on the point prediction alone: no frost risk visible.")
print()
print(f"Model A frost risk: {frost_risk_a:.4f} ({frost_risk_a*100:.2f}% chance of frost)")
print(f"Model B frost risk: {frost_risk_b:.4f} ({frost_risk_b*100:.2f}% chance of frost)")
print()
print("With Model A: the farmer harvests confidently.")
print("With Model B: the 16% frost risk might change the decision entirely.")
print("The predictive distribution reveals what the point prediction hides.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4: Visualisation
# ─────────────────────────────────────────────────────────────────────────────

x = np.linspace(-15, 55, 1000)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle("Session 01, Topic 05: Point Prediction vs Predictive Distribution", fontsize=13)

# Plot 1: Two models, same point prediction
ax1 = axes[0]
ax1.plot(x, model_a.pdf(x), color="steelblue", linewidth=2.5, label="Model A (confident)")
ax1.plot(x, model_b.pdf(x), color="darkorange", linewidth=2.5, label="Model B (uncertain)")
ax1.axvline(x=point_prediction, color="black", linewidth=2, linestyle="--",
            label=f"Point prediction: {point_prediction}")
ax1.set_title("Same Point Prediction, Different Uncertainty")
ax1.set_xlabel("Temperature (degrees C)")
ax1.set_ylabel("Probability Density")
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)

# Plot 2: Quantile format visualised
ax2 = axes[1]
ax2.plot(x, model_a.pdf(x), color="steelblue", linewidth=2.5)
colours = ["#d62728", "#ff7f0e", "#2ca02c", "#ff7f0e", "#d62728"]
labels  = ["10th", "25th", "50th", "75th", "90th"]
for level, colour, label in zip(quantile_levels, colours, labels):
    q_val = model_a.ppf(level)
    ax2.axvline(x=q_val, color=colour, linewidth=1.5, linestyle=":",
                label=f"{label}: {q_val:.1f}")
ax2.set_title("Quantile Format: Key Percentiles")
ax2.set_xlabel("Temperature (degrees C)")
ax2.set_ylabel("Probability Density")
ax2.legend(fontsize=7)
ax2.grid(alpha=0.3)

# Plot 3: Frost risk visualised
ax3 = axes[2]
ax3.plot(x, model_a.pdf(x), color="steelblue", linewidth=2.5, label="Model A")
ax3.plot(x, model_b.pdf(x), color="darkorange", linewidth=2.5, label="Model B")
x_frost = np.linspace(-15, frost_threshold, 300)
ax3.fill_between(x_frost, model_a.pdf(x_frost), alpha=0.3, color="steelblue",
                 label=f"Model A frost risk: {frost_risk_a*100:.1f}%")
ax3.fill_between(x_frost, model_b.pdf(x_frost), alpha=0.3, color="darkorange",
                 label=f"Model B frost risk: {frost_risk_b*100:.1f}%")
ax3.axvline(x=frost_threshold, color="red", linewidth=2, linestyle="--",
            label=f"Frost threshold: {frost_threshold}")
ax3.set_title("Frost Risk: What the Point Prediction Hides")
ax3.set_xlabel("Temperature (degrees C)")
ax3.set_ylabel("Probability Density")
ax3.legend(fontsize=7)
ax3.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("05_point_vs_predictive.png", dpi=150, bbox_inches="tight")
plt.show()

print("Plot saved as 05_point_vs_predictive.png")
print("Use this image in your paper/05_motivation.md file.")
print()
print("You have completed Topic 05.")
print("Next: open learn/06_types_of_uncertainty.md")

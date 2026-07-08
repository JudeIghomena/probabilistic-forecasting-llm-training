"""
Build File 06: Types of Uncertainty
Session 01, Topic 06: Aleatoric vs Epistemic Uncertainty

Connected learn file: learn/06_types_of_uncertainty.md
Connected paper file: paper/06_background_uncertainty.md

What this file does:
    Demonstrates aleatoric and epistemic uncertainty with simulations.
    Shows how epistemic uncertainty shrinks as data increases.
    Shows that aleatoric uncertainty has a permanent floor.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1: Aleatoric Uncertainty Has a Floor
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 1: Aleatoric Uncertainty Does Not Shrink")
print("=" * 60)

# Temperature has genuine randomness (aleatoric component).
# Even with a perfect model, the forecast distribution stays wide.
# We demonstrate this by showing that repeated forecasts do not converge to a point.

np.random.seed(42)
true_mean = 18.0
true_std  = 4.0   # this is the irreducible aleatoric spread

print("Scenario: forecasting daily temperature with a perfect model.")
print(f"True distribution: Gaussian(mean={true_mean}, std={true_std})")
print()
print("No matter how much data we gather, the FORECAST distribution stays at std = 4.")
print("The model is perfect. The uncertainty is real. This is aleatoric.")
print()

observed_outcomes = np.random.normal(true_mean, true_std, size=1000)
print(f"After observing 1,000 days: mean of outcomes = {observed_outcomes.mean():.2f}")
print(f"After observing 1,000 days: std of outcomes  = {observed_outcomes.std():.2f}")
print("The spread of outcomes stays constant. The aleatoric floor is always there.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2: Epistemic Uncertainty Shrinks With Data
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 2: Epistemic Uncertainty Shrinks with More Data")
print("=" * 60)

# We do not know whether a coin is fair (epistemic uncertainty).
# As we flip it more times, our belief about its bias narrows.

true_p_heads = 0.65  # the true bias (unknown to the model)
np.random.seed(7)

# Bayesian update: prior is uniform (Beta(1,1)), update with observations
alpha, beta = 1, 1  # start with no knowledge

print("Estimating the probability a biased coin lands heads.")
print(f"True probability: {true_p_heads} (unknown to the model)")
print()
print(f"{'Flips':>6}  {'Estimate':>10}  {'95% Interval':>25}  {'Interval Width':>15}")
print("-" * 62)

for n_flips in [1, 5, 10, 30, 100, 300, 1000]:
    flips = np.random.binomial(1, true_p_heads, size=n_flips)
    alpha = 1 + flips.sum()
    beta  = 1 + (n_flips - flips.sum())
    dist  = stats.beta(alpha, beta)
    lo, hi = dist.ppf(0.025), dist.ppf(0.975)
    width  = hi - lo
    print(f"{n_flips:>6}  {dist.mean():>10.4f}  ({lo:.4f}, {hi:.4f}){' ':>5}  {width:>15.4f}")

print()
print("As the number of flips increases, the interval width shrinks.")
print("Epistemic uncertainty is reducible. Given enough data, it disappears.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3: LLM Epistemic Uncertainty
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 3: LLM Epistemic Uncertainty")
print("=" * 60)

# An LLM forecasting temperature has no access to today's actual sensor data.
# Its epistemic uncertainty is therefore larger than a model with real-time data.
# We show the difference between two hypothetical forecasts.

llm_forecast    = stats.norm(loc=18.0, scale=7.0)   # wider: no current data
sensor_forecast = stats.norm(loc=18.3, scale=2.5)   # narrower: real sensor readings

print("Forecasting tomorrow's temperature:")
print()
print("LLM forecast (no access to current sensor data):")
print(f"  Mean:        {llm_forecast.mean():.1f} degrees")
print(f"  Std:         {llm_forecast.std():.1f} degrees")
print(f"  90% interval: ({llm_forecast.ppf(0.05):.1f}, {llm_forecast.ppf(0.95):.1f})")
print()
print("Sensor-based model (has current atmospheric readings):")
print(f"  Mean:        {sensor_forecast.mean():.1f} degrees")
print(f"  Std:         {sensor_forecast.std():.1f} degrees")
print(f"  90% interval: ({sensor_forecast.ppf(0.05):.1f}, {sensor_forecast.ppf(0.95):.1f})")
print()
print("The LLM's wider distribution reflects its epistemic gap.")
print("A well-calibrated LLM should reflect this honestly.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4: Visualisation
# ─────────────────────────────────────────────────────────────────────────────

x = np.linspace(-10, 45, 1000)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle("Session 01, Topic 06: Types of Uncertainty", fontsize=13)

# Plot 1: Aleatoric floor
ax1 = axes[0]
for std_val, colour, label in [(4, "steelblue", "std = 4 (true aleatoric spread)"),
                                (4, "steelblue", None)]:
    ax1.plot(x, stats.norm.pdf(x, 18, std_val), color=colour, linewidth=2.5, label=label)
ax1.plot(x, stats.norm.pdf(x, 18, 1.5), color="red", linewidth=2, linestyle="--",
         label="std = 1.5 (overconfident, wrong)")
ax1.set_title("Aleatoric Uncertainty: The Irreducible Floor")
ax1.set_xlabel("Temperature (degrees C)")
ax1.set_ylabel("Probability Density")
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)

# Plot 2: Epistemic shrinkage
n_flips_list = [5, 30, 300, 1000]
alpha_list = [1, 1, 1, 1]
beta_list  = [1, 1, 1, 1]
np.random.seed(7)
flips_all  = np.random.binomial(1, 0.65, size=1000)

ax2 = axes[1]
p_range = np.linspace(0, 1, 500)
colours = ["red", "darkorange", "steelblue", "green"]
for n, colour in zip(n_flips_list, colours):
    a = 1 + flips_all[:n].sum()
    b = 1 + n - flips_all[:n].sum()
    ax2.plot(p_range, stats.beta.pdf(p_range, a, b), color=colour,
             linewidth=2, label=f"After {n} flips")
ax2.axvline(x=0.65, color="black", linewidth=2, linestyle="--", label="True P = 0.65")
ax2.set_title("Epistemic Uncertainty Shrinks with Data")
ax2.set_xlabel("Estimated P(heads)")
ax2.set_ylabel("Probability Density")
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)

# Plot 3: LLM vs sensor forecast
ax3 = axes[2]
ax3.plot(x, llm_forecast.pdf(x),    color="darkorange", linewidth=2.5, label="LLM (wider, no sensor data)")
ax3.plot(x, sensor_forecast.pdf(x), color="steelblue",  linewidth=2.5, label="Sensor model (narrower)")
ax3.set_title("LLM vs Sensor-Based Forecast")
ax3.set_xlabel("Temperature (degrees C)")
ax3.set_ylabel("Probability Density")
ax3.legend(fontsize=9)
ax3.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("06_uncertainty_types.png", dpi=150, bbox_inches="tight")
plt.show()

print("Plot saved as 06_uncertainty_types.png")
print("Use this image in your paper/06_background_uncertainty.md file.")
print()
print("You have completed Topic 06.")
print("Next: open learn/07_llms_as_forecasters.md")

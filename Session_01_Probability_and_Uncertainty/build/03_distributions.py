"""
Build File 03: Probability Distributions
Session 01, Topic 03: What Is a Probability Distribution?

Connected learn file: learn/03_probability_distributions.md
Connected paper file: paper/03_background_distributions.md

What this file does:
    Visualises the PDF and CDF for a continuous random variable.
    Shows how area under a PDF corresponds to probability.
    Demonstrates how distribution shape communicates uncertainty.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1: The PDF and What Its Shape Tells You
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 1: Reading a PDF")
print("=" * 60)

# We use temperature as our example random variable throughout this topic.
# Model: Y = tomorrow's max temperature in London, Gaussian(mean=18, std=5)

mean = 18.0
std  = 5.0
x    = np.linspace(-5, 45, 1000)
pdf  = stats.norm.pdf(x, loc=mean, scale=std)

# The peak of the PDF is the most likely value
peak_x    = x[np.argmax(pdf)]
peak_prob = np.max(pdf)
print(f"The PDF peaks at x = {peak_x:.1f} degrees (the most likely value)")
print(f"Peak density value: {peak_prob:.4f}")
print()
print("Note: density is NOT probability. It is probability per unit of x.")
print("You need area (density times width) to get actual probability.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2: Area Under the Curve = Probability
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 2: Area Under the Curve Is Probability")
print("=" * 60)

# Total area under the PDF = 1 (something must happen)
total_area = stats.norm.cdf(np.inf, loc=mean, scale=std) - \
             stats.norm.cdf(-np.inf, loc=mean, scale=std)
print(f"Total area under the PDF: {total_area:.6f}  (always exactly 1)")
print()

# Area between 13 and 23 degrees = P(13 < Y < 23)
lower_a, upper_a = 13, 23
area_a = stats.norm.cdf(upper_a, loc=mean, scale=std) - \
         stats.norm.cdf(lower_a, loc=mean, scale=std)
print(f"P({lower_a} < Y < {upper_a}) = {area_a:.4f}")
print(f"There is a {area_a*100:.1f}% chance the temperature is between {lower_a} and {upper_a} degrees.")
print()

# Area above 28 degrees = P(Y > 28)
lower_b = 28
area_b = 1 - stats.norm.cdf(lower_b, loc=mean, scale=std)
print(f"P(Y > {lower_b}) = {area_b:.4f}")
print(f"There is a {area_b*100:.1f}% chance of the temperature exceeding {lower_b} degrees.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3: The CDF
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 3: The Cumulative Distribution Function (CDF)")
print("=" * 60)

cdf = stats.norm.cdf(x, loc=mean, scale=std)

# Key CDF values
for temp in [10, 15, 18, 21, 25, 30]:
    prob_below = stats.norm.cdf(temp, loc=mean, scale=std)
    print(f"P(Y < {temp:>2}) = {prob_below:.4f}  ({prob_below*100:.1f}% chance it is below {temp} degrees)")

print()

# Percentiles using the inverse CDF
print("Percentiles of the temperature distribution:")
for pct in [10, 25, 50, 75, 90]:
    value = stats.norm.ppf(pct / 100, loc=mean, scale=std)
    print(f"  {pct}th percentile: {value:.2f} degrees")

print()
print("The 50th percentile equals the mean (18.0) because this is a symmetric distribution.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4: Different Shapes, Different Stories
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 4: How Shape Communicates Uncertainty")
print("=" * 60)

# Narrow distribution: confident forecast
# Wide distribution: uncertain forecast
narrow = stats.norm.pdf(x, loc=18, scale=2)
medium = stats.norm.pdf(x, loc=18, scale=5)
wide   = stats.norm.pdf(x, loc=18, scale=10)

print("Three forecasts, same expected value (18 degrees), different uncertainty:")
for label, std_val in [("Narrow (std=2)", 2), ("Medium (std=5)", 5), ("Wide (std=10)", 10)]:
    interval_90 = stats.norm.interval(0.90, loc=18, scale=std_val)
    print(f"  {label}: 90% interval is ({interval_90[0]:.1f}, {interval_90[1]:.1f}) degrees")
print()
print("A narrow interval = confident forecast. A wide interval = uncertain forecast.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5: Visualisation
# ─────────────────────────────────────────────────────────────────────────────

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle("Session 01, Topic 03: Probability Distributions", fontsize=13)

# Plot 1: PDF with shaded probability regions
ax1 = axes[0]
ax1.plot(x, pdf, color="steelblue", linewidth=2.5, label="PDF")
x_shade = np.linspace(lower_a, upper_a, 300)
ax1.fill_between(x_shade, stats.norm.pdf(x_shade, loc=mean, scale=std),
                 alpha=0.4, color="orange", label=f"P({lower_a} < Y < {upper_a}) = {area_a:.2f}")
ax1.set_title("PDF with Probability Region")
ax1.set_xlabel("Temperature (degrees C)")
ax1.set_ylabel("Probability Density")
ax1.legend(fontsize=9)
ax1.grid(alpha=0.3)

# Plot 2: CDF
ax2 = axes[1]
ax2.plot(x, cdf, color="steelblue", linewidth=2.5)
ax2.axhline(y=0.5, color="red", linestyle="--", linewidth=1, label="50th percentile")
ax2.axvline(x=mean, color="red", linestyle="--", linewidth=1)
ax2.set_title("Cumulative Distribution Function (CDF)")
ax2.set_xlabel("Temperature (degrees C)")
ax2.set_ylabel("P(Y less than or equal to x)")
ax2.legend()
ax2.grid(alpha=0.3)

# Plot 3: Three distributions showing different uncertainty levels
ax3 = axes[2]
ax3.plot(x, narrow, linewidth=2, label="Narrow: std = 2 (confident)")
ax3.plot(x, medium, linewidth=2, label="Medium: std = 5")
ax3.plot(x, wide,   linewidth=2, label="Wide: std = 10 (uncertain)")
ax3.set_title("Same Mean, Different Uncertainty")
ax3.set_xlabel("Temperature (degrees C)")
ax3.set_ylabel("Probability Density")
ax3.legend(fontsize=9)
ax3.set_xlim(-10, 50)
ax3.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("03_distributions.png", dpi=150, bbox_inches="tight")
plt.show()

print("Plot saved as 03_distributions.png")
print("Use this image in your paper/03_background_distributions.md file.")
print()
print("You have completed Topic 03.")
print("Next: open learn/04_key_distributions.md")

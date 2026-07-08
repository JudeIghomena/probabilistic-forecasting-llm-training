"""
Build File 04: The Three Key Distributions
Session 01, Topic 04: Gaussian, Laplace, and Uniform

Connected learn file: learn/04_key_distributions.md
Connected paper file: paper/04_background_families.md

What this file does:
    Implements and visualises the Gaussian, Laplace, and Uniform distributions.
    Compares their shapes, tails, and behaviour directly.
    This module becomes a reusable utility for the pipeline scoring and
    evaluation sessions that follow.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


x = np.linspace(-15, 35, 1000)
mean_val = 10.0  # shared centre for fair comparison


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1: The Gaussian Distribution
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 1: Gaussian Distribution")
print("=" * 60)

gaussian = stats.norm(loc=mean_val, scale=4)

print(f"X ~ N(mean={mean_val}, std=4)")
print(f"Mean:              {gaussian.mean():.2f}")
print(f"Standard deviation:{gaussian.std():.2f}")
print(f"90% interval:      ({gaussian.ppf(0.05):.2f}, {gaussian.ppf(0.95):.2f})")
print(f"P(X > 20):         {1 - gaussian.cdf(20):.4f}")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2: The Laplace Distribution
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 2: Laplace Distribution")
print("=" * 60)

laplace = stats.laplace(loc=mean_val, scale=3)

print(f"X ~ Laplace(location={mean_val}, scale=3)")
print(f"Mean:              {laplace.mean():.2f}")
print(f"Standard deviation:{laplace.std():.2f}")
print(f"90% interval:      ({laplace.ppf(0.05):.2f}, {laplace.ppf(0.95):.2f})")
print(f"P(X > 20):         {1 - laplace.cdf(20):.4f}")
print()

print("Compare P(X > 20) for both distributions:")
print(f"  Gaussian P(X > 20) = {1 - gaussian.cdf(20):.4f}")
print(f"  Laplace  P(X > 20) = {1 - laplace.cdf(20):.4f}")
print("Laplace assigns more probability to extreme values (heavier tails).")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3: The Uniform Distribution
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 3: Uniform Distribution")
print("=" * 60)

lower_u, upper_u = -5, 25
uniform = stats.uniform(loc=lower_u, scale=upper_u - lower_u)

print(f"X ~ Uniform(lower={lower_u}, upper={upper_u})")
print(f"Mean:              {uniform.mean():.2f}")
print(f"Standard deviation:{uniform.std():.2f}")
print(f"P(X > 20):         {1 - uniform.cdf(20):.4f}")
print()
print("The uniform distribution has no peak. Every value is equally likely.")
print("This represents maximum uncertainty within the range.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4: Tail Comparison
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 4: Tail Comparison at Extreme Values")
print("=" * 60)

print("How much probability each distribution assigns beyond extreme thresholds:")
print(f"{'Threshold':>12}  {'Gaussian':>10}  {'Laplace':>10}")
print("-" * 36)

for threshold in [15, 18, 20, 23, 25]:
    g_tail = 1 - gaussian.cdf(threshold)
    l_tail = 1 - laplace.cdf(threshold)
    print(f"{threshold:>12}  {g_tail:>10.5f}  {l_tail:>10.5f}")

print()
print("At extreme values, Laplace always assigns more probability than Gaussian.")
print("This is what 'heavy tails' means in practice.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5: Visualisation
# ─────────────────────────────────────────────────────────────────────────────

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle("Session 01, Topic 04: The Three Key Distributions", fontsize=13)

# Plot 1: PDF comparison
ax1 = axes[0]
ax1.plot(x, gaussian.pdf(x), color="steelblue", linewidth=2.5, label="Gaussian")
ax1.plot(x, laplace.pdf(x),  color="darkorange", linewidth=2.5, label="Laplace")
ax1.plot(x, uniform.pdf(x),  color="green", linewidth=2.5, label="Uniform")
ax1.set_title("PDF Comparison")
ax1.set_xlabel("Value")
ax1.set_ylabel("Probability Density")
ax1.legend()
ax1.set_xlim(-15, 35)
ax1.grid(alpha=0.3)

# Plot 2: CDF comparison
ax2 = axes[1]
ax2.plot(x, gaussian.cdf(x), color="steelblue", linewidth=2.5, label="Gaussian")
ax2.plot(x, laplace.cdf(x),  color="darkorange", linewidth=2.5, label="Laplace")
ax2.plot(x, uniform.cdf(x),  color="green", linewidth=2.5, label="Uniform")
ax2.set_title("CDF Comparison")
ax2.set_xlabel("Value")
ax2.set_ylabel("Cumulative Probability")
ax2.legend()
ax2.set_xlim(-15, 35)
ax2.grid(alpha=0.3)

# Plot 3: Log scale to show tail differences clearly
ax3 = axes[2]
ax3.plot(x, gaussian.pdf(x), color="steelblue", linewidth=2.5, label="Gaussian")
ax3.plot(x, laplace.pdf(x),  color="darkorange", linewidth=2.5, label="Laplace")
ax3.set_yscale("log")
ax3.set_title("PDF on Log Scale (shows tail behaviour)")
ax3.set_xlabel("Value")
ax3.set_ylabel("Probability Density (log scale)")
ax3.legend()
ax3.set_xlim(-15, 35)
ax3.set_ylim(1e-8, 1)
ax3.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("04_key_distributions.png", dpi=150, bbox_inches="tight")
plt.show()

print("Plot saved as 04_key_distributions.png")
print("Use this image in your paper/04_background_families.md file.")
print()
print("You have completed Topic 04.")
print("Next: open learn/05_point_vs_predictive.md")

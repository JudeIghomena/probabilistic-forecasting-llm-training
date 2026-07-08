"""
Build File 07: LLMs as Forecasters - Concept and Mock Pipeline
Session 01, Topic 07: LLMs as Forecasters

Connected learn file: learn/07_llms_as_forecasters.md
Connected paper file: paper/07_research_question.md

What this file does:
    Shows the structure of an LLM forecasting request without making real API calls.
    Defines the three output formats (quantile, parametric, sample).
    Shows how a response would be parsed and what a failure mode looks like.
    Builds intuition for Sessions 03 and 04 where the real pipeline is constructed.

No API key required. Everything here is simulated to illustrate the concepts.
"""

import numpy as np
from scipy import stats


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1: What a Forecasting Prompt Looks Like
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 1: Structure of a Probabilistic Forecasting Prompt")
print("=" * 60)

# This is an example of the kind of prompt we will send to Claude, GPT-4o,
# and Llama in Sessions 03 and 04.

example_prompt = """
You are a probabilistic forecasting assistant.

Historical data: The average daily temperature in London in October
over the past 30 years has been 13.0 degrees Celsius, with a standard
deviation of 3.2 degrees.

Task: Provide a probabilistic forecast for the average temperature
this October in London.

Please respond in this exact format:
  point_estimate: [your best guess in degrees C]
  distribution: [Gaussian, Laplace, or Uniform]
  mean: [mean parameter of your chosen distribution]
  std: [standard deviation or scale parameter]
  interval_90_low: [5th percentile of your distribution]
  interval_90_high: [95th percentile of your distribution]
"""

print("Example prompt sent to an LLM:")
print(example_prompt)

print()
print("Notice the prompt:")
print("  - Gives the LLM the historical context it needs.")
print("  - Asks for a specific distribution family by name.")
print("  - Asks for a 90 percent interval (5th to 95th percentile).")
print("  - Uses a rigid format that can be parsed by our pipeline.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2: Simulating What a Well-Calibrated LLM Might Return
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 2: A Well-Calibrated Response")
print("=" * 60)

# A well-calibrated LLM would roughly recover the historical statistics.
# Here we simulate what that response looks like when parsed.

simulated_response_good = {
    "point_estimate": 13.0,
    "distribution": "Gaussian",
    "mean": 13.0,
    "std": 3.2,
    "interval_90_low": 13.0 - 1.645 * 3.2,
    "interval_90_high": 13.0 + 1.645 * 3.2,
}

parsed_mean = simulated_response_good["mean"]
parsed_std  = simulated_response_good["std"]
parsed_lo   = simulated_response_good["interval_90_low"]
parsed_hi   = simulated_response_good["interval_90_high"]

print("Simulated well-calibrated LLM response (parsed):")
for key, val in simulated_response_good.items():
    print(f"  {key}: {val:.2f}" if isinstance(val, float) else f"  {key}: {val}")

print()

# Verify the stated interval matches the stated distribution.
dist = stats.norm(parsed_mean, parsed_std)
computed_lo = dist.ppf(0.05)
computed_hi = dist.ppf(0.95)
interval_consistent = (
    abs(computed_lo - parsed_lo) < 0.05 and
    abs(computed_hi - parsed_hi) < 0.05
)

print("Consistency check: do the stated mean/std produce the stated 90% interval?")
print(f"  Distribution implies interval: ({computed_lo:.2f}, {computed_hi:.2f})")
print(f"  Stated interval:               ({parsed_lo:.2f}, {parsed_hi:.2f})")
print(f"  Consistent: {interval_consistent}")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3: Simulating What an Overconfident LLM Might Return
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 3: An Overconfident Response")
print("=" * 60)

# An overconfident LLM might claim much tighter uncertainty than the data supports.
# This is one of the three failure modes described in the learn file.

simulated_response_overconfident = {
    "point_estimate": 13.0,
    "distribution": "Gaussian",
    "mean": 13.0,
    "std": 1.0,   # way too narrow
    "interval_90_low": 13.0 - 1.645 * 1.0,
    "interval_90_high": 13.0 + 1.645 * 1.0,
}

oc_std = simulated_response_overconfident["std"]
oc_lo  = simulated_response_overconfident["interval_90_low"]
oc_hi  = simulated_response_overconfident["interval_90_high"]

print("Simulated overconfident LLM response (parsed):")
for key, val in simulated_response_overconfident.items():
    print(f"  {key}: {val:.2f}" if isinstance(val, float) else f"  {key}: {val}")

print()
print(f"The true historical std is 3.2. The LLM claimed std = {oc_std}.")
print(f"Stated 90% interval: ({oc_lo:.2f}, {oc_hi:.2f})")
print(f"If we ran 100 October forecasts with this model, the true temperature")
print(f"would fall OUTSIDE the stated 90% interval far more often than 10% of the time.")
print(f"This is a calibration failure. It is what CRPS and Log-Score will detect.")
print()

# Simulate calibration check
true_std = 3.2
np.random.seed(42)
true_outcomes = np.random.normal(13.0, true_std, size=1000)
inside_overconfident = np.mean((true_outcomes >= oc_lo) & (true_outcomes <= oc_hi))

print(f"Calibration simulation ({1000} true outcomes drawn from true distribution):")
print(f"  Coverage of overconfident 90% interval: {inside_overconfident * 100:.1f}%")
print(f"  Expected coverage: 90.0%")
print(f"  The interval is too narrow. The stated confidence is not earned.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4: The Three LLMs This Project Will Benchmark
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 4: The Three LLMs in This Project")
print("=" * 60)

llm_models = [
    {
        "name": "Claude (Anthropic)",
        "access": "Anthropic API",
        "key_env_var": "ANTHROPIC_API_KEY",
        "type": "Commercial, closed-source",
        "sessions": "Sessions 03 and 05",
    },
    {
        "name": "GPT-4o (OpenAI)",
        "access": "OpenAI API",
        "key_env_var": "OPENAI_API_KEY",
        "type": "Commercial, closed-source",
        "sessions": "Sessions 03 and 05",
    },
    {
        "name": "Llama 3.1-8B (Meta via Hugging Face)",
        "access": "Hugging Face Inference API",
        "key_env_var": "HUGGINGFACE_API_KEY",
        "type": "Open-source",
        "sessions": "Sessions 03 and 05",
    },
]

print(f"{'Model':<40} {'Access Method':<30} {'Key Variable':<25}")
print("-" * 95)
for m in llm_models:
    print(f"{m['name']:<40} {m['access']:<30} {m['key_env_var']:<25}")

print()
print("All three models will receive identical prompts and be scored by the same metrics.")
print("Any performance gap we measure reflects genuine differences in probabilistic reasoning.")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5: The Three Output Formats We Will Accept
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 5: Three Output Formats")
print("=" * 60)

# Format 1: Quantile format
# The LLM states specific probability thresholds directly.
print("Format 1 - Quantile Format:")
quantile_levels = [0.1, 0.25, 0.5, 0.75, 0.9]
true_distribution = stats.norm(13.0, 3.2)
quantile_values = [round(true_distribution.ppf(q), 2) for q in quantile_levels]

print(f"  {'Probability Level':<20} {'Temperature (deg C)':<20}")
print(f"  {'-'*40}")
for level, value in zip(quantile_levels, quantile_values):
    print(f"  {level:<20} {value:<20}")
print()

# Format 2: Parametric format
# The LLM names a distribution and states its parameters.
print("Format 2 - Parametric Format:")
print("  distribution: Gaussian")
print("  mean: 13.0")
print("  std: 3.2")
print()
print("  The pipeline then computes any quantile it needs from these parameters.")
computed_90_interval = (true_distribution.ppf(0.05), true_distribution.ppf(0.95))
print(f"  90% interval computed from parameters: ({computed_90_interval[0]:.2f}, {computed_90_interval[1]:.2f})")
print()

# Format 3: Sample format
# The LLM generates N plausible values.
print("Format 3 - Sample Format:")
np.random.seed(99)
samples = np.round(true_distribution.rvs(20), 2)
print(f"  20 samples drawn from the stated distribution:")
print(f"  {list(samples)}")
print()
print(f"  Sample mean: {samples.mean():.2f}")
print(f"  Sample std:  {samples.std():.2f}")
print()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 6: What the Pipeline Will Do With These Responses
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("SECTION 6: What the Pipeline Does With Each Response")
print("=" * 60)

print("For each LLM response, the pipeline will:")
print()
print("  Step 1. Parse the response into a structured format.")
print("  Step 2. Check that the response is internally consistent.")
print("          (e.g. do the stated parameters produce the stated interval?)")
print("  Step 3. Score the distribution against the true observed outcome using:")
print("          - CRPS (Continuous Ranked Probability Score)  [Session 06]")
print("          - Log-Score                                   [Session 06]")
print("          - Interval Coverage at 50%, 90%               [Session 06]")
print("  Step 4. Repeat across many forecasting tasks to build a calibration picture.")
print("  Step 5. Compare each LLM against classical baselines.")
print("          (ARIMA, Quantile Regression, Deep Ensembles)  [Sessions 07 and 08]")
print()
print("This is what the next nine sessions build, one layer at a time.")
print()
print("You have completed Topic 07 and Session 01.")
print("Open paper/07_research_question.md and write your draft.")
print("Then open Session_01_Probability_and_Uncertainty/INTRO.md")
print("and work through the final completion checklist.")

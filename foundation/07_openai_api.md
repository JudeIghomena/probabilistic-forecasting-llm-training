# Foundation Guide 07 — OpenAI API

**Complete Foundation Guide 03 (Claude CLI) before this.
The pattern here is identical to what you did for Anthropic.**

---

## Why OpenAI in This Project?

This project evaluates multiple LLMs, not just Claude. GPT-4o (OpenAI's
flagship model) is one of the two commercial LLMs being benchmarked.
You will send the same probabilistic forecasting prompts to both Claude and
GPT-4o and compare their calibration and accuracy using the same scoring rules.

To do that, your pipeline needs access to the OpenAI API alongside the
Anthropic API.

---

## Step 1 — Create an OpenAI Account

1. Go to platform.openai.com in your browser
2. Click "Sign up"
3. Create an account with your email address
4. Verify your email

---

## Step 2 — Add Billing (Required for API Access)

OpenAI's API is not free. You need to add a payment method and purchase credits.

1. After logging in, go to platform.openai.com/settings/billing
2. Click "Add payment method"
3. Add a card and purchase a small starting credit

For this project, a starting credit of $5 to $10 is sufficient. The pipeline
will make a controlled number of API calls per experiment, and GPT-4o-mini
can be used for exploration at much lower cost than GPT-4o.

---

## Step 3 — Create an API Key

1. Go to platform.openai.com/api-keys
2. Click "Create new secret key"
3. Give it a name: "probability-pipeline-project"
4. Click "Create secret key"
5. Copy the key immediately — it starts with `sk-`
6. Store it somewhere safe. You cannot view it again after closing this page.

---

## Step 4 — Store the Key as an Environment Variable

Never put the key in a code file. Store it as an environment variable
exactly the same way as the Anthropic key.

**macOS / Linux:**
```
echo 'export OPENAI_API_KEY="your-key-here"' >> ~/.zshrc
source ~/.zshrc
```

**Windows (PowerShell):**
```
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your-key-here", "User")
```

Close and reopen your terminal after running this.

**Verify:**
```
echo $OPENAI_API_KEY
```

---

## Step 5 — Install the OpenAI Python Library

With your virtual environment active:

```
pip install openai
```

---

## Step 6 — Test the Connection

Create a file called `test_openai.py` and run it:

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Give me a single number: your best point estimate for tomorrow's high temperature in London in degrees Celsius."
        }
    ],
    max_tokens=20
)

print(response.choices[0].message.content)
```

If you see a temperature value printed, the connection is working.

Note: we use `gpt-4o-mini` here for testing because it is cheaper. The
main benchmarking sessions will switch to `gpt-4o` for the formal evaluation.

---

## Step 7 — Understand the Cost Structure

OpenAI charges per token. A token is roughly 0.75 of a word.

| Model | Input cost (per 1M tokens) | Output cost (per 1M tokens) |
|---|---|---|
| gpt-4o-mini | $0.15 | $0.60 |
| gpt-4o | $5.00 | $15.00 |

For this project, the pipeline will send hundreds of forecasting prompts
in the benchmarking sessions. Use `gpt-4o-mini` for exploration and
testing throughout Sessions 03 and 04. Switch to `gpt-4o` only for the
formal benchmark runs in Sessions 09 and 10.

You can track your spending at platform.openai.com/usage.

Set a monthly spending limit to avoid surprises:
1. Go to platform.openai.com/settings/limits
2. Set a hard monthly limit (e.g., $10)

---

## Step 8 — How the Pipeline Reads the Key

In every pipeline file that calls OpenAI, the key is read from the
environment variable, never hardcoded:

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
```

This is the standard pattern throughout this project. You will see it in
Sessions 03 and 04 when we build the LLM querying module.

---

## Troubleshooting

**AuthenticationError: No API key provided:**
The environment variable is not set or not visible in the current terminal.
Run `echo $OPENAI_API_KEY` to check. If empty, repeat Step 4 and open a
new terminal window.

**RateLimitError:**
You have exceeded your usage quota or hit a rate limit. Wait a few seconds
and retry. The pipeline code has built-in retry logic for this.

**InsufficientQuotaError:**
Your credits have run out. Go to platform.openai.com/settings/billing
and add more.

---

## Next Step

Move to:

`foundation/08_huggingface_and_llama.md`

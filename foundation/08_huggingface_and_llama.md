# Foundation Guide 08 — Hugging Face and Llama

**Complete Foundation Guides 03 and 07 (Anthropic and OpenAI API) before this.**

---

## Why Hugging Face and Llama in This Project?

Claude and GPT-4o are commercial, closed-source models. They are powerful
but they cost money per call and you cannot see their internal weights.

Llama (developed by Meta) is an open-source LLM. It is publicly available,
can be run on your own machine, and represents a growing class of models that
researchers and developers use as alternatives to commercial APIs.

This project benchmarks three categories of LLMs:
- Commercial closed-source: Claude (Anthropic), GPT-4o (OpenAI)
- Open-source via API: Llama (Meta, accessed through Hugging Face)

Hugging Face is the platform that hosts Llama and thousands of other
open-source models. It provides two ways to use them:

1. The Inference API — you call the model remotely, like a commercial API
2. Local download — you download the model weights and run it on your machine

This project uses the Inference API as the primary approach because it
requires no GPU and works on any computer. Local download is covered at
the end of this guide as an optional extension for students with GPU access.

---

## Step 1 — Create a Hugging Face Account

1. Go to huggingface.co in your browser
2. Click "Sign Up"
3. Create an account with your email
4. Verify your email address

---

## Step 2 — Create an Access Token

1. Log in to Hugging Face
2. Click your profile picture in the top right
3. Click "Settings"
4. In the left sidebar, click "Access Tokens"
5. Click "New token"
6. Give it a name: "probability-pipeline-project"
7. Set the role to "Read"
8. Click "Generate a token"
9. Copy the token — it starts with `hf_`
10. Store it safely. You can view it again later in settings, but treat it as a secret.

---

## Step 3 — Store the Token as an Environment Variable

**macOS / Linux:**
```
echo 'export HUGGINGFACE_API_KEY="your-token-here"' >> ~/.zshrc
source ~/.zshrc
```

**Windows (PowerShell):**
```
[System.Environment]::SetEnvironmentVariable("HUGGINGFACE_API_KEY", "your-token-here", "User")
```

**Verify:**
```
echo $HUGGINGFACE_API_KEY
```

---

## Step 4 — Install the Required Libraries

With your virtual environment active:

```
pip install huggingface_hub transformers requests
```

`huggingface_hub` handles authentication and model downloads.
`transformers` is the core library for working with models locally.
`requests` is used for direct API calls to the Inference API.

---

## Step 5 — Request Access to Llama

Meta requires you to accept a licence agreement before downloading or using
Llama models through the API.

1. Go to huggingface.co/meta-llama/Llama-3.1-8B-Instruct
2. Click "Request access" or "Agree and access repository"
3. Fill in the required fields (name, intended use)
4. Submit the request

Access is usually granted within a few minutes to a few hours.

You can check your access status at huggingface.co/settings/gated-repos.

---

## Step 6 — Test the Inference API

The Hugging Face Inference API lets you call Llama remotely without
downloading any model files. This is what the pipeline uses.

Create a file called `test_llama.py` and run it:

```python
import os
import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.1-8B-Instruct"
headers = {"Authorization": f"Bearer {os.environ.get('HUGGINGFACE_API_KEY')}"}

def query_llama(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "return_full_text": False
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

result = query_llama(
    "Give me a single number: your best estimate for tomorrow's high "
    "temperature in London in degrees Celsius. Reply with only the number."
)

print(result)
```

If you see a response containing a number, the Inference API is working.

Note: the free Inference API has rate limits and the model may take a moment
to load if it has not been used recently. If you see a "Loading" message in
the response, wait 30 seconds and try again.

---

## Step 7 — Understand Llama Model Sizes

Llama comes in several sizes. Larger models are more capable but slower and
more expensive (or require more GPU memory for local use).

| Model | Parameters | When to Use |
|---|---|---|
| Llama-3.1-8B-Instruct | 8 billion | Fast, cheap, good for exploration and testing |
| Llama-3.1-70B-Instruct | 70 billion | More capable, better for formal benchmarking |
| Llama-3.1-405B-Instruct | 405 billion | Most capable, requires PRO API or powerful GPU |

For this project:
- Use 8B for development and testing throughout Sessions 03 and 04
- Switch to 70B for the formal benchmark runs in Sessions 09 and 10

---

## Optional Extension — Running Llama Locally

If you have a computer with a dedicated GPU (NVIDIA with at least 8GB VRAM
for the 8B model, at least 40GB VRAM for the 70B model), you can download
and run Llama entirely on your own hardware. This removes rate limits and
gives you faster responses at scale.

This approach uses the `transformers` library and is recommended only if you
have confirmed GPU access. If you are unsure whether your computer qualifies,
use the Inference API approach above — it works on any machine.

**To run locally (GPU required):**

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install accelerate bitsandbytes
```

Then in Python:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "meta-llama/Llama-3.1-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

inputs = tokenizer("What is 2 + 2?", return_tensors="pt").to(model.device)
output = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

The first run downloads the model weights (several GB). Subsequent runs
load from cache.

Ask your supervisor whether local GPU access is available for this project
before attempting the local setup.

---

## How All Three LLM APIs Compare

| Aspect | Claude (Anthropic) | GPT-4o (OpenAI) | Llama (Hugging Face) |
|---|---|---|---|
| Access method | Anthropic API + CLI | OpenAI API | Inference API or local |
| Cost | Pay per token | Pay per token | Free tier available |
| Open source | No | No | Yes |
| Key variable | ANTHROPIC_API_KEY | OPENAI_API_KEY | HUGGINGFACE_API_KEY |
| Python library | anthropic | openai | requests or transformers |
| Session first used | Session 03 | Session 03 | Session 03 |

---

## Troubleshooting

**"Model is currently loading" in the API response:**
The Inference API loads models on demand. Wait 30 seconds and retry.
This only happens on the first call — subsequent calls are fast.

**401 Unauthorized:**
Your token is incorrect or not set. Run `echo $HUGGINGFACE_API_KEY` to check.

**403 Forbidden:**
You have not been granted access to the Llama model yet. Check your access
request status at huggingface.co/settings/gated-repos and wait for approval.

**Out of memory when running locally:**
The model is too large for your GPU. Switch to the 8B model or use the
Inference API instead.

---

## Next Step

Move to:

`foundation/09_obsidian.md`

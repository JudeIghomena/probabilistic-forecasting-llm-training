# Foundation Guide 03: Setting Up Claude CLI

**Complete Foundation Guides 01 and 02 before this.**

---

## What Is Claude CLI?

Claude CLI (Command Line Interface) is a tool that lets you talk to Claude
directly from your terminal, without opening a browser or the desktop app.

In this project, the pipeline code will use Claude CLI to send forecasting
requests to Claude programmatically, meaning the code itself talks to Claude,
not you manually. This is how the benchmarking pipeline queries the LLM at scale.

You will also use it directly in the terminal to test prompts quickly.

---

## Step 1: Install Node.js (Required First)

Claude CLI is installed through npm, which comes with Node.js.

Check if Node.js is already installed:

```
node --version
```

If you see a version number (v18 or higher), skip to Step 2.

If not, install Node.js:

1. Go to nodejs.org in your browser
2. Download the LTS (Long Term Support) version, it is the most stable
3. Run the installer and follow the steps
4. Open a new terminal and run `node --version` to confirm it worked

---

## Step 2: Install Claude CLI

With Node.js installed, run this in your terminal:

```
npm install -g @anthropic-ai/claude-code
```

The `-g` flag installs it globally, meaning you can use it from any folder
on your computer, not just the project folder.

When the install finishes, confirm it worked:

```
claude --version
```

You should see a version number printed.

---

## Step 3: Get Your Anthropic API Key

The CLI needs an API key to connect to Anthropic's servers.

1. Go to console.anthropic.com in your browser
2. Sign in with the same account you used for the desktop app
3. In the left sidebar, click "API Keys"
4. Click "Create Key"
5. Give it a name like "probability-pipeline-project"
6. Copy the key, it starts with `sk-ant-`
7. Store it somewhere safe immediately. You cannot view it again after closing that page.

---

## Step 4: Store the API Key as an Environment Variable

Never paste your API key directly into code files. If you commit code to GitHub
with a key inside it, that key is compromised and must be deleted immediately.

The correct approach is to store the key as an environment variable, a named
value your operating system holds in memory that your code can read without
the key ever appearing in the file.

**macOS / Linux (permanent setup):**

Open your terminal and run:

```
echo 'export ANTHROPIC_API_KEY="your-key-here"' >> ~/.zshrc
source ~/.zshrc
```

Replace `your-key-here` with your actual key. If you use bash instead of zsh,
replace `.zshrc` with `.bashrc`.

**Windows (PowerShell, permanent setup):**

```
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "your-key-here", "User")
```

Close and reopen PowerShell after running this.

**Verify the key is set:**

```
echo $ANTHROPIC_API_KEY
```

You should see your key printed. If it prints nothing, the variable was not set.

---

## Step 5: Log In to Claude CLI

Run:

```
claude
```

The CLI will open an interactive session. Type a message and press Enter:

```
Hello. What is the Gaussian distribution in one sentence?
```

If Claude responds, your CLI is fully set up and connected.

Press Ctrl + C to exit the interactive session.

---

## Step 6: Test a Non-Interactive Request

In the pipeline, we will call Claude non-interactively, passing a prompt and
getting a response back as text, without a back-and-forth conversation.

Test this now:

```
claude -p "Give me the 10th, 50th, and 90th percentile forecast for tomorrow's
temperature in London, assuming current conditions. Return only the three numbers
separated by commas."
```

You should get a response with three numbers. This is exactly the kind of call
the pipeline will make at scale in Sessions 04 and 09.

---

## Step 7: Understand the Difference Between the Desktop App and the CLI

Both connect to Claude, but they are used differently in this project:

| Tool | When You Use It | What It Does |
|---|---|---|
| Claude Code Desktop | During build sessions | Reads your files, writes and runs code, explains errors |
| Claude CLI | Inside the pipeline code | Called programmatically to get forecasts at scale |

The desktop app is for you as a developer. The CLI is for your code to call.

---

## Step 8: The --print Flag (Important for the Pipeline)

When the pipeline code calls Claude, it uses the `--print` flag to get the
response as plain text and exit immediately, without opening an interactive session.

```
claude --print "What is 2 + 2?"
```

This returns just the answer and exits. The pipeline captures this output
and parses it. You will see this pattern throughout Sessions 04 and 09.

---

## Troubleshooting

**"claude: command not found" after installing:**
npm's global folder may not be in your PATH. Run `npm bin -g` to find where
global packages are installed, then add that path to your PATH variable.
Ask Claude Code to help you do this for your specific operating system.

**API key not found error:**
Run `echo $ANTHROPIC_API_KEY` to check the variable is set. If it is empty,
repeat Step 4. Make sure you opened a new terminal after setting it.

**Rate limit errors:**
The free tier of the Anthropic API has usage limits. If you see a rate limit
error during the pipeline sessions, wait a few minutes before retrying.
The pipeline code includes retry logic for this reason.

---

## Security Rules: Read These and Remember Them

These rules apply for the entire duration of this project:

1. Never put your API key in a Python file, notebook, or any file committed to GitHub
2. Never share your API key with anyone
3. If you accidentally commit a key to GitHub, go to console.anthropic.com and delete it immediately, then create a new one
4. Always read the key from the environment variable `ANTHROPIC_API_KEY` in code:

```python
import os
api_key = os.environ.get("ANTHROPIC_API_KEY")
```

---

## You Are Ready

All three foundation guides are complete. You have:

- Python installed with all required libraries
- Claude Code desktop app set up and connected to your project folder
- Claude CLI installed, authenticated, and tested

Go to `Session_01_Probability_and_Uncertainty/learn/session_01_learn.md`
and begin the first session.

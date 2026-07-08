# Foundation Guide 02: Setting Up Claude Code Desktop

**Complete Foundation Guide 01 (Python installation) before this.**

---

## What Is Claude Code Desktop?

Claude Code is an AI coding assistant made by Anthropic. In this project you
will use it as your pair programmer: you describe what you want to build and
Claude Code writes the code, explains it, and helps you fix errors.

This is not cheating. This is how modern software is built. Your job is to
understand every piece of code that gets generated, ask questions until you do,
and connect what you see in the code back to what you learned in the session's
learn file.

The desktop app gives you a full coding environment with Claude built in,
without needing to use a browser.

---

## Step 1: Download Claude Code Desktop

1. Go to claude.ai/download in your browser
2. Choose the version for your operating system (macOS, Windows, or Linux)
3. Download and install it the same way you would any application

**macOS:** Open the .dmg file, drag Claude to Applications, open it.

**Windows:** Run the .exe installer and follow the prompts.

**Linux:** Follow the instructions on the download page for your distribution.

---

## Step 2: Create an Anthropic Account (if you do not have one)

1. Go to claude.ai in your browser
2. Click "Sign up"
3. Create an account with your email address
4. Verify your email

You will use this same account to log in to the desktop app.

---

## Step 3: Log In to Claude Code Desktop

1. Open the Claude Code desktop app
2. Click "Sign in"
3. Enter the email and password you just created
4. The app will open to a workspace

---

## Step 4: Open a Project Folder

Claude Code works best when it can see your project files. This is called
opening a workspace or project folder.

1. In the Claude Code desktop app, look for "Open Folder" or "Open Project"
2. Navigate to the `PROBABILITY PIPELINE PROJECT TRAINING` folder on your computer
3. Select it and confirm

Claude Code will now show your project files in the sidebar and can read,
create, and edit files in that folder.

---

## Step 5: Run Your First Test

This confirms Claude Code is set up and connected to your project.

In the Claude Code chat, type:

```
Open the file Session_01_Probability_and_Uncertainty/build/probability_demo.py
and tell me what each section does in plain language.
```

Claude Code should read the file and give you a clear explanation. If it does,
everything is working.

---

## Step 6: How to Use Claude Code During This Project

Here is the workflow you will follow every session:

**During the build task:**

1. Open the build file for the session (e.g., `Session_01/build/probability_demo.py`)
2. Run it and see if it works: in the Claude Code chat, type "run this file"
3. If there are errors, paste them into the chat and ask Claude Code to explain and fix them
4. If a line of code is unclear, ask: "what does line 42 do and why?"
5. Ask Claude Code to modify things and see what changes

**Good questions to ask Claude Code:**

- "Run this file and show me the output"
- "What does this function do in plain language?"
- "Can you add a comment explaining why this line is written this way?"
- "I want the plot to show one more distribution, add the Student-t distribution"
- "This is giving an error. What is wrong and how do I fix it?"

**Questions to never skip:**

After every build session, ask Claude Code:
"What is the most important thing this code demonstrates that I should understand
before the next session?"

Write the answer in your own words in the paper contribution file.

---

## Step 7: Important Settings

**Auto-save:** Make sure auto-save is on so you do not lose work. In most
editors, this is in Settings under "Auto Save".

**Python interpreter:** When running Python files, make sure Claude Code is
using the virtual environment you created in Foundation Guide 01. If it asks
which Python to use, choose the one inside `prob_pipeline_env`.

---

## Troubleshooting

**Claude Code cannot find the file:**
Make sure you opened the correct project folder. The file paths in the build
tasks are relative to the project root.

**Errors when running Python:**
Check that your virtual environment is active. Ask Claude Code: "my virtual
environment is at prob_pipeline_env, how do I make sure this project uses it?"

**Claude Code does not respond:**
Check your internet connection. Claude Code requires a connection to Anthropic's
servers to generate responses.

---

## Next Step

Move to:

`foundation/03_setup_claude_cli.md`

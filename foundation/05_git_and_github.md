# Foundation Guide 05 — Git and GitHub

**Complete Foundation Guide 04 (VS Code) before this.**

---

## What Are Git and GitHub?

**Git** is a version control system. It tracks every change you make to your
code and lets you go back to any previous version. Think of it as an unlimited
undo history for your entire project, not just the last few actions.

**GitHub** is a website where you store your Git-tracked projects online.
It keeps a backup of your work in the cloud, lets you share code with others,
and is where the training curriculum lives so you can access it.

In this project you use Git and GitHub for three things:

1. Clone the training curriculum to your own computer so you have all the files
2. Track changes to your pipeline code as you build it across sessions
3. Push your completed work online so it is backed up and shareable

---

## Step 1 — Install Git

**Check if Git is already installed:**

```
git --version
```

If you see a version number, skip to Step 2.

**macOS:**

Git is usually already installed on macOS. If not:

```
xcode-select --install
```

A dialog will appear asking you to install developer tools. Accept it.
Git will be included.

Alternatively, install it with Homebrew if you have it:

```
brew install git
```

**Windows:**

1. Go to git-scm.com in your browser
2. Click "Download for Windows"
3. Run the installer
4. On the "Adjusting your PATH environment" screen, select
   "Git from the command line and also from 3rd-party software"
5. Accept all other defaults and complete the installation
6. Open a new PowerShell window and run `git --version`

**Linux (Ubuntu/Debian):**

```
sudo apt update
sudo apt install git
```

---

## Step 2 — Create a GitHub Account

1. Go to github.com in your browser
2. Click "Sign up"
3. Choose a username, enter your email, and set a password
4. Verify your email address

Your GitHub username will be publicly visible, so choose something
professional — your name or initials is fine.

---

## Step 3 — Configure Git with Your Identity

Git needs to know who you are so your commits are labelled correctly.
Run these two commands in your terminal, replacing the values with your
own name and GitHub email:

```
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

Verify the settings were saved:

```
git config --list
```

You should see your name and email in the output.

---

## Step 4 — Clone the Training Repository

Cloning means downloading the project from GitHub to your computer,
with the full Git history attached. This is how you get all the session
files onto your machine.

1. Go to github.com/JudeIghomena/probabilistic-forecasting-llm-training
2. Click the green "Code" button
3. Copy the HTTPS URL shown

In your terminal, navigate to where you want to store the project and run:

```
git clone https://github.com/JudeIghomena/probabilistic-forecasting-llm-training.git
```

This creates a folder called `probabilistic-forecasting-llm-training` with
all the session files inside.

Then open that folder in VS Code:

```
code probabilistic-forecasting-llm-training
```

---

## Step 5 — Understand the Core Git Commands

You will use these six commands throughout every session:

**Check what has changed:**
```
git status
```
Shows which files have been modified, added, or deleted since your last commit.

**Stage changes (tell Git which files to include in the next save):**
```
git add filename.py
```

To stage everything in the current folder:
```
git add .
```

**Commit (save a snapshot with a message describing what changed):**
```
git commit -m "Session 01: add probability demo and paper introduction"
```

The message should be short and say what you did, not just "update".

**Push (send your commits to GitHub):**
```
git push
```

**Pull (download the latest changes from GitHub):**
```
git pull
```

Run this at the start of every session to make sure you have the latest
session files.

**View the commit history:**
```
git log --oneline
```

---

## Step 6 — The Session Commit Habit

At the end of every build session, commit and push your work.
This is your session backup. Never end a session without doing this.

```
git add .
git commit -m "Session 01: completed probability demo and paper introduction draft"
git push
```

If you skip this and your computer crashes, the session's work is gone.

---

## Step 7 — What to Never Commit

Some files must never go to GitHub:

- Your `.env` file or any file containing API keys
- Your virtual environment folder (`prob_pipeline_env/`)
- Large data files (datasets over a few MB)

These are already excluded by the `.gitignore` file in the project. But
make a habit of running `git status` before every `git add .` to check
what is about to be staged. If you see anything unexpected, do not commit
until you understand what it is.

---

## Troubleshooting

**"Authentication failed" when pushing:**
GitHub stopped accepting passwords for Git operations. You need to use a
Personal Access Token instead. Go to github.com, click your profile picture,
then Settings, then Developer Settings, then Personal Access Tokens, then
"Tokens (classic)". Generate a new token with "repo" scope. Use this token
as your password when Git asks.

**"fatal: not a git repository":**
You are running a Git command from the wrong folder. Navigate into the
project folder first: `cd probabilistic-forecasting-llm-training`

**Merge conflict:**
This happens when two changes affect the same line. Git will mark the
conflict in the file. Ask Claude Code to explain and resolve the conflict
for you — it handles these well.

---

## Next Step

Move to:

`foundation/06_jupyter_notebooks.md`

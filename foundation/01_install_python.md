# Foundation Guide 01 — Installing Python

**Read this first. Complete it before opening any session files.**

---

## What Is Python and Why Do We Use It?

Python is a programming language. It is what we will use to build the entire
benchmarking pipeline in this project. You write instructions in Python and
your computer follows them.

We chose Python for this project for three reasons:

1. It has the best libraries for data science and machine learning in the world
2. Every major AI company (Anthropic, OpenAI, Google) provides Python SDKs for their APIs
3. It is readable enough for a beginner to follow along while being powerful enough for production research

---

## Step 1 — Check If Python Is Already Installed

Open a terminal on your computer and type:

```
python --version
```

or

```
python3 --version
```

If you see something like `Python 3.11.4` or higher, Python is already installed.
Skip to Step 3.

If you see `command not found` or a version below 3.9, continue to Step 2.

### How to Open a Terminal

**macOS:** Press Command + Space, type "Terminal", press Enter.

**Windows:** Press Windows key, type "PowerShell", press Enter. Or use Windows
Terminal if you have it installed.

**Linux:** Press Ctrl + Alt + T, or search for "Terminal" in your applications.

---

## Step 2 — Install Python

### macOS

The recommended way on macOS is to install Python through the official website.

1. Open your browser and go to python.org/downloads
2. Click the large yellow button that says "Download Python 3.x.x"
3. Open the downloaded file and follow the installer steps
4. When the installer finishes, open a new terminal and run: `python3 --version`
5. You should see Python 3.11 or higher

### Windows

1. Open your browser and go to python.org/downloads
2. Click "Download Python 3.x.x"
3. Open the downloaded installer
4. IMPORTANT: On the first screen, tick the box that says "Add Python to PATH"
   before clicking Install Now. This step is easy to miss and causes problems later.
5. Click "Install Now"
6. When done, open PowerShell and run: `python --version`

### Linux (Ubuntu or Debian)

Open a terminal and run:

```
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

---

## Step 3 — Install pip

pip is the Python package manager. It lets you install libraries like numpy,
matplotlib, and the Anthropic API client.

Check if pip is installed:

```
pip --version
```

or

```
pip3 --version
```

If it is not found, install it:

**macOS / Linux:**
```
python3 -m ensurepip --upgrade
```

**Windows:**
```
python -m ensurepip --upgrade
```

---

## Step 4 — Create a Virtual Environment for This Project

A virtual environment is an isolated Python workspace. It keeps the packages
you install for this project separate from everything else on your computer.
This prevents version conflicts and keeps things clean.

Navigate to where you want to store the project code and run:

**macOS / Linux:**
```
python3 -m venv prob_pipeline_env
source prob_pipeline_env/bin/activate
```

**Windows (PowerShell):**
```
python -m venv prob_pipeline_env
prob_pipeline_env\Scripts\Activate.ps1
```

When the environment is active, your terminal prompt will show the environment
name in brackets, like: `(prob_pipeline_env) $`

---

## Step 5 — Install the Core Libraries

With your virtual environment active, install all the libraries this project uses:

```
pip install numpy scipy pandas matplotlib statsmodels properscoring anthropic openai
```

This will take a minute. When it finishes, verify the key installs:

```
python -c "import numpy; import scipy; import matplotlib; print('All good')"
```

If you see `All good`, you are ready.

---

## Step 6 — Install Jupyter (Optional but Recommended)

Jupyter notebooks let you run Python code one small block at a time and see
the output immediately below each block. This is very useful for learning.

```
pip install jupyter
```

To open a notebook:

```
jupyter notebook
```

Your browser will open with a file browser. You can create new notebooks there.

---

## Troubleshooting Common Problems

**"python is not recognized" on Windows:**
You likely did not tick "Add Python to PATH" during installation. Uninstall Python
and reinstall, making sure to check that box on the first screen.

**"Permission denied" on macOS / Linux:**
Do not use sudo with pip inside a virtual environment. If you see this error,
make sure your virtual environment is active first.

**pip installs but import fails:**
You may have multiple Python versions installed. Make sure you activated the
virtual environment before installing, and that you are using the same Python
to run your files.

---

## Verify Everything Is Working

Run this to confirm your setup is correct:

```python
python -c "
import sys
import numpy as np
import scipy
import matplotlib
print(f'Python version: {sys.version}')
print(f'numpy: {np.__version__}')
print(f'scipy: {scipy.__version__}')
print(f'matplotlib: {matplotlib.__version__}')
print('Setup complete.')
"
```

You should see version numbers printed without any errors.

---

## Next Step

Once Python is installed and your environment is set up, move to:

`foundation/02_setup_claude_code_desktop.md`

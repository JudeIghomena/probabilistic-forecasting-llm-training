# Foundation Guide 06: Jupyter Notebooks

**Complete Foundation Guide 01 (Python) before this.**

---

## What Is a Jupyter Notebook?

A Jupyter notebook is a document that contains live Python code, its output,
and your written notes all in one file. Instead of running an entire script
at once, you run small blocks of code called cells one at a time and see the
result immediately below each one.

This makes notebooks ideal for:
- Exploring data before writing formal pipeline code
- Plotting distributions and checking what they look like
- Testing scoring functions on small examples before scaling up
- Keeping notes alongside your code during learning sessions

You will use notebooks extensively in Sessions 01 through 08 for exploration
and experimentation before writing the clean pipeline code.

---

## Step 1: Install Jupyter

With your virtual environment active, run:

```
pip install jupyter notebook
```

Or if you prefer the newer interface called JupyterLab (recommended):

```
pip install jupyterlab
```

Both do the same thing. JupyterLab has a better file browser and layout.

---

## Step 2: Launch Jupyter

Navigate to your project folder in the terminal and run:

```
jupyter lab
```

or for the classic interface:

```
jupyter notebook
```

Your browser will open automatically showing a file browser pointing at your
project folder. If it does not open, look at the terminal output, there will
be a URL starting with `http://localhost:8888` that you can copy and paste
into your browser.

---

## Step 3: Create Your First Notebook

In the JupyterLab interface:

1. Click the "+" button or go to File, then New, then Notebook
2. Choose your Python kernel when asked (select the one from your virtual environment)
3. A new untitled notebook opens with one empty cell

In the classic Jupyter interface:

1. Click "New" in the top right
2. Select "Python 3"

---

## Step 4: Understand the Interface

A notebook is made of cells. Each cell is either a code cell or a text cell.

**Code cells:** contain Python. Press `Shift + Enter` to run a cell. The output
appears directly below it.

**Markdown cells:** contain formatted text. Change a cell from Code to Markdown
using the dropdown in the toolbar. Press `Shift + Enter` to render it.

**The toolbar:** contains buttons to run cells, add cells, delete cells, and
save the notebook.

**The kernel:** is the Python process running your code. If something goes
wrong (infinite loop, crash), go to Kernel in the menu and click "Restart".

---

## Step 5: Try These Three Cells

Create a new notebook and run these three cells in order. This tests that
your environment is fully working.

**Cell 1:**
```python
import numpy as np
import matplotlib.pyplot as plt
print("Libraries loaded successfully")
print(f"numpy version: {np.__version__}")
```

**Cell 2:**
```python
x = np.linspace(-5, 5, 100)
y = np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)
plt.plot(x, y)
plt.title("Standard Gaussian Distribution")
plt.xlabel("x")
plt.ylabel("Density")
plt.show()
```

**Cell 3:**
```python
samples = np.random.normal(0, 1, 1000)
print(f"Mean: {samples.mean():.4f}  (expected: 0)")
print(f"Std:  {samples.std():.4f}   (expected: 1)")
```

If all three cells run without errors and the plot appears, your notebook
environment is fully working.

---

## Step 6: Save Your Notebook

Press `Ctrl + S` (or `Cmd + S` on macOS) to save. Notebooks save as `.ipynb`
files. Save your exploration notebook as:

```
Session_01_Probability_and_Uncertainty/build/exploration.ipynb
```

This keeps your exploratory work alongside the formal Python script for
the same session.

---

## Step 7: Notebooks vs Python Scripts

You will use both in this project. Here is when to use each:

| Situation | Use |
|---|---|
| Exploring a new dataset | Notebook |
| Testing a scoring function with a small example | Notebook |
| Generating a plot for the paper | Notebook |
| Writing production pipeline code | Python script (.py) |
| Running the full benchmark | Python script (.py) |
| Automating anything that runs repeatedly | Python script (.py) |

The rule of thumb: use a notebook when you are thinking and exploring,
use a script when you are building something that has to run reliably.

---

## Step 8: VS Code Has Built-In Notebook Support

If you prefer to stay inside VS Code rather than opening a browser:

1. Install the "Jupyter" extension from the VS Code Extensions panel
2. Open any `.ipynb` file in VS Code
3. It renders as an interactive notebook inside the editor
4. Select your Python interpreter the same way as for `.py` files

This means you can run notebooks without opening a browser at all.

---

## Troubleshooting

**"Kernel not found" or wrong Python version:**
The notebook may be using the system Python instead of your virtual environment.
In JupyterLab, go to Kernel, then Change Kernel, and select the correct one.
In VS Code, click the kernel name in the top right of the notebook and choose
the virtual environment interpreter.

**Plots do not appear:**
Add `%matplotlib inline` as the first line in the cell that imports matplotlib.
This tells Jupyter to display plots inside the notebook.

**Browser does not open when launching:**
Copy the URL from the terminal output (starts with `http://localhost:8888`)
and paste it into your browser manually.

---

## Next Step

Move to:

`foundation/07_claude_code_desktop.md`

(The Claude Code Desktop guide is already complete at `02_setup_claude_code_desktop.md`.)

Then proceed to:

`foundation/08_openai_api.md`

# Foundation Guide 09: Obsidian

**This is the last foundation guide. Complete it and then begin Session 01.**

---

## What Is Obsidian?

Obsidian is a free application for reading and writing Markdown files. It
renders `.md` files as clean, formatted documents with headings, tables,
bullet points, and code blocks, exactly the way they are intended to be read.

Without Obsidian (or VS Code's Markdown preview), your learn files look like
this in a plain text editor:

```
## Why Probabilistic Forecasting Matters

**Point predictions** are convenient but they throw away...
```

With Obsidian, they look like properly formatted documents with headings,
bold text, and readable tables. This makes a significant difference when you
are sitting down to read a dense session like Session 06 or 07.

Obsidian also has one feature that is particularly useful for this curriculum:
it treats a folder of Markdown files as a connected knowledge base. You can
see links between concepts and navigate between sessions without hunting through
folders.

---

## Step 1: Download and Install Obsidian

1. Go to obsidian.md in your browser
2. Click "Download" and choose your operating system
3. Install it like any other application

Obsidian is free for personal use. You do not need to create an account to use it.

---

## Step 2: Open the Project as a Vault

In Obsidian, a "vault" is just a folder. Opening a vault means telling
Obsidian to treat that folder as your Markdown workspace.

1. Open Obsidian
2. Click "Open folder as vault"
3. Navigate to your `probabilistic-forecasting-llm-training` folder
4. Click "Open" or "Select"

Obsidian will index all the `.md` files in the project. You will see them
in the left sidebar organised by folder, exactly matching the session structure.

---

## Step 3: Navigate the Curriculum

In the left sidebar, you will see the folder tree:

```
foundation/
Session_01_Probability_and_Uncertainty/
  learn/
  build/
  paper/
Session_02_Forecasting_Types/
...
```

Click any file to open and read it. Headings, tables, code blocks, and
bullet points all render correctly.

To switch between the raw Markdown source and the rendered view, look for
the reading mode toggle in the top right corner of the file (it looks like
a book icon or pencil icon).

---

## Step 4: Reading Mode vs Editing Mode

Obsidian has two modes:

**Reading mode (book icon):** Shows the rendered document. Use this when
reading learn files and paper contribution templates. Everything is clean
and formatted.

**Editing mode (pencil icon):** Shows the raw Markdown with all the symbols.
Use this when writing your paper contributions, since you need to type into
the file.

Switch between them with `Ctrl + E` (or `Cmd + E` on macOS).

---

## Step 5: Write Your Paper Contributions Here

Your paper contribution files live in `Session_XX/paper/paper_contribution.md`.
Obsidian is a good place to write them because:

- You can see the formatted output while you type (with the live preview setting)
- The spell checker catches errors
- You can have the learn file open in one tab and the paper file in another

To open two files side by side in Obsidian:
1. Hold `Ctrl` (or `Cmd`) and click a file in the sidebar
2. It opens in a new split panel

---

## Step 6: Useful Obsidian Settings to Change

These settings make Obsidian more comfortable for this project:

**Enable live preview (edit and see formatting at the same time):**
Go to Settings, then Editor, and enable "Live Preview" mode.

**Increase font size:**
Go to Settings, then Appearance, and adjust the font size slider.
The learn files are long, a comfortable reading size prevents eye strain.

**Disable the graph view:**
The graph view shows connections between notes. For this project it is
not needed and can be visually cluttered. You can ignore it or close it.

---

## What Obsidian Is Not

Obsidian is for reading and writing `.md` files. It does not:

- Run Python code (use VS Code or Jupyter for that)
- Call LLM APIs
- Replace Claude Code Desktop for coding sessions
- Edit `.py` files well (use VS Code for Python files)

Think of Obsidian as your reading room and writing desk. Everything else
happens in VS Code, Jupyter, and Claude Code Desktop.

---

## Your Complete Tool Setup

You now have all nine tools set up:

| Tool | Purpose | Used In |
|---|---|---|
| Python | Run all pipeline code | Every session |
| VS Code | Code editor, file navigator | Every session |
| Git + GitHub | Version control, backup, sharing | Every session |
| Jupyter | Exploratory code and plots | Sessions 01-08 |
| Claude Code Desktop | AI-assisted coding | Every session |
| Claude CLI + Anthropic API | LLM querying in the pipeline | Sessions 03-10 |
| OpenAI API | GPT-4o queries in the pipeline | Sessions 03-10 |
| Hugging Face + Llama | Open-source LLM queries | Sessions 03-10 |
| Obsidian | Read learn files, write paper sections | Every session |

---

## You Are Ready to Begin

All foundation setup is complete.

Open Obsidian, navigate to:

```
Session_01_Probability_and_Uncertainty/learn/session_01_learn.md
```

Read it in reading mode. Then follow the instructions at the bottom of that
file to move to the build and paper tasks.

Good luck.

# Foundation Guide 04: Setting Up VS Code

**Complete Foundation Guide 01 (Python) before this.**

---

## What Is VS Code?

VS Code (Visual Studio Code) is a free code editor made by Microsoft. It is
the most widely used editor in software development and data science.

In this project you will use VS Code for three things:

1. Reading the session learn files in a clean, formatted view
2. Editing your paper contribution files
3. Viewing and navigating the pipeline folder structure as it grows

Claude Code Desktop handles AI-assisted coding. VS Code handles everything
else, file management, markdown reading, and editing without AI assistance.
Both tools are open at the same time during every session.

---

## Step 1: Download and Install VS Code

1. Go to code.visualstudio.com in your browser
2. Click the download button for your operating system
3. Run the installer

**macOS:** Open the downloaded zip, drag VS Code to Applications, open it.

**Windows:** Run the installer. On the "Select Additional Tasks" screen,
tick "Add to PATH" and "Open with Code" context menu options, both are
useful and easy to miss.

**Linux (Ubuntu/Debian):**
```
sudo apt update
sudo apt install code
```

---

## Step 2: Open the Project Folder

1. Open VS Code
2. Click "File" in the top menu, then "Open Folder"
3. Navigate to your `PROBABILITY PIPELINE PROJECT TRAINING` folder
4. Click "Select Folder" (or "Open" on macOS)

VS Code will show the full project tree in the left sidebar. You can click
any file to open it. You will use this constantly to navigate between
learn, build, and paper files across sessions.

---

## Step 3: Install the Python Extension

VS Code becomes much more useful for Python with the official extension.

1. Click the Extensions icon in the left sidebar (it looks like four squares)
2. In the search box, type "Python"
3. Click the extension named "Python" published by Microsoft
4. Click "Install"

This extension gives you syntax highlighting, error detection as you type,
and the ability to select which Python interpreter to use.

---

## Step 4: Install the Markdown Preview Extension

Your learn files and paper contributions are all written in Markdown.
Without a preview, they look like raw text with symbols everywhere.
With preview, they render as clean, formatted documents.

The Markdown preview is built into VS Code, no extra extension needed.

To preview any Markdown file:
1. Open the file (any `.md` file)
2. Press `Cmd + Shift + V` on macOS or `Ctrl + Shift + V` on Windows/Linux
3. A rendered preview opens alongside the raw text

You can also right-click the tab of an open `.md` file and choose
"Open Preview" from the menu.

---

## Step 5: Connect VS Code to Your Python Virtual Environment

VS Code needs to know which Python to use, the one inside your virtual
environment, not the system Python.

1. Open any `.py` file in VS Code
2. Look at the bottom status bar, it shows the current Python interpreter
3. Click on it
4. A dropdown appears at the top of the screen showing available interpreters
5. Select the one that shows your virtual environment path
   (it will contain `prob_pipeline_env` in the path)

If your virtual environment does not appear, click "Enter interpreter path"
and navigate to `prob_pipeline_env/bin/python` on macOS/Linux or
`prob_pipeline_env\Scripts\python.exe` on Windows.

---

## Step 6: Install Two More Useful Extensions

**Markdown All in One**, adds a table of contents, keyboard shortcuts for
Markdown, and auto-formatting. Useful when writing paper sections.

**GitLens**, shows who changed what in every file and integrates with Git
history. Useful once you start working with the pipeline across sessions.

Install both the same way as the Python extension in Step 3.

---

## How VS Code Fits Into the Session Workflow

During each session, you will have two windows open side by side:

**Left window (VS Code):**
- Learn file open in Markdown preview, your reference while working
- Paper contribution file open for writing
- Project file tree visible in the sidebar

**Right window (Claude Code Desktop):**
- Pipeline code open
- Claude chat active for building and debugging

Switch between them as you move through the three session components.

---

## Useful Keyboard Shortcuts

| Action | macOS | Windows / Linux |
|---|---|---|
| Open a file | Cmd + P | Ctrl + P |
| Open the terminal | Ctrl + ` | Ctrl + ` |
| Preview Markdown | Cmd + Shift + V | Ctrl + Shift + V |
| Split editor | Cmd + \ | Ctrl + \ |
| Find in all files | Cmd + Shift + F | Ctrl + Shift + F |
| Toggle sidebar | Cmd + B | Ctrl + B |

---

## Next Step

Move to:

`foundation/05_git_and_github.md`

# Pylance Git Worktrees Navigation Issue Demo

This repository demonstrates the Pylance "Go to Definition" navigation issue when using git worktrees, as reported in [microsoft/pylance-release#7642](https://github.com/microsoft/pylance-release/issues/7642).

## Problem

When working with git worktrees, Pylance's "Go to Definition" (Ctrl+Click or F12) incorrectly navigates to function definitions in the **wrong worktree** instead of the current one.

## Repository Structure

```
pylance-worktree-demo/
├── demo_package/
│   ├── core/
│   │   ├── config.py
│   │   └── logger.py
│   ├── algo/
│   │   ├── processor.py    # Imports core
│   │   └── analyzer.py     # Imports processor + core
│   └── api/
│       └── endpoints.py    # Imports algo + core
└── worktrees/              # Worktrees nested inside main repo
    ├── feature-a/          # Modified processor.py (3x multiplier)
    └── feature-b/          # Modified logger.py (added timestamps)
```

## Reproducing the Issue

```bash
# 1. Clone and set up worktree
git clone https://github.com/yonichechik/pylance-worktree-demo.git
cd pylance-worktree-demo
git worktree add worktrees/feature-a feature-a

# 2. Open worktree in VSCode
code worktrees/feature-a
```

**3. Test navigation:**
- Open `demo_package/algo/analyzer.py`
- Line 7: Ctrl+Click on `process_data`
- Check the opened file's implementation

**Expected:** Opens `worktrees/feature-a/.../processor.py` (multiply by **3**)
**Actual:** Opens main repo `processor.py` (multiply by **2**)

This proves Pylance ignores workspace boundaries and resolves to the main repo instead of the current worktree.

## Environment

- Python 3.13+
- VSCode + Pylance (latest)
- Worktrees nested inside main repository
- editable install (`pip install -e .`)

## Related

[microsoft/pylance-release#7642](https://github.com/microsoft/pylance-release/issues/7642)

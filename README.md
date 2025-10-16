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

## Setup to Reproduce

### 1. Clone Repository
```bash
git clone https://github.com/yonichechik/pylance-worktree-demo.git
cd pylance-worktree-demo
```

### 2. Worktrees Already Exist
The worktrees are **already created** at `worktrees/feature-a` and `worktrees/feature-b`. This matches the exact structure we use in production.

Verify with:
```bash
git worktree list
```

### 3. Open in VSCode
```bash
# Open main repository
code .

# OR open a specific worktree
code worktrees/feature-a
```

## Reproducing the Issue

### Quick Test
1. Open `demo_package/api/endpoints.py`
2. Ctrl+Click on `log_info` (line 6)
3. **Expected**: Navigate to `log_info` definition in the **current** worktree
4. **Actual**: May navigate to `log_info` in a **different** worktree (e.g., feature-b which has timestamps)

### What Should Happen
When working in `worktrees/feature-a/`, clicking on `log_info` should navigate to:
```
worktrees/feature-a/demo_package/core/logger.py
```

### What Actually Happens
Pylance may navigate to:
- `demo_package/core/logger.py` (main repo)
- `worktrees/feature-b/demo_package/core/logger.py` (wrong worktree!)

The navigation is **non-deterministic** and **ignores workspace boundaries**.

## Differences Between Worktrees

To see the issue clearly:

**Main branch** - `processor.py`: multiplies by 2
**Feature-a** - `processor.py`: multiplies by 3
**Feature-b** - `logger.py`: adds timestamps to all log functions

When navigating, you'll see different implementations depending on which worktree Pylance chose (incorrectly).

## Environment

- Python 3.13+
- VSCode + Pylance (latest)
- Worktrees nested inside main repository
- editable install (`pip install -e .`)

## Related

[microsoft/pylance-release#7642](https://github.com/microsoft/pylance-release/issues/7642)

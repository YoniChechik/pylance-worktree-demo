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

### 2. Set Up Worktree
The branches exist remotely. Create the worktree structure locally (matches our production setup):

```bash
# Create worktree for feature-a inside the main repo
git worktree add worktrees/feature-a feature-a

# Verify it's set up correctly
git worktree list
```

### 3. Open Worktree in VSCode
```bash
# Open the feature-a worktree (NOT the main repo)
code worktrees/feature-a
```

## Reproducing the Issue

### Quick Test
1. In the worktree, open `demo_package/algo/analyzer.py`
2. Find line 7: `processed = process_data(data)`
3. Ctrl+Click (or F12) on `process_data`
4. **Expected**: Navigate to `process_data` in `worktrees/feature-a/demo_package/algo/processor.py` (which multiplies by 3)
5. **Actual**: Navigates to `demo_package/algo/processor.py` in the **main repo** (which multiplies by 2)

### What Should Happen
When working in `worktrees/feature-a/`, clicking on `process_data` should navigate to:
```
worktrees/feature-a/demo_package/algo/processor.py
```
Where the implementation multiplies by **3**.

### What Actually Happens
Pylance navigates to the **main repository**:
```
demo_package/algo/processor.py
```
Where the implementation multiplies by **2**.

This proves Pylance is **ignoring workspace boundaries** and resolving symbols from the main repo instead of the current worktree.

## Key Difference to Spot the Bug

**Main branch** - `processor.py`: multiplies by 2
**Feature-a** - `processor.py`: multiplies by 3

When you navigate to `process_data`, check the implementation to see which version Pylance opened. If you're working in feature-a but see "multiply by 2", Pylance opened the wrong file.

## Environment

- Python 3.13+
- VSCode + Pylance (latest)
- Worktrees nested inside main repository
- editable install (`pip install -e .`)

## Related

[microsoft/pylance-release#7642](https://github.com/microsoft/pylance-release/issues/7642)

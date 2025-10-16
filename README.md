# Pylance Git Worktrees Navigation Issue Demo

This repository demonstrates the Pylance "Go to Definition" navigation issue when using git worktrees, as reported in [microsoft/pylance-release#7642](https://github.com/microsoft/pylance-release/issues/7642).

## Problem Description

When working with git worktrees, Pylance's "Go to Definition" feature (Ctrl+Click or F12) incorrectly navigates to function definitions in the wrong worktree instead of the current one.

### Key Symptoms

- **Intermittent behavior**: Sometimes navigates correctly, sometimes to wrong worktree
- **Cross-worktree jumping**: When working in one worktree, definitions resolve to another worktree or the main repository
- **Scope violation**: Pylance fails to respect workspace folder boundaries during symbol resolution

## Repository Structure

This demo follows a common Python project pattern with worktrees nested inside the main repository:

```
pylance-worktree-demo/
├── demo_package/           # Main package
│   ├── core/              # Core utilities
│   │   ├── config.py      # Configuration (imported by algo)
│   │   └── logger.py      # Logging (imported by algo and api)
│   ├── algo/              # Algorithms
│   │   ├── processor.py   # Data processing (imports core)
│   │   └── analyzer.py    # Data analysis (imports processor + core)
│   └── api/               # API layer
│       └── endpoints.py   # API endpoints (imports algo + core)
├── worktrees/             # Worktrees directory
│   ├── feature-a/         # Feature A worktree
│   └── feature-b/         # Feature B worktree
├── pyproject.toml         # Project configuration
└── .vscode/settings.json  # VSCode settings
```

### Module Dependencies

The package structure demonstrates typical cross-module imports:

- `api/endpoints.py` → imports from `algo/` and `core/`
- `algo/analyzer.py` → imports from `algo/processor.py` and `core/`
- `algo/processor.py` → imports from `core/`

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yonichechik/pylance-worktree-demo.git
cd pylance-worktree-demo
```

### 2. Install Dependencies

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

### 3. Create Worktrees

The repository includes pre-created worktrees, but you can create new ones:

```bash
# Create a new worktree for a feature
git worktree add worktrees/my-feature -b my-feature

# List all worktrees
git worktree list
```

## Reproducing the Issue

### Method 1: Open Main Repository

1. Open the main repository root in VS Code:
   ```bash
   code /path/to/pylance-worktree-demo
   ```

2. Open `demo_package/api/endpoints.py`

3. Try "Go to Definition" (Ctrl+Click or F12) on these imports:
   - `analyze_data` (line 3)
   - `process_data` (line 4)
   - `load_config` (line 5)
   - `log_info` (line 6)

4. **Expected**: Should navigate to definitions in main repository
5. **Actual**: May navigate to definitions in `worktrees/feature-a/` or `worktrees/feature-b/`

### Method 2: Open Worktree

1. Open a specific worktree in VS Code:
   ```bash
   code /path/to/pylance-worktree-demo/worktrees/feature-a
   ```

2. Open `demo_package/api/endpoints.py` in the worktree

3. Try "Go to Definition" on the same imports as above

4. **Expected**: Should navigate to definitions within the same worktree
5. **Actual**: May navigate to:
   - Definitions in the main repository
   - Definitions in a different worktree (`feature-b`)

### Method 3: Multi-root Workspace

1. Create a VS Code workspace with both locations:
   ```json
   {
     "folders": [
       {"path": "/path/to/pylance-worktree-demo"},
       {"path": "/path/to/pylance-worktree-demo/worktrees/feature-a"}
     ]
   }
   ```

2. Navigate between files in different workspace folders

3. Observe that "Go to Definition" often jumps to the wrong workspace folder

## Expected Behavior

When working in a specific worktree (or the main repository), "Go to Definition" should:

1. **Respect workspace boundaries**: Always navigate to files within the current workspace folder
2. **Consistent navigation**: Always navigate to the same location for the same symbol
3. **Isolated symbol resolution**: Treat each worktree as an independent environment

## Actual Behavior

Pylance appears to:

1. **Index all worktrees simultaneously**: Creates a global symbol index across all worktrees
2. **Non-deterministic navigation**: Randomly picks a worktree when multiple definitions exist
3. **Ignore workspace scope**: Fails to filter symbol resolution by workspace folder

## Environment

- **Python**: 3.13+
- **VSCode**: Latest
- **Pylance**: Latest
- **Package Manager**: uv (or pip)
- **Build System**: Hatchling
- **Worktree Structure**: Nested inside main repository (at `worktrees/`)

## Additional Context

This issue is particularly problematic in development workflows where:

- Multiple features are developed in parallel using worktrees
- Developers frequently switch between worktrees
- Code navigation is critical for understanding cross-module dependencies

## Workarounds

Current workarounds (all unsatisfactory):

1. **Avoid worktrees**: Use branches instead (loses worktree benefits)
2. **One VSCode window per worktree**: Memory-intensive, awkward workflow
3. **Manual navigation**: Use file explorer instead of "Go to Definition" (slow)

## Related Issues

- [microsoft/pylance-release#7642](https://github.com/microsoft/pylance-release/issues/7642) - Original issue report

## Contributing

If you have additional insights or workarounds, please open an issue or pull request!

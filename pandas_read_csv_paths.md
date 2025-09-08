## Portable ways to load a local CSV with pandas

### Short answer
- **Prefer `pathlib.Path`** and use **relative paths** inside your project (e.g., `data/myfile.csv`).
- **Avoid `os.chdir()`** in shared code; use only interactively if necessary.
- **Anchor paths**: in scripts, anchor to the script location; in notebooks, anchor to a project root marker or a known folder.

### Reliable patterns

- **Scripts (anchored to the script’s folder)**
```python
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parent / "data" / "myfile.csv"
df = pd.read_csv(DATA_PATH)
```

- **Notebooks (anchor to a project root that contains `data/`)**
```python
from pathlib import Path
import pandas as pd

# Find the nearest parent that has a "data" folder (or use .git/pyproject.toml as markers)
project_root = next((p for p in [Path.cwd(), *Path.cwd().parents] if (p / "data").exists()), Path.cwd())
csv_path = project_root / "data" / "myfile.csv"
df = pd.read_csv(csv_path)
```

- **Pure relative path** (works if you run code from the project root)
```python
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path("data") / "myfile.csv")
```

- **Optional: environment variable for data directory** (robust in varied setups)
```python
import os
from pathlib import Path
import pandas as pd

DATA_DIR = Path(os.getenv("DATA_DIR", "data"))
df = pd.read_csv(DATA_DIR / "myfile.csv")
```

- **Optional: interactive file picker** (good for workshops)
```python
from tkinter.filedialog import askopenfilename
import pandas as pd

path = askopenfilename(title="Select CSV", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
df = pd.read_csv(path)
```

### Practical tips
- **Organize data** under a `data/` folder at the project root.
- **Use `pathlib.Path`** for cross-platform paths; avoid manual string paths.
- **Don’t rely on CWD** being “correct.” Always compute paths, don’t assume.
- **If you must change directories** in a notebook for a demo, use `%cd <path>` interactively rather than hard-coding `os.chdir()` in reusable code.

### Rules of thumb
- **Scripts**: use `Path(__file__).parent` to build paths.
- **Notebooks**: dynamically discover the project root (e.g., nearest folder containing `data/`, `.git`, or `pyproject.toml`) and build paths from there.

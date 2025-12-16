from pathlib import Path
import json

p = Path('/Users/ginuram/Desktop/Dekstop/30DAYSOFPYTHON/MINI_PROJECTS/to_do_CLI')
task_file = p / "todo.json"

def load_tasks() -> list[dict]:
    if not task_file.exists():
        return []
    with task_file.open("r") as f:
        return(json.load(f))

def save_tasks(tasks) -> None:
    task_file.parent.mkdir(parents=True, exist_ok=True)
    with task_file.open("w") as f:
        json.dump(tasks, f, indent=2)

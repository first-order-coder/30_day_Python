import json
from pathlib import Path
import sys

p = Path('/Users/ginuram/Desktop/Dekstop/30DAYSOFPYTHON/MINI_PROJECTS/to_do_CLI')
task_file = p / "all_in_one.json"

tasks = []
if task_file.exists():
    with task_file.open("r") as f:
        tasks = json.load(f)
else:
    tasks = []

def add_task(tasks):
    user_given_task = ' '.join(sys.argv[1::])
    tasks.append({"id":len(tasks)+1,"task":user_given_task, "status":False})
    with task_file.open("w") as f:
        json.dump(tasks, f, indent=2)

def load_tasks(tasks):
    with task_file.open("r") as f:
        tasks = json.load(f)
        return tasks
        
print(load_tasks(tasks)[0])
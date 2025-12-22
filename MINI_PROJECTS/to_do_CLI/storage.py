import json
from pathlib import Path
import sys
from art import *

#pip install art

p = Path('/Users/ginuram/Desktop/Dekstop/30DAYSOFPYTHON/MINI_PROJECTS/to_do_CLI')
task_file = p / "all_in_one.json"

def read_tasks():
    if not task_file.exists() or task_file.stat().st_size == 0:
        task_file.parent.mkdir(parents=True, exist_ok=True)
        with task_file.open("w") as f:
            json.dump([], f) #if read --> load if write --> dump 
        return []
        
    elif task_file.exists() or task_file.stat().st_size != 0:
        with task_file.open("r") as f:
            return(json.load(f))

def write_tasks(tasks):
    task_file.parent.mkdir(parents=True, exist_ok=True)
    with task_file.open("w") as f:
        json.dump(tasks, f, indent=2)
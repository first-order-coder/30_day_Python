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

"<--- Working with sys.argv--->"
# def system_logic(tasks):
#     if (sys.argv[1] == "add"):
#         add_task(tasks)
#     elif (sys.argv[1] == "load"):
#         load_tasks(tasks)
# system_logic(tasks)

# def add_task(tasks):
    # user_given_task = ' '.join(sys.argv[2::])
    # tasks.append({"id":len(tasks)+1,"task":user_given_task, "status":False})
    # with task_file.open("w") as f:
    #     json.dump(tasks, f, indent=2)

def add_task(user_given_task):
    tasks.append({"id":len(tasks)+1,"task":user_given_task, "status":False})
    with task_file.open("w") as f:
        json.dump(tasks, f, indent=2)

def load_tasks(tasks):
    with task_file.open("r") as f:
        tasks = json.load(f)
        for task in tasks:
            print(task)

ops_lst = ["ADD", "LOAD"]
def working_with_menu():
    user_input = input("Enter operation:")
    if (int(user_input) == 1):
        add_task_input = input("Selected ADD Enter Your operation:")
        add_task(add_task_input)

    elif (int(user_input) == 2):
        print("Selected LOAD and Your tasks are:\n")
        load_tasks(tasks)
working_with_menu()
import json
from pathlib import Path
import sys
from art import *

p = Path('/Users/ginuram/Desktop/Dekstop/30DAYSOFPYTHON/MINI_PROJECTS/to_do_CLI')
task_file = p / "all_in_one.json"

def read_tasks():
    if task_file.exists() or task_file.stat().st_size == 0:
        return []
    
    with task_file.open("r") as f:
        return(json.load(f))

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

def write_tasks(tasks):
    task_file.parent.mkdir(parents=True, exist_ok=True)
    with task_file.open("w") as f:
        json.dump(tasks, f, indent=2)

def load_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        if task.get("status"):
            mark = "✔" 
        else:
            mark = ""
        print(f"[{mark} {task["id"]}: {task["task"]}]")

def add_task(tasks):
    tprint("ADD TASK", "mini")
    text = input("Task: ").strip()
    if not text: #if text string is empty then it would return false (basically this means if not fals == if true)
        print("Task cannot be empty.")
        return tasks
    tasks.append({"id": len(tasks) + 1, "task": text, "status": False})

ops_lst = ["ADD TASK", "LOAD TASK", "UPDATE TASK", "REMOVE TASK", "QUIT"]
def operation_list(ops):
    print("-"*115)
    tprint("SELECT OPERATION", "graffiti-tiny")
    print("-"*115)
    print("")

    for i,e in enumerate(ops):
        print(i+1,e)
    print("")

def working_with_menu():
    operation_list(ops_lst)
    user_input = input("Enter operation:")
    if (int(user_input) == 1):
        tprint("ADD TASK", "mini")
        add_task_input = input("Task:")
        add_task(add_task_input)
        tprint("Task added Sucessfully\n", "tiny")
    elif (int(user_input) == 2):
        print("------------------------ Your tasks are -------------------------------------------------\n")
        load_tasks(tasks)
    elif (int(user_input) == 3):
        print("Selected LOAD and Your tasks are:\n")
        load_tasks(tasks)
    elif (int(user_input) == 4):
        print("Selected LOAD and Your tasks are:\n")
        load_tasks(tasks)
    elif (int(user_input) == 5):
        # return False
        tprint("Good bye!", "small")
        sys.exit() #we can use either of them 

while True:
    working_with_menu()

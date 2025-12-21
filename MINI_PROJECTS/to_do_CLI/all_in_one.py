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
        if (task.get("status")): #if this is True print this
            mark = "✔" 
        else:
            mark = "X"
        print(mark, task["id"], task["task"])

def add_task(tasks):
    tprint("ADD TASK", "mini")
    text = input("Task: ").strip()
    if not text: #if text string is empty then it would return false (basically this means not false == if true)
        print("Task cannot be empty.")
        return tasks
    
    biggest = 0
    for t in tasks:
        if t["id"] > biggest:
            biggest = t["id"]
    new_id = biggest + 1

    tasks.append({"id": new_id, "task": text, "status": False})
    write_tasks(tasks)
    tprint("Saved", "tiny")
    return tasks

def find_task_by_id(tasks, task_id): 
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None
        
def parse_status(s):
    s = s.strip().casefold()
    true_set = {"done", "d", "true", "1"}
    false_set = {"not done", "not", "n", "false", "0"}

    if s in true_set:
        return True
    elif s in false_set:
        return False
    return None

def update_task(tasks):
    tprint("UPDATE TASK", "mini")
    
    user_given_id = input("Enter the Task ID want to change:")
    try:
        task_id = int(user_given_id)
    except ValueError:
        print("Invalid Input. Please enter a number.")
        return tasks

    task = find_task_by_id(tasks, task_id)
    if task is None:
        print(f"No task found with id={task_id}.")
        return tasks

    print("Selected Task:", task["id"], task["task"], task.get("status"))  #problem with using task[user_given_id - 1] the index way is that when we remove a task the indexing method will go wrong.
    
    while True:
        raw_status = input("Enter the new status (Done / Not Done):")
        new_status = parse_status(raw_status)
    
        # new_status = raw_status.lower().startswith("done") #if it starts with done then new status is True (bool)
        if new_status is None:
            print("Please type: Done / Not Done")
            continue    
        task["status"] = new_status
        break
    write_tasks(tasks)
    print("Updated Successfully.")
    return tasks

def remove_tasks(tasks):
    user_given_id = input("Enter the id you want to remove: ")
    try:
        task_id = int(user_given_id)
    except ValueError:
        print("Please enter a valid digit")
        return tasks

    task = find_task_by_id(tasks, task_id)
    if task is None:
        print(f"Task is not found with id={task_id}")
        return tasks
    
    tasks.remove(task)

    write_tasks(tasks)
    print("Updated Successfully.")
    return tasks



ops_lst = ["ADD TASK", "LOAD TASK", "UPDATE TASK", "REMOVE TASK", "QUIT"]
def menu():
    print("-"*115)
    tprint("SELECT OPERATION", "graffiti-tiny")
    print("-"*115)
    print("")
    for i,e in enumerate(ops_lst):
        print(i+1,e)
    print()

def main():
    tasks = read_tasks()
    
    while True:
        menu()
        user_input = input("Enter operation:").strip()
        if not user_input.isdigit():
            print("Please enter a number 1-5. \n")
            continue
        user_input = int(user_input)

        if (user_input == 1):
            tasks = add_task(tasks)
        elif (user_input == 2):
            print("Your tasks:\n")
            load_tasks(tasks)
        elif (int(user_input) == 3):
            print("Selected UPDATE and Your tasks are:\n")
            update_task(tasks)
        elif (int(user_input) == 4):
            print("Selected Remove and Your tasks are:\n")
            remove_tasks(tasks)
        elif (int(user_input) == 5):
            # return False
            tprint("Good bye!", "small")
            break
        else:
            print("Choose a number 1-5.\n")

if __name__ == "__main__":
    main()

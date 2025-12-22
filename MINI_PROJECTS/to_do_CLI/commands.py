import json
from pathlib import Path
import sys
from art import *

#pip install art

from storage import write_tasks

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
    
    # this handles the task id getting the correct one even if some tasks were removed.
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


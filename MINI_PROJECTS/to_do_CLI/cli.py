import json
from pathlib import Path
import sys
from art import *

#pip install art

from storage import read_tasks
from commands import add_task, load_tasks, update_task, remove_tasks


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

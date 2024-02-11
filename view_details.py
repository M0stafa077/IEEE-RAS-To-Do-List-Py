"""
    A ptyhon script file contains the operations done on tasks :
        - Create a new Task. (DONE)
        - Add new tasks to the json file. (DONE)
        - Remove tasks from the json file.
"""

import json
from tabulate import tabulate
import datetime

# --------------- Opening and reading from the json file --------------- #
try :
    with open("Tasks.json", "r") as jsonFile:
        tasks:dict = json.load(jsonFile)
except :
    print("An error occured while oppeneing the file!!")

# --------------- Section : Software Interfaces --------------- #
    
# --------------- A Software Interfaces Creates A new Task object --------------- #
def create_task(task_name:str, task_due_data:datetime.datetime, priority:bool = False, details:str = "") -> dict:
    """ 
        A function Creates A new Task object
        @param task_name : A string contains the name of the task.
        @param task_due_data : A datetime object contains the due date of the task.
        @param priority : A bool object specifies if the task has priority over other tasks or not. (False by default)
        @param details : A string contains the details of the task. (Empty by default)
        @returns : A dictionary of the new task created.
    """
    new_task = {}                       # Define a new dictionary for the task to be created.
    new_task["task_number"] = 0
    try :
        new_task["task_name"] = task_name   # Define the name of the task.
    except :
        print("Name is not specified")
        return {}
    try :
        # Define the due date of the task.
        new_task["due_date"] = str(task_due_data.strftime("%a")) + ", " +  str(task_due_data.date()) 
    except :
        print("Due-date is not specified")
        return {}
    new_task["priority"] = str(priority)    # Define the priority of the task. 
    new_task["details"] = details           # Defin the details of the task. 
    return new_task                         # Return the created task.

# --------------- A Software Interfaces adds a new task to the json file --------------- #
def add_task(task:dict) -> bool :
    """
        A function adds a new task to the json file
        @param task : A dictionary contains all the required data about the task.
        @returns : A boolean object identefies if the tasks is added successfully (Take Action if Not).
    """
    task["task_number"] = len(tasks["Tasks"]) + 1

    tasks["Tasks"].append(task)     # Append the new tasks to the Tasks list in the json file
    try :
        with open("Tasks.json", "w") as jsonFile:       # Open the json file for writing
            json.dump(tasks, jsonFile, indent=4)        # Commit the changes to the json file
    except :    
        return False                                    # Return Flase if an error occured (Take Action)!!
    return True

# --------------- A Software Interfaces removes a task from the json file --------------- #
def remove_task(removed_task:dict) -> bool:
    """
        A function deletes a specific task from the json file
        @param task : A dictionary contains all the required data about the task.
        @returns : A boolean object identefies if the tasks removed successfully (Take Action if Not).
    """
    tasks["Tasks"].remove(removed_task)             # Removes the tasks from the Tasks list in the json file
    try :
        with open("Tasks.json", "w") as jsonFile:       # Open the json file for writing
            json.dump(tasks, jsonFile, indent=4)        # Commit the changes to the json file
    except :    
        return False                                    # Return Flase if an error occured (Take Action)!!
    return True


# --------------- A Software Interface displays the tasks from the json file --------------- #
def view_details(task_index):
    """
    A function to view details of a specific task.
    @param task_index: Index of the task in the list of tasks.
    @returns: None
    """
    if 0 <= task_index < len(tasks["Tasks"]):
        task = tasks["Tasks"][task_index]
        print("\nTask Details:")
        print(f"Task Name: {task['task_name']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Priority: {'High' if task['priority'] else 'Low'}")
        print(f"Details: {task['details']}")
    else:
        print("Invalid task index.")
    task_index = int(input("Enter the index of the task to view details: ")) - 1
    view_details(task_index)
# from task_operations import *

# # --------------- Creating and adding a new task object --------------- #
# task_temp = create_task("IEEE_Project", datetime.datetime(2024, 2, 11), True)
# ret = add_task(task_temp)

# # --------------- Opening and reading from the json file --------------- #
# with open("Tasks.json", "r") as jsonFile:
#     new_tasks:dict = json.load(jsonFile)

# --------------- Printing The content of the json file --------------- #
# print("============= :: ADDING THE TASK :: ============= ")
# print(tabulate(new_tasks))




# if u don't have tabulate, just use :
# print(new_tasks)


# print("============= :: REMOVING THE TASK :: ============= ")
# ret = remove_task(task_temp)
# with open("Tasks.json", "r") as jsonFile:
#     new_tasks:dict = json.load(jsonFile)
# print(tabulate(new_tasks))

# task_index = int(input("Enter the index of the task to view details: ")) - 1
# view_details(task_index)

# ================================================================================== #

def view_tasks() :
    with open("Tasks.json", "r") as jsonFile:
        file:dict = json.load(jsonFile)

    tasks:list = file["Tasks"]

    print('Task Number,', "Task Name,", 'Task Due-date')
    for task in tasks : 
        print(str(task["task_number"]) + '- ' + task["task_name"], task["due_date"], '\n')

view_tasks()
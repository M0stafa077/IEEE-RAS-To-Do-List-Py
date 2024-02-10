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
    try :
        new_task["task_name"] = task_name   # Define the name of the task.
    except :
        print("Name is not specified")
        return {}
    try :
        # Define the due date of the task.
        new_task["due_date"] = str(task_due_data.strftime("%a")) + ", " +  str(task_due_data.date()) 
    except :
        print("Name is not specified")
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
    tasks["Tasks"].append(task)     # Append the new tasks to the Tasks list in the json file
    try :
        with open("Tasks.json", "w") as jsonFile:       # Open the json file for writing
            json.dump(tasks, jsonFile, indent=4)        # Commit the changes to the json file
    except :    
        return False                                    # Return Flase if an error occured (Take Action)!!
    return True

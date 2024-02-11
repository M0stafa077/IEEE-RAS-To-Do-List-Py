"""
    A ptyhon script file contains the operations done on tasks :
        - Create a new Task. (DONE)
        - Add new tasks to the json file. (DONE)
        - Remove tasks from the json file. (DONE)
        - Display all the tasks in the json file. (DONE)
        - Marks a task as completed. (DONE)
        - Calculates the time left for a task deadline (DONE)
        - 
"""
import json
# from tabulate import tabulate
import datetime
from Utilities import *
import Utilities

# --------------- Opening and reading from the json file --------------- #
try :
    with open("Tasks.json", "r") as jsonFile:
        tasks:dict = json.load(jsonFile)
except :
    print("An error occured while oppeneing the file!!")

# --------------- Section : Software Interfaces --------------- #
    
# --------------- A Software Interfaces Creates A new Task object --------------- #
def create_task() -> dict:
    """ 
        A function Creates A new Task object
    """
    new_task = {}          # Define a new dictionary for the task to be created.

    # First. Get the task attributes from user #
    task_name = get_task_name()        # Get The task name from user
    
    task_due_data = get_task_due_date() # Get The task due-date from user
    
    priority = get_task_priority()      # Get The task priority from user

    details = input("Enetr the task details")   # Get The task details from user
    
    completed = False

    task_number = len(tasks["Tasks"]) + 1 

    # Second. Save the attributes into the task object #
    new_task["task_number"] = task_number
    try :
        new_task["task_name"] = task_name   # Define the name of the task.
    except :
        print("Name is not specified")
        return {}
    try :
        # Define the due date of the task. 
        new_task["due_date"] =   str(task_due_data.date()) +","+str(task_due_data.time())

    except :
        print("Due-date is not specified")
        return {}
    new_task["priority"] = str(priority)    # Define the priority of the task. 
    new_task["details"] = details           # Defin the details of the task. 
    new_task["completed"] = str(completed)
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

# --------------- A Software Interfaces removes a task from the json file --------------- #
def remove_task(removed_task:dict) -> bool:
    """
        A function deletes a specific task from the json file
        @param task : A dictionary contains all the required data about the task.
        @returns : A boolean object identefies if the tasks removed successfully (Take Action if Not).
    """
    tasks["Tasks"].remove(removed_task)             # Removes the tasks from the Tasks list in the json file

    for task in tasks["Tasks"] :
        task["task_number"] -= 1

    try :
        with open("Tasks.json", "w") as jsonFile:       # Open the json file for writing
            json.dump(tasks, jsonFile, indent=4)        # Commit the changes to the json file
    except :
        return False                                    # Return Flase if an error occured (Take Action)!!
    return True

# --------------- A Software Interfaces view all tasks in the json file --------------- #
def view_tasks():
    with open("Tasks.json", "r") as jsonFile:
        file:dict = json.load(jsonFile)

    tasks:list = file["Tasks"]
    if tasks:

        print("number,""     Task Name,      ,", "Task Due-date,", '   priority,   ', 'Completed')
        print("                    --------------------                 ")
        
        for task in tasks:
            status:chr
            if task["completed"] == 'True':
                status = "✔"
            else:
                status = "❌"
            print("  " + str(task["task_number"]) + '  |     ' + task["task_name"] + "   |", end="")
            print('    ' + task["due_date"] + '  |  ' + '   ' + task["priority"], '   |  ', status, '\n')
            
            
    else:
        print("no tasks to view")
        return
    
# --------------- A Software Interfaces marks a task as completed --------------- #
def complete_task():
    try:
        with open("Tasks.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Tasks file not found")
        return []

    task_number = int(input("Enter the number of the task to mark as completed: "))

    if task_number > 0 and task_number <= len(data["Tasks"]):
        data["Tasks"][task_number - 1]["completed"] = "True"
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

    with open("Tasks.json", "w", indent=4) as file:
        json.dump(data, file)

# --------------- A Software Interface prints the time left for a task deadline --------------- #
def due_date():
    task_number = get_task_number()

    while True :
        if len(tasks["Tasks"]) < task_number :
            print("Invalid task number please try again")
        else :
            _task = tasks["Tasks"][task_number - 1]
        
            task_date = _task['due_date'] 
            target_date = datetime.strptime(task_date,'%Y-%m-%d,%H:%M:%S')   # transmit date from string into opject
            today_date = datetime.now()      # the date of today
            date_diff = target_date - today_date           #the deadline in days, time form  
            print("the remaining time for the task is ", date_diff, "hour")
            break
    
# --------------- A Software Interface views the details of a task --------------- #
def view_details(task_index):
    """
    A function to view details of a specific task.
    @param task_index: Index of the task in the list of tasks.
    @returns: None
    """
    if 0 <= task_index < len(tasks["Tasks"]):
        task = tasks["Tasks"][task_index]
        print("Task Details:")
        print(f"Task Name: {task['task_name']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Priority: {'High' if task['priority'] else 'Low'}")
        print(f"Details: {task['details']}")
    else:
        print("Invalid task index.")

# --------------- A Software Interface views the tasks based on their priority --------------- #
def sort_priority_level():
   sorted_tasks = tasks["Tasks"]
   for i in range(len(sorted_tasks)):
       for j in range(i + 1, len(sorted_tasks)):
           x = sorted_tasks[i]["priority"]
           y = sorted_tasks[j]["priority"]
           if y > x:
              sorted_tasks[i], sorted_tasks[j] = sorted_tasks[j], sorted_tasks[i]
              
       ## view tasks after sorting by priority level
   print("number,""     Task Name,      ,", "Task Due-date,", '   priority,   ', 'Completed')
   print("                    --------------------                 ")
   for sorted_task in sorted_tasks:
               status:chr
               if sorted_task["completed"] == 'True':
                   status = "✔"
               else:
                   status = "❌"
               print("  " + str(sorted_task["task_number"]) + '  |     ' + sorted_task["task_name"] + "   |", end="")
               print('    ' + sorted_task["due_date"] + '  |  ' + '   ' + sorted_task["priority"], '   |  ', status, '\n')
                
from task_operations import *

# --------------- Creating and adding a new task object --------------- #
task_temp = create_task("IEEE_Project", datetime.datetime(2024, 2, 11), True)
ret = add_task(task_temp)

# --------------- Opening and reading from the json file --------------- #
with open("Tasks.json", "r") as jsonFile:
    new_tasks:dict = json.load(jsonFile)

# --------------- Printing The content of the json file --------------- #
print("============= :: ADDING THE TASK :: ============= ")
print(tabulate(new_tasks))
# if u don't have tabulate, just use :
# print(new_tasks)


print("============= :: REMOVING THE TASK :: ============= ")
ret = remove_task(task_temp)
with open("Tasks.json", "r") as jsonFile:
    new_tasks:dict = json.load(jsonFile)
print(tabulate(new_tasks))

# ================================================= #
def complete_task(task:dict) -> bool :
    with open("Tasks.json", "r") as jsonFile:
        tasks:dict = json.load(jsonFile)

    for it_task in tasks["Tasks"] :
        if task["task_name"] == it_task["task_name"] :
            it_task["completed"] = True
            return True
        else :
            continue

    return False

# ================================================= #
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

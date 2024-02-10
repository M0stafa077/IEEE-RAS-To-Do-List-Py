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
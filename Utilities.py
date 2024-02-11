from datetime import datetime
import json

def get_task_name() -> str :
    return input("Enter the task name: ")

def get_task_due_date() :

    while True:
        date=input ("date is(yyyy-mm-dd,hh:mm:ss):")
        if date.isalpha :
            date_form = datetime.strptime(date,'%Y-%m-%d,%H:%M:%S')
            return date_form
        else:
            print("please, try again!")
            continue

def get_task_priority() -> bool:
    while True :                                    # Ask the user if he want to give this task priority
        print("Do you want to prioritize this task ?")
        temp_choice = input("y or n ?")
        if ('y' == temp_choice) or ('n' == temp_choice) or ('Y' == temp_choice) or ('N' == temp_choice):
            break
        else :
            print('Invalid Input, Please Try again')
            continue

    match temp_choice :
        case 'y' :
            priority = True
        case 'Y' :
            priority = True
        case 'n' :
            priority = False
        case 'N' :
            priority = False
        case _:
            priority = False

    return priority

def get_task_number() :
    while True :
        try :
            task_number = int(input('Enter the task number: '))
            return task_number
        except :
            print("Invalid Input, Please try again ")
            continue

def get_task(task_number) -> dict:
    try:
        with open("Tasks.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Tasks file not found")
        return []
    
    if task_number > 0 and task_number < len(data["Tasks"]):
        return data["Tasks"][task_number-1]
    else:
        print("Invalid task number!")
        return {}


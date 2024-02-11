from task_operations import *
import os, time

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def header_msg() :
    print("|------------------------------------------------|")
    print("|------------ To-do-list Application ------------|")
    print("|------------------------------------------------|")

def choices_msg() :
    print('Chose what you want to do :')
    print('1- New Task.\t\t\t2- Remove Task.')
    print('3- Complete Task\t\t\t4- Due-date of a task')
    print('5- View details of a task.\t\t6- Prioritize Tasks.')

def get_choice() -> int:
    while True :
        try :
            choices_msg()
            choice = int(input())
            if (0 < choice ) and (7 >= choice) :
                return choice
            else :
                print('Invalid Input, Please try again')
        except :
            print('Invalid Input, Please try again')

if __name__ == "__main__":
    while True :
        clear_screen()
        header_msg()
        view_tasks()
        choice = get_choice()
        match choice :                
            case 1 :
                new_task = create_task()
                add_task(new_task)
                print('Task is added successfully')
            case 2 :
                task_number = get_task_number()
                removed_task = get_task(task_number)
                remove_task(removed_task)
                print('Task is removed successfully')
            case 3 :
                complete_task()
            case 4 :
                due_date()
            case 5:
                task_number = get_task_number()
                view_details(task_number - 1)
            case 6 :
                sort_priority_level()    
        

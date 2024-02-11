def priority_level ():
    try:
        with open("tasks.json", "r") as jsonfile:
            file:dict=json.load(jsonfile)
    except :
        print ("An error occured while oppening the file!!")
    tasks:list=file["Tasks"]
    priority= input("Enter priority level for the task (True or False): ").lower()
    if  priority == "true":
        tasks["priority_level"]=True
    elif priority_level == "false":
        tasks["priority_level"] = False
    else:
        print("Invalid input. Please enter 'True' or 'False' for priority level.")
        return
    
def sort_priority_level(tasks):
        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                x = tasks[i]["priority"]
                y = tasks[j]["priority"]
                if y > x:
                    tasks[i], tasks[j] = tasks[j], tasks[i]
        view_task()
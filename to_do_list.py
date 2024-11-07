import sys
#Welcome user and display a menu with options to ...
    #Add tasks
    #View tasks
    #Delete tasks
    #Quit the program
#Error handling using try, except, else, and finally

tasks = {}
error_message = "An error occured, please try again."
return_menu = "Returning to the main menu..."

def start():
    options = {
            1: ("Add a new task", add_task),
            2: ("View current tasks", view_task),
            3: ("Delete a task", del_task),
            4: ("Quit", quit_program)
        }
    
    print("Main Menu \nPlease choose from the following options:")
    for num, (description, func) in options.items():
        print(f"{num} - {description}")

    try:
        answer = int(input(""))
        if answer in options:
            options[answer][1](tasks)  # Call the associated function
        else:
            print(error_message)
            start()
            
    except (ValueError, TypeError) as e:
        print(error_message)
        start()

def add_task(tasks):
    try:
        print("Adding new task(s) \nEnter 'Back' to return to the main menu")
        task_qty = input("How many tasks would you like to add? ")
        
        #Returning to the main menu is not working for now.
        if task_qty.lower() == 'back':
            print(return_menu)
            start()
            
        elif task_qty.isdigit() and int(task_qty) > 0:
            task_qty = int(task_qty)
            print("Please enter the following...")
            
            while task_qty > 0:
                title = input("Task title: ")
                tasks[title] = {
                    "task_description": input("Description: "),
                    "task_date": input("Date: "),
                    "task_time": input("Time: ")
                }
                task_qty -= 1
            print("Task(s) added!")
            print(return_menu)
            start()
                
        else:
            print("Invalid input, please enter a positive number.")
            add_task(tasks)
                            
    except (ValueError, TypeError) as e:
        print(error_message)
        add_task(tasks)
        

def view_task(tasks):
    print("Viewing saved tasks \nEnter 'Back' to return to the main menu")
    for task, info in tasks.items():
        desc = info["task_description"]
        date = info["task_date"]
        time = info["task_time"]
        print(task)
        print(f"\t {desc} \n\t {date} \n\t {time}")
        
    try:
        answer = input("")
        
        if answer.lower() == "back":
            print(return_menu)
            start()
        else:
            print("Invalid input.")
            view_task(tasks)
            
    except (ValueError, TypeError) as e:
        print(error_message)
        view_task(tasks)
        

def del_task(tasks):
    print("Viewing saved tasks \nEnter 'Back' to return to the main menu")
    for task, info in tasks.items():
        desc = info["task_description"]
        date = info["task_date"]
        time = info["task_time"]
        print(task)
        print(f"\t {desc} \n\t {date} \n\t {time}")
        
    try:
        answer = input("Please enter what task you'd like to delete: ")
        
        if tasks.count(answer) > 1:
            pass
        elif answer in tasks:
            tasks.pop(answer)
        else:
            print("That is not a valid task to delete. Please try again.")
            del_task(tasks)
    except (TypeError, ValueError) as e:
        print(error_message)
        del_task(tasks)
            

def quit_program(tasks):
    print("Exiting program...")
    sys.exit()

start()
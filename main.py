import json
import time

tasks = []

def view_tasks():
    if not tasks:
        print("\nNo tasks available!!")
        return
         
    for i, task in enumerate(tasks, start = 1):
        status = "✅" if task["Done"] else "❌"  
        print(i,'.', task["task"], status) 

def eliminate():
    if not tasks:
        print("\nNothing to remove!! ")
        return
    print()
    print('=========================')    
    view_tasks()
    try:
        rem = int(input("\nEnter the task(s) you want to delete !:- "))
    except ValueError:
        print("\nInvalid Input! ")
        return

    if rem < 1 or rem > len(tasks):
        print("\nIndex out of range...")
        return
    print("Updating...!")
    time.sleep(2)
    tasks.pop(rem - 1)
    save_tasks()

    print("\nTask successfully removed!")
    print("\n---- Updated list:- ----")
    view_tasks()

def mark_completed():
    if not tasks:
        print("Empty Task(s) cannot be marked!\n ")
        return
    print("=======================")
    view_tasks()

    try:
         mark = int(input("\nWhich task have you completed? "))
    except ValueError:
        print("Invalid input")
        return

    if mark < 1 or mark > len(tasks):
        print("Index out of range...!") 
        return 

    tasks[mark - 1]["Done"] = True 
    save_tasks()
    print("\nTask marked as completed !!") 
    view_tasks()

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent = 4)

def load_tasks():
    global tasks    # This tells python to modify the tasks variable that exists outside the function

    try:            # Try reading the file
        with open("tasks.json", "r") as file:
            tasks = json.load(file)    
    except FileNotFoundError:
        tasks = []

load_tasks()
while True:
    print("\n-------- Welcome 2 'TO DO LIST' ----------\n")
    print("1. Add Task(s)")
    print("2. View task(s)")
    print("3. Delete tasks")
    print("4. Mark as completed")
    print("5. Exit.")

    choice = (input("\nEnter the Operator no: "))
    if choice not in ['1', '2', '3', '4', '5']:
        print("\nERROR! Given attribute not found.")
        continue      

    if choice == '1':
        print("\n----You chose to add a task---- ")
        task = input("\nAdd your Task: ").strip()
        if task == '':
            print("Task can't be empty !")
        else:
            tasks.append({
                "task": task,
                "Done": False
                })
            print("=======================")
            print("\nTask added successfully")
            print("=======================")
            save_tasks()

    elif choice == '2':
        print("\nLoading your tasks...\n")
        time.sleep(3)
        view_tasks()
 
    elif choice == '3':
        eliminate()

    elif choice == '4':
        mark_completed()

    elif choice == '5':
        print("Exiting the Program...")
        time.sleep(2)    
        print("You are good to go !")
        break
         
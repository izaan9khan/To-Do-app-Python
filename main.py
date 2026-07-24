import os
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
    print('\n=========================')    
    view_tasks()
    try:
        rem = int(input("\nEnter the task(s) you want to delete !:- "))
    except ValueError:
        print("\nInvalid Input! ")
        return

    if rem < 1 or rem > len(tasks):
        print(f"\nNo {rem} tasks found !!")
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
    print("========================")
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

def clear_screen():
    os.system("cls")

def edit_tasks():
    if not tasks:
        print("\nNothing to Edit!") 
        return

    view_tasks()
    try:
        edit = int(input("\nEnter the task(s) you want to edit? "))
    except ValueError:
        print("Invalid Input ! ")
        return

    if edit < 1 or edit > len(tasks):
        print("\nInvalid Input !! ")
        return
    print("current task: ", tasks[edit - 1]["task"])
    new_task = input("\nEdit task: ").strip()

    if not new_task:
        print("\nTask can't be empty !")
        return

    tasks[edit - 1]["task"] = new_task
    save_tasks()
    
    print("\nTask edited and added successfully ! \n")
    view_tasks()

def search_tasks():
    search = input("\nSearch Tasks: ").strip()
    if not search:
        print("\nEnter a task!")
        return

    found = False
    for item in tasks:
        if search.lower() in item["task"].lower():
            found = True
            status = "✅" if item["Done"] else "❌"
            print(item["task"], status)

    if not found:
        print("\n❌ No matching tasks found.")
        choice = input("\nWould you like to add a new task? (Y/N): ").strip().lower()

        if choice == "y":
            new_task = input("\nEnter the new task: ").strip()

            if new_task:
                tasks.append({
                    "task": new_task,
                    "Done": False
                })
                save_tasks()
                print("\n✅ Task added successfully!")
            else:
                print("\nTask cannot be empty.")


load_tasks()
while True:
    clear_screen()
    print("\n-------- Welcome 2 'TO DO LIST' ----------\n")
    print("1. Add Task(s)")
    print("2. View task(s)")
    print("3. Edit Tasks")
    print("4. Search tasks")
    print("5. Delete tasks")
    print("6. Mark as completed")
    print("7. Exit.")

    choice = (input("\nEnter the Operator no: "))
    if choice not in ['1', '2', '3', '4', '5','6', '7']:
        print("\nERROR! Given attribute not found.")
        print("\nPress Enter to continue...")
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
            input("\nPress Enter to continue...")

    elif choice == '2':
        print("\nLoading your tasks...\n")
        time.sleep(1.5)
        view_tasks()
        input("\nPress Enter to continue...")

    elif choice == '3':
        edit_tasks()
        input("Press Enter to continue...")

    elif choice == '4':
        search_tasks()
        input("\nPress Enter to continue")

    elif choice == '5':
        eliminate()
        input("\nPress Enter to continue...")

    elif choice == '6':
        mark_completed()
        input("\nPress Enter to continue...")

    elif choice == '7':
        print("Exiting the Program...")
        time.sleep(1)    
        print("\nYou are good to go !")
        break
         
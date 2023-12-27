import os

# Function to display the to-do list
def display_todo_list():
    with open("todo.txt", "r") as file:
        todo_list = file.readlines()
        if todo_list:
            print("\nTo-Do List:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task.strip()}")
        else:
            print("\nYour to-do list is empty!")

# Function to add a task to the to-do list
def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print(f"\nAdded task: {task}")

# Function to remove a task from the to-do list
def remove_task(task_number):
    try:
        with open("todo.txt", "r") as file:
            todo_list = file.readlines()
        
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            
            with open("todo.txt", "w") as file:
                file.writelines(todo_list)
            
            print(f"\nRemoved task: {removed_task.strip()}")
        else:
            print("\nInvalid task number.")
    except FileNotFoundError:
        print("\nYour to-do list is empty!")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        display_todo_list()
    elif choice == "2":
        task = input("\nEnter the task to add: ")
        add_task(task)
    elif choice == "3":
        display_todo_list()
        task_number = int(input("\nEnter the task number to remove: "))
        remove_task(task_number)
    elif choice == "4":
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")

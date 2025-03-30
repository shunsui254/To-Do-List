import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f'Added: "{task}"')

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available!")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{index}. {task['task']} [{status}]")

def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f'Marked task {index} as complete!')
    else:
        print("Invalid task number!")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f'Deleted task: "{removed_task["task"]}"')
    else:
        print("Invalid task number!")

def main():
    while True:
        try:
            print("\nTo-Do List App")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Complete Task")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                while True:  # Loop to handle the "Enter task" interface
                    task = input("Enter task: ")
                    print("\nY. Yes\nN. No\nB. Back to Main Menu")
                    sub_choice = input("Confirm adding the task: ").upper()
                    if sub_choice == "Y":
                        add_task(task)
                        break  # Exit the loop and return to the main menu
                    elif sub_choice == "N":
                        while True:  # Handle "Task discarded" interface
                            print("Task discarded. Please choose:")
                            print("\nN. New Task\nB. Back to Main Menu")
                            back_choice = input("Choose an option: ").upper()
                            if back_choice == "N":
                                break  # Restart the outer loop to allow the user to enter a new task
                            elif back_choice == "B":
                                break  # Exit the loop and return to the main menu
                            else:
                                print("Invalid choice! Returning to the 'Task discarded' interface.")
                        if back_choice == "B":
                            break  # Exit the outer loop and return to the main menu
                    elif sub_choice == "B":
                        break  # Exit the loop and return to the main menu
                    else:
                        print("Invalid choice! Returning to the 'Enter task' interface.")
            
            elif choice == "2":
                while True:  # Loop to handle the "View tasks" interface
                    view_tasks()
                    print("\nB. Back to Main Menu")
                    sub_choice = input("Choose an option: ").upper()
                    if sub_choice == "B":
                        break  # Exit the loop and return to the main menu
                    else:
                        print("Invalid choice! Returning to the 'View tasks' interface.")
            
            elif choice == "3":
                while True:  # Loop to handle the "Complete task" interface
                    view_tasks()
                    try:
                        index = int(input("Enter task number to complete: "))
                        print("\nY. Yes\nN. No\nB. Back to Main Menu")
                        sub_choice = input("Confirm completing the task: ").upper()
                        if sub_choice == "Y":
                            complete_task(index)
                            break  # Exit the loop and return to the main menu
                        elif sub_choice == "N":
                            while True:  # Handle "Task completion canceled" interface
                                print("Task completion canceled. Please choose:")
                                print("\nN. New Task\nB. Back to Main Menu")
                                back_choice = input("Choose an option: ").upper()
                                if back_choice == "N":
                                    break  # Restart the outer loop to allow the user to select a new task
                                elif back_choice == "B":
                                    break  # Exit the loop and return to the main menu
                                else:
                                    print("Invalid choice! Returning to the 'Task completion canceled' interface.")
                            if back_choice == "B":
                                break  # Exit the outer loop and return to the main menu
                        elif sub_choice == "B":
                            break  # Exit the loop and return to the main menu
                        else:
                            print("Invalid choice! Returning to the 'Complete task' interface.")
                    except ValueError:
                        print("Invalid input! Please enter a valid task number.")
            
            elif choice == "4":
                while True:  # Loop to handle the "Delete task" interface
                    view_tasks()
                    try:
                        index = int(input("Enter task number to delete: "))
                        print("\nY. Yes\nN. No\nB. Back to Main Menu")
                        sub_choice = input("Confirm deleting the task: ").upper()
                        if sub_choice == "Y":
                            delete_task(index)
                            break  # Exit the loop and return to the main menu
                        elif sub_choice == "N":
                            while True:  # Handle "Task deletion canceled" interface
                                print("Task deletion canceled. Please choose:")
                                print("\nN. New Task\nB. Back to Main Menu")
                                back_choice = input("Choose an option: ").upper()
                                if back_choice == "N":
                                    break  # Restart the outer loop to allow the user to select a new task
                                elif back_choice == "B":
                                    break  # Exit the loop and return to the main menu
                                else:
                                    print("Invalid choice! Returning to the 'Task deletion canceled' interface.")
                            if back_choice == "B":
                                break  # Exit the outer loop and return to the main menu
                        elif sub_choice == "B":
                            break  # Exit the loop and return to the main menu
                        else:
                            print("Invalid choice! Returning to the 'Delete task' interface.")
                    except ValueError:
                        print("Invalid input! Please enter a valid task number.")
            
            elif choice == "5":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice! Try again.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

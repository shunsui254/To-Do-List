# To-Do List CLI Application
A simple command-line interface (CLI) application for managing your tasks. This Python program allows you to add, view, complete, and delete tasks while saving your data to a JSON file for persistence.

## Features
Add Tasks: Enter a new task and confirm before saving.

View Tasks: List all tasks with a status icon showing whether they are complete (✓) or not (✗).

Complete Tasks: Mark tasks as complete by selecting them from the list.

Delete Tasks: Remove tasks from your list after confirmation.

Persistent Storage: Stores all tasks in a file (tasks.json), so your task list is maintained across sessions.


## Requirements
Python 3.x: Ensure you have a recent version of Python installed.

No external libraries: Only built-in modules (json, os) are used.


## Installation
Clone the Repository If you have Git installed, clone this repository to your local machine:

    git clone https://your-repository-url.git
    cd your-repository-directory

Download the Script If not using Git, download the script file (e.g., todo_app.py) to your local machine.

Ensure Python is installed Verify Python installation by running:

    python3 --version

## Usage

Run the Application Execute the script using Python:

    python todo_app.py
or

    python3 todo_app.py

## Interacting with the CLI

A menu will appear with options:

1. Add Task: Enter and confirm a new task.

2. View Tasks: Display all tasks with their status.

3. Complete Task: Mark a selected task as complete.

4. Delete Task: Remove a task after confirmation.

5. Exit: Quit the program.

For each primary action, you will be prompted with further sub-options like:

Y: Confirm the action.

N: Cancel the current action and choose to either start over or go back.

B: Return to the main menu.

Follow the on-screen instructions to manage your tasks.

### File Persistence All tasks are stored in tasks.json, which is automatically created in the same directory as the script. Do not delete or modify this file manually to maintain data integrity.

# Code Overview
## Main Functions:

load_tasks(): Loads the tasks from tasks.json if it exists.

save_tasks(tasks): Saves the current list of tasks to tasks.json.

add_task(task): Appends a new task to the task list.

view_tasks(): Lists all tasks with their completion status.

complete_task(index): Marks the given task (by its number) as completed.

delete_task(index): Removes the task specified by the index.

## User Interaction:

The main() function manages the overall application flow using loops, ensuring smooth navigation between menus and sub-menus for task management operations.

# Error Handling
The script validates user input (e.g., checking if the input task number is valid) and handles exceptions to prevent crashes.

Messages guide the user whenever an invalid choice is entered.

# Future Improvements
Adding a feature to edit tasks.

Incorporating deadlines or priorities.

Using a database or a more robust data management method for scalability.

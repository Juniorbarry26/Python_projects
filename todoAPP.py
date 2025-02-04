import os

todo_list = []

def show_menu():
    print("\n To-Do List Application")
    print("1. View Task")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Update a Task")
    print("6. Exit")

def view_task():
    if not todo_list:
        print("No task available")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully.")

def complete_task():
    view_task()
    try:
        task_num = int(input("Enter the task to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list.pop(task_num - 1)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number")

def delete_task():
    if not todo_list:
        print("No task to delete.")
        return
    view_task()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            del todo_list[task_num - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

def update_task():
    view_task()
    try:
        task_num = int(input("Select the task number to update: "))
        if 1 <= task_num <= len(todo_list):
            new_task = input("Enter the new task description: ")
            todo_list[task_num - 1] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            update_task()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

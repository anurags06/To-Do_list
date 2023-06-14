def display_menu():
    print("To-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("No tasks in the To-Do List.")
    else:
        print("Tasks in the To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully!")

def complete_task(todo_list):
    view_todo_list(todo_list)
    if not todo_list:
        return

    task_index = int(input("Enter the index of the completed task: ")) - 1
    if 0 <= task_index < len(todo_list):
        completed_task = todo_list.pop(task_index)
        print(f"Task '{completed_task}' marked as completed!")
    else:
        print("Invalid task index.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            complete_task(todo_list)
        elif choice == '4':
            print("Exiting the To-Do List Application.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()

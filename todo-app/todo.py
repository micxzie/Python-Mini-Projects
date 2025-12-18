import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "tasks.json")


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            return []

    if not isinstance(tasks, list):
        return []

    for task in tasks:
        if not isinstance(task, dict):
            continue
        if 'done' not in task and 'completed' in task:
            task['done'] = task['completed']
        if 'priority' not in task:
            task['priority'] = 'Medium'
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task = input("Enter the task description: ").strip()

    if task == "":
        print("Task description cannot be empty.")
        return

    print("Select task priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    priority_choice = input("Enter priority (1-3): ").strip()

    if priority_choice == "1":
        priority = "High"
    elif priority_choice == "2":
        priority = "Medium"
    elif priority_choice == "3":
        priority = "Low"
    else:
        print("Invalid priority. Defaulting to Medium.")
        priority = "Medium"

    tasks.append({'task': task, 'done': False, 'priority': priority})

    save_tasks(tasks)
    print('Task added successfully.')


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return {}

    priority_order = {'High': 1, 'Medium': 2, 'Low': 3}

    sorted_tasks = sorted(
        enumerate(tasks),
        key=lambda x: priority_order.get(x[1].get('priority', 'Medium'), 2)
    )

    display_map = {}

    for display_index, (original_index, task) in enumerate(sorted_tasks, start=1):
        is_done = task.get("done", task.get("completed", False))
        status = "[x]" if is_done else "[ ]"
        priority = task.get("priority", "Medium")
        print(f"{display_index}. {status} {task['task']} ({priority})")
        display_map[display_index] = original_index

    return display_map


def mark_task_done(tasks):
    display_map = view_tasks(tasks)
    if not display_map:
        return

    try:
        choice = int(input("Enter the task number to mark as done: "))
        if choice not in display_map:
            print("Invalid task number.")
            return

        task = tasks[display_map[choice]]
        task["done"] = True
        task["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    display_map = view_tasks(tasks)
    if not display_map:
        return

    try:
        choice = int(input("Enter the task number to delete: "))
        if choice in display_map:
            deleted_task = tasks.pop(display_map[choice])
            save_tasks(tasks)
            print(f'Task "{deleted_task["task"]}" deleted successfully.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def edit_task(tasks):
    display_map = view_tasks(tasks)

    if not display_map:
        return

    try:
        choice = int(input("Enter the task number to edit: "))
        if choice not in display_map:
            print("Invalid task number.")
            return

        task = tasks[display_map[choice]]
        new_description = input(
            f"Enter new description (leave blank to keep '{task['task']}'): "
        ).strip()
        if new_description:
            task['task'] = new_description

        print("Select new priority (leave blank to keep current):")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        priority_choice = input("Enter priority (1-3): ").strip()
        if priority_choice == "1":
            task["priority"] = "High"
        elif priority_choice == "2":
            task["priority"] = "Medium"
        elif priority_choice == "3":
            task["priority"] = "Low"
        elif priority_choice == "":
            pass
        else:
            print("Invalid choice. Keeping current priority.")

        save_tasks(tasks)
        print("Task updated successfully.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        print("")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

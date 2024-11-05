import json

# Load tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added.")

# View tasks
def view_tasks(tasks):
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. [{status}] {task['task']}")

# Mark task as complete
def complete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        print("Task marked as complete.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

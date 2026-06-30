import os

FILENAME = "todo_list.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file]

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)

def remove_task(tasks):
    num = int(input("Enter task number: "))
    tasks.pop(num - 1)
    save_tasks(tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
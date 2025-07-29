def showtasks(tasks):
    if not tasks:
        print("\nNo tasks yet.\n")
        return
    print("\n Your To Do List ")
    for i, task in enumerate(tasks, start=1):
        status = "(Done)" if task["done"] else "(Not Done)"
        print(f"{i}. {status} {task['title']}")
    print()


def addtask(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added.\n")
    else:
        print("Task cannot be empty.\n")


def markdone(tasks):
    showtasks(tasks)
    try:
        index = int(input("Enter task no. to mark it as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task complete.\n")
        else:
            print("Invalid task no.\n")
    except ValueError:
        print("Enter a valid no.\n")


def updatetask(tasks):
    showtasks(tasks)
    try:
        index = int(input("Enter task no. to update: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Enter new title: ").strip()
            if new_title:
                tasks[index]["title"] = new_title
                print("Task updated.\n")
            else:
                print("Task cannot be empty.\n")
        else:
            print("Invalid task no.\n")
    except ValueError:
        print("Enter a valid no.\n")


def deletetask(tasks):
    showtasks(tasks)
    try:
        index = int(input("Enter task no. to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed['title']}\n")
        else:
            print("Invalid task no.\n")
    except ValueError:
        print("Enter a valid no.\n")


def main():
    tasks = []

    while True:
        print(" To-Do List Menu ")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            showtasks(tasks)
        elif choice == "2":
            addtask(tasks)
        elif choice == "3":
            markdone(tasks)
        elif choice == "4":
            updatetask(tasks)
        elif choice == "5":
            deletetask(tasks)
        elif choice == "6":
            print("Exiting")
            break
        else:
            print("Wrong choice.Try again.\n")


if __name__ == "__main__":
    main()

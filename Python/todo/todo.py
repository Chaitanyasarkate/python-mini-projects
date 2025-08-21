
tasks = []

def show_menu():
    print("\n=== TO-DO LIST APP ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet! ✅")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty!")

def remove_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please enter 1–4.")

if __name__ == "__main__":
    main()

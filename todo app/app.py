my_list = []


def add_task():
    try:
        user = input("Enter Your Task Here: ")
        my_list.append(user)
        print("Task added successfully")

    except Exception:
        print("Invalid data, try again")


def view_task():
    if len(my_list) == 0:
        print("No tasks available")

    else:
        print("\nTasks:")
        for index, task in enumerate(my_list, start=1):
            print(f"{index}. {task}")


def delete_task():
    view_task()

    try:
        index = int(input("Enter task number you want to delete: "))

        if 1 <= index <= len(my_list):
            removed = my_list.pop(index - 1)
            print(f"Task '{removed}' deleted successfully")

        else:
            print("Invalid task number")

    except ValueError:
        print("Please enter a valid number")


def update_task():
    view_task()

    try:
        index = int(input("Enter task number you want to update: "))

        if 1 <= index <= len(my_list):
            new_task = input("Enter new task: ")
            my_list[index - 1] = new_task
            print("Task updated successfully")

        else:
            print("Invalid task number")

    except ValueError:
        print("Please enter a valid number") 


while True:
    print("\n----- TO-DO LIST MENU ----")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_task()

        elif choice == 2:
            view_task()

        elif choice == 3:
            update_task()

        elif choice == 4:
            delete_task()

        elif choice == 5:
            print("Thanks! You are exiting the program")
            break

        else:
            print("Invalid choice! Try Again")

    except ValueError:
        print("Please enter numbers only")
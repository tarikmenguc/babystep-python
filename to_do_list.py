def to_do_list():
    tasks = []  # List to store tasks

    while True:
        # Display the current to-do list
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        # Display menu options
        print("\n1. Add a New Task")
        print("2. Delete a Task")
        print("3. Exit")
        choice = input("Your choice: ")

        # Handle user's choice
        if choice == "1":
            new_task = input("New task: ")
            tasks.append(new_task)  # Add the new task to the list
        elif choice == "2":
            try:
                task_to_delete = int(input("Enter the number of the task to delete: "))
                if 1 <= task_to_delete <= len(tasks):
                    tasks.pop(task_to_delete - 1)  # Remove the selected task
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "3":
            break  # Exit the program
        else:
            print("Invalid choice!")

# Run the to-do list program
to_do_list()
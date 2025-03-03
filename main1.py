from tasks import add_task, view_tasks, delete_task

def main():
    print("Welcome to the To-Do List Manager!")
    while True:
        print("\nOptions:")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Delete a Task")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            print(add_task(task))
        elif choice == "2":
            print("Your Tasks:")
            print(view_tasks())
        elif choice == "3":
            print(view_tasks())
            task_no = int(input("Enter the task number to delete: "))
            print(delete_task(task_no))
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

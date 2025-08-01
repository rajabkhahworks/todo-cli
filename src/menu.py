def show_menu():
    # Print the main menu header
    print("\n---- Todo-CLI ----")

    # Show option to display all tasks
    print("[0] Show tasks")

    # Show option to add a new task
    print("[1] Add task")

    # Show option to remove a task
    print("[2] Remove task")

    # Show option to clear all tasks
    print("[3] Clear all tasks")

    # Show option to mark a task as done
    print("[4] Mark task as done")

    # Show option to exit the program
    print("[5] Exit")
    
    # Print menu footer line
    print("------------------")

def get_user_choice():
    # Prompt the user to enter their menu choice and return it
    return input("\nEnter your choice: ")

# Import the TaskManager class from tasks.py
from src.tasks import TaskManager
# Import the show_menu and get_user_choice functions from menu.py
from src.menu import show_menu, get_user_choice
from src.colors import gray, red, reset

def main():
    # Create a TaskManager object to handle tasks
    manager = TaskManager()
    
    # Infinite loop to show the menu and get user input
    while True:
        # Display the menu options
        show_menu()
        
        # Get the user's choice
        choice = get_user_choice()
        
        # If the user chooses 0 → show all tasks
        if choice == "0":
            manager.show_tasks()

        # If the user chooses 1 → add a new task
        elif choice == "1":
            manager.add_task()

        # If the user chooses 2 → remove a task
        elif choice == "2":
            manager.remove_task()

        # If the user chooses 3 → clear all tasks
        elif choice == "3":
            manager.clear_tasks()

        # If the user chooses 4 → mark a task as done
        elif choice == "4":
            manager.mark_task_done()

        # If the user chooses 5 → exit the program
        elif choice == "5":
            print(f"\n{gray}Exiting...{reset}")
            break

        # If the input is invalid → show an error message
        else:
            print(f"\n{red}Invalid option. Please try again.{reset}")

# Run the main function only if the file is executed directly
if __name__ == "__main__":
    main()

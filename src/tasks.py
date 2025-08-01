from .models import Task
from .storage import Storage
from .colors import green, red, gray, reset

class TaskManager:
    def __init__(self):
        # Initialize Storage and load existing tasks from file
        self.storage = Storage()
        self.tasks = self.storage.load()

    def show_tasks(self):
        # Display all tasks with their status
        if not self.tasks:
            print(f"\n{gray}No tasks found.{reset}")
        else:
            print("\n--- Your Tasks ---")
            for i, task in enumerate(self.tasks, 1):
                # Show checkmark if done, cross if not
                status = f"{green}✔{reset}" if task.done else f"{red}✗{reset}"
                print(f"\n[{i}] {task.title} ({status})")

    def add_task(self):
        # Prompt user to enter a new task title
        title = input("\nEnter a new task: ").strip()
        if title:
            # Add new Task and save updated list
            self.tasks.append(Task(title))
            self.storage.save(self.tasks)
            print(f"\n{green}Task added.{reset}")
        else:
            print(f"\n{red}Task cannot be empty.{reset}")

    def remove_task(self):
        # Remove a task by its number
        if not self.tasks:
            print(f"\n{gray}No tasks to remove.{reset}")
            return
        try:
            index = int(input("\nEnter the task number to remove: ")) - 1
            if 0 <= index < len(self.tasks):
                removed = self.tasks.pop(index)  # Remove task from list
                self.storage.save(self.tasks)    # Save updated list
                print(f"\n{green}Task '{removed.title}' removed.{reset}")
            else:
                print(f"\n{red}Invalid task number.{reset}")
        except ValueError:
            print(f"\n{red}Please enter a valid number.{reset}")

    def clear_tasks(self):
        # Confirm before clearing all tasks
        confirm = input("\nAre you sure you want to clear all tasks? [Yes/No]: ").lower()
        if confirm in ("yes", "y"):
            self.tasks.clear()          # Clear the tasks list
            self.storage.save(self.tasks)  # Save empty list
            print(f"\n{green}All tasks cleared.{reset}")

    def mark_task_done(self):
        # Mark a specific task as done by its number
        if not self.tasks:
            print(f"\n{gray}No tasks to mark.{reset}")
            return
        try:
            index = int(input("\nEnter the task number to mark as done: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index].mark_done()  # Mark the task done
                self.storage.save(self.tasks)  # Save changes
                print(f"\n{green}Task '{self.tasks[index].title}' marked as done.{reset}")
            else:
                print(f"\n{green}Invalid task number.{reset}")
        except ValueError:
            print(f"\n{red}Please enter a valid number.{reset}")

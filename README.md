# 📝 Todo-CLI

A simple and modular **command-line todo list manager** written in Python.  
Tasks are saved in a JSON file so you will never lose your list after closing the program.  

---

## ✨ Features
- Add new tasks
- Show all tasks
- Remove specific tasks
- Clear all tasks
- Mark tasks as **done** (✔)
- Tasks are saved in a `tasks.json` file automatically
- Colorred output (🟥 🟩 ⬛) to distinguish task statuses 

---

## 📦 Requirements
- Python 3.x installed
- No external dependencies (uses only Python standard library)

---

## 🚀 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/rajabkhahworks/todo-cli.git
   ```
2. **Change directory**
    ```bash
    cd todo-cli
    ```
3. **Run main.py**
    ```bash
    python3 main.py
    ```
    
----

## 🖥️ Example CLI Output

```
---- Todo-CLI ----
[0] Show tasks
[1] Add task
[2] Remove task
[3] Clear all tasks
[4] Mark task as done
[5] Exit
------------------

Enter your choice: 1
Enter a new task: Buy milk
Task added.

Enter your choice: 0
--- Your Tasks ---
[1] Buy milk (✗)

Enter your choice: 4
Enter the task number to mark as done: 1
Task 'Buy milk' marked as done.

Enter your choice: 0
--- Your Tasks ---
[1] Buy milk (✔)
```


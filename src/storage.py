import json, os
from .models import Task

class Storage:
    def __init__(self, file_path="tasks.json"):
        # Initialize Storage with the path to the JSON file for saving/loading tasks
        self.file_path = file_path

    def load(self):
        # Load tasks from the JSON file if it exists
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                data = json.load(f)  # Read JSON data from file
                # Convert each dictionary in data to a Task object
                return [Task.from_dict(item) for item in data]
        # Return empty list if file does not exist
        return []
    
    def save(self, tasks):
        # Save a list of Task objects to the JSON file
        with open(self.file_path, "w") as f:
            # Convert each Task to a dictionary and write to file with indentation
            json.dump([task.to_dict() for task in tasks], f, indent=2)

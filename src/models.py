class Task:
    def __init__(self, title, done=False):
        # Initialize a Task with a title and done status (default is False)
        self.title = title
        self.done = done
    
    def mark_done(self):
        # Mark the task as done by setting done to True
        self.done = True
    
    def to_dict(self):
        # Convert the Task object to a dictionary for easy saving
        return {"title": self.title, "done": self.done}
    
    @staticmethod
    def from_dict(data):
        # Create a Task object from a dictionary
        return Task(data["title"], data["done"])

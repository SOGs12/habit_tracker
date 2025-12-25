from models.habit import Habit
from storage.database_handler import DatabaseHandler

class HabitManager:
    """
    Manages all habits in the application.
    """

    def __init__(self):
        self.db = DatabaseHandler()
        self.habits = self.db.load_habits()  # Load habits from database at startup

    def create_habit(self, name: str, periodicity: str):
        """Create a new habit and save it."""
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        self.db.save_habit(habit)
        print(f"Habit '{name}' created successfully!")

    def delete_habit(self, name: str):
        """Delete a habit by name."""
        habit = self.get_habit(name)
        if habit:
            self.habits.remove(habit)
            self.db.delete_habit(habit)
            print(f"Habit '{name}' deleted successfully!")
        else:
            print(f"Habit '{name}' not found.")

    def get_habit(self, name: str):
        """Find a habit by name."""
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def complete_habit(self, name: str):
        """Mark a habit as completed and save the completion."""
        habit = self.get_habit(name)
        if habit:
            habit.complete_task()
            self.db.save_completion(habit)
            print(f"Habit '{name}' marked as completed!")
        else:
            print(f"Habit '{name}' not found.")

    def list_habits(self):
        """List all habits."""
        if not self.habits:
            print("No habits found.")
        for habit in self.habits:
            print(habit)

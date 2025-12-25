from src.db import DatabaseHandler
from src.manager import HabitManager

db = DatabaseHandler()
mgr = HabitManager(db)

# Create a habit
hid = mgr.create_habit("Exercise", "daily")
print("Created habit id:", hid)

# Complete the habit
ts = mgr.complete_habit(hid)
print("Completed at:", ts)

# Delete the habit
deleted = mgr.delete_habit(hid)
print("Deleted:", deleted)


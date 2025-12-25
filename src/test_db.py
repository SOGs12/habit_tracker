from src.db import DatabaseHandler

db = DatabaseHandler()

# Try fetching habits (should be empty now)
print("Habits:", db.fetch_habits())

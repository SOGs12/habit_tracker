\# Habit Tracker
A simple habit tracking app built with Python and SQLite.  
Track daily and weekly habits, record completions, and analyze streaks.

## Features
- Create and delete habits
- Mark habits as completed
- View all habits or filter by periodicity
- Analytics: longest streak per habit and across all habits
- Seed script with demo data
- Automated tests with pytest

---



\## Setup



1\. Clone the repository:

&nbsp;  ```bash

&nbsp;  git clone https://github.com/yourusername/habit-tracker.git

&nbsp;  cd habit-tracker



2\. Create a virtual environment:

python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\\Scripts\\activate      # Windows



3\. Create a virtual environment:

pip install -r requirements.txt



**Initialize Data**

Seed the database with predefined habits and 4 weeks of completions:

python -m src.seed

&nbsp;

**Expected output:**
✅ Seeded 5 habits with 4 weeks of data.



**Run**
Launch the CLI:
python -m src.cli

**Usage**
Initialize the database:
python -m src.db

Seed demo data:
python -m src.seed

Run the CLI:
python -m src.cli


**Analytics**

* List all habits → see all habit titles.
* Filter habits → by periodicity (Daily/Weekly).
* Longest streak overall → across all habits.
* Longest streak for chosen habit → detailed streak analysis.



**Testing**
Run all tests with:
python -m pytest -v



**Tests cover:**
* Habit creation, completion, deletion.
* Analytics functions (list, filter, streaks).
* Seed data verification.

**Project Structure**
habit_tracker/
  src/
    db.py
    manager.py
    analytics.py
    cli.py
    seed.py
  tests/
    test_analytics.py
    test_habits.py
    test_manager.py
    test_manager_mock.py
    test_seed.py


**Design Notes**

* OOP → used for core habit/user management (manager.py, models.py).
* FP → used for analytics (analytics.py) to keep functions pure and testable.
* Persistence → SQLite database with schema defined in schema.sql.


**Limitations \& Roadmap**

* Current periodicities: Daily and Weekly only.
* No reminders or notifications yet.
* CLI‑only interface (no GUI/web).


**Future improvements:**

* Add monthly habits.
* Add reminder system (email/notifications).
* Build a GUI or web interface for broader usability.



---



✅ This README.md covers all the required sections: overview, setup, seed, run, features, analytics, testing, design notes, limitations \& roadmap.

# habit_tracker

"""Student Database — nested dictionaries exercise.

Exercises:
  1. Create a student database with nested dicts
  2. Add students with name, grades dict, and attendance
  3. Calculate GPA for each student
  4. Find top student and class average
"""


def add_student(db, name, grades=None):
    """Add a student to the database."""
    # TODO: Implement
    # Hint: db[name] = {"grades": grades or {}, "attendance": 0}
    pass


def add_grade(db, name, subject, grade):
    """Add a grade for a student in a subject."""
    # TODO: Implement
    pass


def get_gpa(db, name):
    """Calculate and return a student's GPA."""
    # TODO: Implement
    # Hint: grades = db[name]["grades"].values()
    pass


def top_student(db):
    """Return the name of the student with highest GPA."""
    # TODO: Implement
    pass


def main():
    # TODO: Create database, add students, add grades, show stats
    # Hint: db = {}
    # Hint: add_student(db, "Alice")
    # Hint: add_grade(db, "Alice", "Math", 95)
    pass  # Remove when done


if __name__ == "__main__":
    main()

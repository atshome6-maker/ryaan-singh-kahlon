"""
Student Grading System (friendly version)
-----------------------------------------
A small program to keep track of your students' marks, work out their
grades, and see how the whole class is doing.

Built in 7 steps - write them in order and run the file after each one.
"""

import json
import os

DATA_FILE = "students.json"
PASS_MARK = 40



def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= PASS_MARK:
        return "E"
    else:
        return "F"


def encouragement(grade):
    """A little note to go with each grade, so a report card feels personal."""
    notes = {
        "A+": "Outstanding work! Keep it up.",
        "A": "Excellent results, really well done.",
        "B": "Good job - a little more push and you'll be at the top.",
        "C": "Solid effort. There's room to grow.",
        "D": "You're getting there. Keep practising.",
        "E": "A pass, but only just. Extra revision will help.",
        "F": "Don't be discouraged - let's work on the weak subjects together.",
    }
    return notes[grade]



class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}  # for example {"Maths": 90, "Science": 80}

    def add_mark(self, subject, score):
        # "not (0 <= score <= 100)" also catches odd input like "nan"
        if not (0 <= score <= 100):
            raise ValueError("Marks need to be between 0 and 100.")
        self.marks[subject.title()] = score

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        return calculate_grade(self.average())

    def report_card(self):
        print()
        print("=" * 38)
        print(f"  Report card for {self.name}")
        print(f"  Roll number: {self.roll_no}")
        print("-" * 38)

        if not self.marks:
            print(f"  No marks for {self.name} yet.")
            print("=" * 38)
            return

        for subject, score in self.marks.items():
            print(f"  {subject:<16}{score:>6.1f}   ({calculate_grade(score)})")
        print("-" * 38)
        print(f"  Average : {self.average():.2f}")
        print(f"  Grade   : {self.grade()}")
        print(f"  Result  : {'Passed' if self.average() >= PASS_MARK else 'Needs another try'}")
        print()
        print(f"  {encouragement(self.grade())}")
        print("=" * 38)



class GradingSystem:
    def __init__(self):
        self.students = {}

    
    def add_student(self, roll_no, name):
        if roll_no.strip() == "" or name.strip() == "":
            raise ValueError("Both a roll number and a name are needed.")
        if roll_no in self.students:
            raise ValueError(f"Roll number {roll_no} is already taken.")
        self.students[roll_no] = Student(roll_no, name)

    def get_student(self, roll_no):
        if roll_no not in self.students:
            raise KeyError(f"I couldn't find a student with roll number {roll_no}.")
        return self.students[roll_no]

    def remove_student(self, roll_no):
        self.get_student(roll_no)  
        del self.students[roll_no]

   
    def graded_students(self):
        return [s for s in self.students.values() if s.marks]

    def ranking(self):
        graded = self.graded_students()
        if not graded:
            print("Nobody has any marks yet, so there's nothing to rank.")
            return
        graded.sort(key=lambda s: s.average(), reverse=True)
        print("\nClass ranking")
        print("-" * 38)
        for place, s in enumerate(graded, 1):
            print(f"  {place}. {s.name:<16}{s.average():>6.2f}   {s.grade()}")

    def class_statistics(self):
        graded = self.graded_students()
        if not graded:
            print("Nobody has any marks yet, so there are no statistics to show.")
            return
        class_avg = sum(s.average() for s in graded) / len(graded)
        topper = max(graded, key=lambda s: s.average())
        passed = sum(1 for s in graded if s.average() >= PASS_MARK)
        print("\nHow the class is doing")
        print("-" * 38)
        print(f"  Class average : {class_avg:.2f}")
        print(f"  Top student   : {topper.name} ({topper.average():.2f})")
        print(f"  Passed        : {passed} of {len(graded)} "
              f"({passed / len(graded) * 100:.0f}%)")

    def save(self, path=DATA_FILE):
        data = [
            {"roll_no": s.roll_no, "name": s.name, "marks": s.marks}
            for s in self.students.values()
        ]
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def load(self, path=DATA_FILE):
        if not os.path.exists(path):
            return  
        try:
            with open(path) as f:
                data = json.load(f)
            for d in data:
                student = Student(d["roll_no"], d["name"])
                student.marks = d["marks"]
                self.students[d["roll_no"]] = student
            if self.students:
                print(f"Welcome back! Loaded {len(self.students)} student(s).")
        except (json.JSONDecodeError, KeyError, TypeError):
            print("Hmm, the saved data file looks damaged, so I'm starting fresh.")
            self.students = {}



def enter_marks(student):
    print(f"Let's add marks for {student.name}. Press Enter on its own when done.")
    while True:
        subject = input("  Subject: ").strip()
        if subject == "":
            break
        try:
            score = float(input(f"  Marks in {subject} (0-100): "))
            student.add_mark(subject, score)
        except ValueError as e:
            print(f"  That didn't work ({e}) Let's try {subject} again.")
    print("Marks saved for now.")


def main():
    system = GradingSystem()
    print("\nHello! Welcome to the Student Grading System.")
    system.load()

    while True:
        print("\nWhat would you like to do?")
        print("  1. Add a student")
        print("  2. Enter marks")
        print("  3. See a report card")
        print("  4. See the class ranking")
        print("  5. See class statistics")
        print("  6. Remove a student")
        print("  7. Save and quit")
        choice = input("Your choice (1-7): ").strip()

        try:
            if choice == "1":
                roll = input("Roll number: ").strip()
                name = input("Student's name: ").strip()
                system.add_student(roll, name)
                print(f"Done - {name} has been added.")
            elif choice == "2":
                enter_marks(system.get_student(input("Roll number: ").strip()))
            elif choice == "3":
                system.get_student(input("Roll number: ").strip()).report_card()
            elif choice == "4":
                system.ranking()
            elif choice == "5":
                system.class_statistics()
            elif choice == "6":
                system.remove_student(input("Roll number: ").strip())
                print("The student has been removed.")
            elif choice == "7":
                system.save()
                print("Everything is saved. See you next time!")
                break
            else:
                print("Sorry, please pick a number from 1 to 7.")
        except (ValueError, KeyError) as e:
            print(f"Oops: {e.args[0]}")


if __name__ == "__main__":
    main()

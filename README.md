# ryaan-singh-kahlon
he Student Grading System is a Python program that lets teachers add students, record subject marks, and automatically calculate averages, letter grades, and pass or fail results. It shows report cards, class rankings, and statistics, checks for invalid input, and saves all data to a JSON file.

# Student Grading System

A simple, menu-driven Python program that helps teachers record student marks, calculate grades, and see how a class is performing. It runs in the terminal and needs no external libraries.

## Features

- Add and remove students using a roll number and name
- Enter marks for any number of subjects (0-100)
- Automatic average, letter grade, and pass/fail result
- Report card for each student
- Class ranking from highest to lowest average
- Class statistics: class average, top student, and pass count
- Data saved to a JSON file and loaded automatically on the next run
- Input checking with clear error messages

## Requirements

- Python 3.6 or newer (also works on Python 2.7)
- No extra packages needed

## How to Run

1. Save the code as `grading.py`.
2. Open a terminal in the same folder.
3. Run:

```
python grading.py
```

On some systems you may need to use `python3 grading.py` instead.

## How to Use

When the program starts, you will see this menu:

```
What would you like to do?
  1. Add a student
  2. Enter marks
  3. See a report card
  4. See the class ranking
  5. See class statistics
  6. Remove a student
  7. Save and quit
```

Type a number from 1 to 7 and press Enter.

**Typical workflow:**

1. Choose **1** to add a student (for example roll number `1`, name `Asha`).
2. Choose **2**, enter the roll number, then type each subject and its marks. Press Enter on an empty subject when you are finished.
3. Choose **3** to view the student's report card.
4. Choose **7** to save and quit. Your data is stored in `students.json`.

## Example Report Card

```
======================================
  Report card for Asha
  Roll number: 1
--------------------------------------
  Maths             92.0   (A+)
  Science           85.0   (A)
--------------------------------------
  Average : 88.50
  Grade   : A
  Result  : Passed
======================================
```

## Grading Scale

| Average    | Grade |
|------------|-------|
| 90 - 100   | A+    |
| 80 - 89    | A     |
| 70 - 79    | B     |
| 60 - 69    | C     |
| 50 - 59    | D     |
| 40 - 49    | E     |
| Below 40   | F     |

The pass mark is 40. You can change it by editing `PASS_MARK` at the top of the file.

## Project Structure

```
grading.py        # the whole program
students.json     # created automatically when you save
README.md         # this file
```

## How the Code Is Organised

| Part                  | What it does                                                        |
|-----------------------|---------------------------------------------------------------------|
| `calculate_grade()`   | Converts an average score into a letter grade                       |
| `Student` class       | Stores a student's details and marks, and calculates their results  |
| `GradingSystem` class | Manages all students, ranking, statistics, saving, and loading      |
| `enter_marks()`       | Handles typing in subjects and marks for one student                |
| `main()`              | Shows the menu and runs the program                                 |

## Error Handling

The program handles these cases without crashing:

- Marks that are not numbers, or are outside 0-100
- Duplicate roll numbers
- Empty roll numbers or names
- Students that do not exist
- A damaged or unreadable `students.json` file (the program starts fresh)

## Future Improvements

- Weighted subjects (for example, exams worth more than assignments)
- GPA calculation
- Export reports to CSV or PDF
- A graphical interface

## Concepts Demonstrated

Classes and objects, dictionaries, lists, loops, functions, exception handling, and file handling with JSON.

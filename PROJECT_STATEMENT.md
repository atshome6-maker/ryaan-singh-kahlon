# Project Statement: Student Grading System

## Problem Statement

Teachers often record student marks on paper or in scattered spreadsheets. Calculating averages and grades by hand takes time, is easy to get wrong, and makes it hard to compare students or see how a whole class is performing. Records can also be lost or become inconsistent between terms.

There is a need for a simple tool that stores student marks in one place, calculates results automatically, and gives a clear picture of individual and class performance.

## Objective

To build a Python program that lets a teacher:

- Record students and their marks in multiple subjects
- Automatically calculate averages, letter grades, and pass/fail results
- View individual report cards
- Rank students and see class-wide statistics
- Save data so it is available the next time the program is used

## Scope

**Included**

- Adding and removing students by roll number and name
- Entering marks (0-100) for any number of subjects
- Grade calculation using a fixed scale (A+ to F, pass mark 40)
- Report cards, class ranking, and class statistics
- Saving and loading data using a JSON file
- Validation of user input with clear error messages

**Not included**

- A graphical interface or web version
- Multiple teachers or user accounts
- Weighted subjects, GPA, or report export (possible future work)

## Proposed Solution

A menu-driven command-line application written in Python using object-oriented programming.

- A `Student` class stores a student's details and marks and calculates their average and grade.
- A `GradingSystem` class manages all students, produces the ranking and statistics, and handles saving and loading.
- The program checks all input and handles errors such as invalid marks, duplicate roll numbers, missing students, and damaged data files without crashing.

## Tools and Technologies

| Item              | Details                                   |
|-------------------|-------------------------------------------|
| Language          | Python 3.6+ (also works on Python 2.7)    |
| Storage           | JSON file (`students.json`)               |
| Libraries         | Standard library only (`json`, `os`)      |
| Interface         | Command-line menu                         |

## Expected Outcome

A reliable, easy-to-use program that saves teachers time, removes calculation errors, and gives a quick overview of student and class performance.

## Grading Scale Used

| Average    | Grade |
|------------|-------|
| 90 - 100   | A+    |
| 80 - 89    | A     |
| 70 - 79    | B     |
| 60 - 69    | C     |
| 50 - 59    | D     |
| 40 - 49    | E     |
| Below 40   | F     |

## Future Enhancements

- Weighted subjects and GPA calculation
- Export reports to CSV or PDF
- Graphical or web interface

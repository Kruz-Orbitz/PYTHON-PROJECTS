# reading json file into python
import json

with open("students.json", "r") as file:
    students = json.load(file)

    for student in students:
        print(f"{student['name']},{student['score']}")


# writting python file into json
import json

students = [
    {"name": "Tega", "score": 80, "passed": True},
    {"name": "Miracle", "score": 52, "passed": True},
    {"name": "Tamte", "score": 10, "passed": False},
]

with open("students_backup.json", "w") as file:
    json.dump(students, file, indent=4)

# function with json

import json


def save_subjects(subjects):
    with open("subjects.json", "w") as file:
        json.dump(subjects, file, indent=4)


import json


def load_subjects():
    with open("subjects.json", "r") as file:
        all_subjects = json.load(file)
        return all_subjects


def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


# error handling with json

import json


def load_students():
    try:
        with open("students.json", "r") as file:
            student_file = json.load(file)
            return student_file
    except FileNotFoundError:
        print("file not found")
        return []


def load_students():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
            return students

    except json.JSONDecodeError:
        print("invalid json file")
        return []


import json


def load_students():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
            return students
    except FileNotFoundError:
        print("json file not found")
        return []
    except json.JSONDecodeError:
        print("json file not valid")
        return []

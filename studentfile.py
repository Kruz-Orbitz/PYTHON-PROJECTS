def save_students(students):
    with open("students.txt", "w") as file:
        for student in students:
            file.write(student + "\n")
            print(student)


students = ["kingsley", "tega", "miracle", "neche", "agu"]
save_students(students)

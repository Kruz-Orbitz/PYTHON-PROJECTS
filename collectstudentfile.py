def load_student():
    students = []

    with open("students.txt", "r") as file:
        student = file.readline()

        while student != "":
            students.append(student.strip())

            student = file.readline()

    return students


print(load_student())

def load_students():
    students = []
    with open("students.txt", "r") as file:
        for student in file:
            student_details = student.strip().split(",")
            student_name = student_details[0]
            student_score = int(student_details[1])
            all_student = [student_name, student_score]
            students.append(all_student)
    return students


def update_student(students, name, new_score):
    for student in students:
        if student[0] == name:
            student[1] = new_score
    return students


students = load_students()

update_student(students, "Miracle", 95)

all_students = []

for student in students:
    line = student[0] + ',' + str(student[1])
    all_students.append(line)
student_update = '\n'.join(all_students)

with open('students.txt', 'w') as file:
    file.write(student_update)
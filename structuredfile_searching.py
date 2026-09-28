def find_student_score(name):
    with open("students.txt", "r") as file:
        for student in file:
            student_record = student.strip().split(",")
            student_name = student_record[0]
            student_score = int(student_record[1])
            if student_name == name:
                return student_score

    return None


print(find_student_score("Miracle"))
print(find_student_score("David"))

students = []

while True:
    name = input('what is the student name (or done): ')
    if name == 'done':
        break
    students.append(name)

with open('student.txt', 'a') as file:
    for name in students:
        file.write(name + '\n')

print(students)
total = 0

try:
    with open('student.txt', 'r') as file:
        student_names = file.readline()
        while student_names != '':
            total = total + 1
            student_names = file.readline()
except FileNotFoundError:
    print('create a valid file')
else:
    print(total)
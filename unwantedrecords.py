lines = [
    'kingsley,85\n',
    'Tega,seventy-two\n',
    'Miracle,91\n',
    '\n',
    'Grace, 64\n'
]

valid_students = []

for line in lines:
    line =  line.strip()
    if line == '':
        continue
    students = line.split(',')
    student_name = students[0]
    try:
        scores = int(students[1])
    except ValueError:
        print(f'invalid score for {student_name}')
        continue
    valid_students.append([student_name, scores])

print(valid_students)

    

    

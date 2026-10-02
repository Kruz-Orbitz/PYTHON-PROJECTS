lines = ["kingsley,85\n", "\n", "miracle, 91\n" "", "grace, 64\n"]
new_names = []
for line in lines:
    line = line.strip()
    if line == "":
        continue
    student = line.split(",")
    name = student[0]
    score = int(student[1])

    all_names = [name, str(score)]

    finalized_names = ",".join(all_names)

    new_names.append(finalized_names)

    print(finalized_names)

import csv


def load_students():

    student_records = []
    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames is None:
                print("the file is empty")
                return student_records
            if "name" not in reader.fieldnames or "score" not in reader.fieldnames:
                print("invalid headers")
                return student_records

            for student in reader:
                if student["score"] == "" or student["name"] == "":
                    continue
                try:
                    student["score"] = int(student["score"])
                    if student["score"] < 0 or student["score"] > 100:
                        continue
                except ValueError:
                    continue
                student_records.append(student)
            return student_records
    except FileNotFoundError:
        print("file was not found")
        return student_records

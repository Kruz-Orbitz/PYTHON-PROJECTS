import csv


def load_students():
    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)

        next(reader)

        students_record = []

        for student in reader:
            student_name = student[0]
            student_score = int(student[1])

            all_student = [student_name, student_score]

            students_record.append(all_student)

        return students_record


import csv


def load_products():
    with open("products.csv", "r", newline="") as file:

        all_products = []

        reader = csv.DictReader(file)

        for row in reader:

            row["price"] = int(row["price"])
            row["quantity"] = int(row["quantity"])
            all_products.append(row)
        return all_products


def total_stock_value(products):
    total = 0

    for product in products:

        total = total + product["price"] * product["quantity"]
    return total


def main():
    products = load_products()
    print(total_stock_value(products))


main()


import csv


def save_students(students):
    with open("students.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


def load_students():
    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        students_records = []

        for detail in reader:
            detail["score"] = int(detail["score"])
            students_records.append(detail)
        return students_records


def amend_records(students, name, score):

    found = False

    for student in students:
        if student["name"] == name:
            student["score"] = score
            found = True
            break

    if not found:
        students.append({"name": name, "score": score})
    return students


students = load_students()
amend_records(students, "Kingsley", 95)
save_students(students)

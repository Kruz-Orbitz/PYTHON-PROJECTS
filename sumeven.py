def greater_than_five(numbers):
    new_list = []
    for number in numbers:
        if number > 5:
            new_list.append(number)
    return new_list
print(greater_than_five([2, 7, 4, 10, 5,8]))
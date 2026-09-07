"""
write a function that takes a list of numbers and returns a new
list containing only the numbers that are greater than average of the list.
"""
def above_average(numbers):
    new_list = []
    average = sum(numbers) / len(numbers)
    for number in numbers:
        if number > average:
            new_list.append(number)
    return new_list

print(above_average([2, 4, 6, 8]))
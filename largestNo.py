"""write a function that takes a list of numbers 
and return the largest number in the list without using max()
"""
def largest_number(numbers):
    largest_num = numbers[0]
    for number in numbers:
        if number > largest_num:
            largest_num = number
    return largest_num


print(largest_number([20, 2, 4, 10, 30, 22, 50])) 
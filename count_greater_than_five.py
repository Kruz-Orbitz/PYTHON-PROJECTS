def count_greater_than_five(numbers):
    count = 0
    for number in numbers:
        if number > 5:
            count = count + 1
    return count


print(count_greater_than_five([2, 7, 4, 10, 5, 8]))

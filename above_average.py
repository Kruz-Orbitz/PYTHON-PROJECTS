"""
Write a function called count_down() that uses a while 
loop to print the numbers from 5 down to 1.
"""
def count_down():
    number = 5
    while number >= 1:
        print(number)
        number = number - 1

count_down()
"""
you have a text called scores.txt. each lines contains a single
number (a player's score). write a program that opens the file
reads all the lines, loops through them, prints each score,
but only if its above 80, closes the file
"""

file = open("scores.txt", "r")

school_scores = file.readlines()

for score in school_scores:
    numbers = int(score)
    if numbers > 80:
        print(numbers)
file.close()
 
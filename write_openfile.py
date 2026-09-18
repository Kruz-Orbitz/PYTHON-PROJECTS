file = open("scores.txt", "w")

file.write("45\n")
file.write("75\n")
file.write("81\n")
file.write("63\n")
file.write("90\n")

file.close()

new_file = open("scores.txt", "r")

score_numbers = new_file.readlines()

total = 0

for score in score_numbers:
    numbers = int(score)
    total = total + numbers
print(total)
file.close()

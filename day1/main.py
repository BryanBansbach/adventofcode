file1 = open("day1.txt", "r")
Lines = file1.readlines()
numbers = []
value_sum = 0

for line in Lines:
    letter = [x for x in line if x.isdigit()]
    numbers.append(letter)

for num in numbers:
    number_string = str(num[0]) + str(num[- 1])
    value_sum += int(number_string)

print(value_sum)
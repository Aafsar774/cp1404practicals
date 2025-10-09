numbers = [3, 1, 4, 1, 5, 9, 2]

#Q1
numbers[0] = "ten"
print(numbers[0])

#Q2
numbers[6] = 1
print(numbers[6])

#Q3
del numbers[0:2]
print(numbers)

#Q4
if 9 in numbers:
    print("9 is in numbers")

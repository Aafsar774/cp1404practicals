# 1. Write a name to name.txt
name = input("Enter your name: ")
out_file = open("name.txt","w")
print(name, file=out_file)
out_file.close()

# 2. Read the name from name.txt
in_file = open("name.txt","r")
input_name = in_file.read().strip()
in_file.close()
print(f"Hi {input_name}!")

# 3. Read only the first two numbers from numbers.txt and print their sum total
with open("numbers.txt","r") as numbers_file:
    num1 = int(numbers_file.readline())
    num2 = int(numbers_file.readline())

    print(num1 + num2)

# 4. Print the total for all lines in numbers.txt
total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        line = line.strip()
        if line:                            # ignore any accidental blank lines
            total = total + int(line)
print(total)

"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

A ValueError will occur if the user enters something that is not an integer or a decimal

2. When will a ZeroDivisionError occur?

A ZeroDivisionError will occur if the user enters 0 for the denominator since division by zero is mathematically undefined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

You can avoid a ZeroDivisionError by checking if the denominator is zero before performing the division

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("The denominator cannot be zero.")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

"""When will a ValueError occur?
When will a ZeroDivisionError occur?
Could you change the code to avoid the possibility of a ZeroDivisionError?
If you could figure out the answer to question 3, then make this change now."""


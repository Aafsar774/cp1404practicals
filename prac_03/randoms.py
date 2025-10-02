"""What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

smallest = 5,  largest = 20

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?

smallest = 3,  largest = 9

What did you see on line 3?
Could line 2 have produced a 4?

yes

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

smallest = 2.5,  largest = 5.5

Write code, not a comment, to produce a random number between 1 and 100 inclusive."""

import random
random_number = random.randint(1, 100)
print(f"Random number = {random_number} ")

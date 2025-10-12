import random

num_per_pick = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    try:
        picks_count = int(input("How many quick picks? "))
    except ValueError:
        print("Please enter an integer.")
        return
    for i in range(picks_count):
        pick = generate_quick_pick()
        pick.sort()
        print(" ".join(f"{n:2d}" for n in pick))

def generate_quick_pick():
    numbers = []
    while len(numbers) < num_per_pick:
        n = random.randint(MIN_NUMBER, MAX_NUMBER)
        if n not in numbers:
            numbers.append(n)
    return numbers

main()

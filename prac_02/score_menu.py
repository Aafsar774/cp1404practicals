"""
CP1404- Practical
"""
def main():
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(score_status(score))
        elif choice == "S":
            print("*" * int(score))
        elif choice != "Q":
            print("Invalid option!")
    print("Farewell, thank you for using the program!")

def print_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! score must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score

def score_status(score):
    if score < 0 or score > 100:
        return "Invalid score!"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
main()

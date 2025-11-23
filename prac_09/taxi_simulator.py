MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")
    bill = 0.0

    choice = input(f"{MENU}\n>>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
        elif choice == "d":
            print("Drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill}")
        choice = input(f"{MENU}\n>>> ").lower()

    print(f"Total trip cost: ${bill}")
    print("Taxis are now:")

if __name__ == "__main__":
    main()
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100),SilverServiceTaxi("Limo", 100, 2),SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0.0

    choice = input(f"{MENU}\n>>> ").lower()
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
        elif choice == "d":
            print("Drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill}")
        choice = input(f"{MENU}\n>>> ").lower()

    print(f"Total trip cost: ${bill}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    print("Taxis available:")
    taxis_available = 0
    for taxi in taxis:
        print(f"{taxis_available} - {taxi}")
        taxis_available += 1

if __name__ == "__main__":
    main()
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
            choose_taxi(taxis)
        elif choice == "d":
            print("You need to choose a taxi before you can drive")
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

def choose_taxi(taxis):
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            taxi = taxis[taxi_choice]
            taxi.start_fare()
            return taxi
    except ValueError:
        print("Invalid taxi choice")
        return None

    print("Invalid taxi choice")
    return None


if __name__ == "__main__":
    main()
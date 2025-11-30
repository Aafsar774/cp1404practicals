from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100),SilverServiceTaxi("Limo", 100, 2),SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0.0
    active_taxi = 0

    choice = input(f"{MENU}\n>>> ").lower()
    while choice != "q":
        if choice == "c":
            chosen_taxi = choose_taxi(taxis)
            if chosen_taxi:
                active_taxi = chosen_taxi
        elif choice == "d":
            if active_taxi==0:
                print("You need to choose a taxi before you can drive")
            else:
                bill += drive_taxi(active_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")
        choice = input(f"{MENU}\n>>> ").lower()

    print(f"Total trip cost: ${bill:.2f}")
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
        if taxi_choice < 0 or taxi_choice >= len(taxis):
            print("Invalid taxi choice")
            return 0
        taxi = taxis[taxi_choice]
        taxi.start_fare()
        return taxi
    except ValueError:
        print("Invalid taxi choice")
        return 0

def drive_taxi(taxi):
    try:
        drive_distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0.0

    taxi.drive(drive_distance)
    trip_cost = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
    return trip_cost


if __name__ == "__main__":
    main()
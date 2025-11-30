from prac_09.unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("Car1", 100, 30)
    successful_tries = 0
    unsuccessful_tries = 0
    for tries in range(10):
       distance_driven = car.drive(1)
       if distance_driven > 0:
           successful_tries += 1
    unsuccessful_tries = 10 - successful_tries

    print(car)
    print(f"car drove {successful_tries} times and failed {unsuccessful_tries} times.")
if __name__ == "__main__":
    main()

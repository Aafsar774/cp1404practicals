from prac_09.unreliable_car import UnreliableCar
car = UnreliableCar("Car1",100,30)

successful_tries = 0
for tries in range(10):
    distance_driven = car.drive(1)
    if distance_driven > 0:
        successful_tries += 1

print(car)
print(f"car drove {successful_tries} times.")

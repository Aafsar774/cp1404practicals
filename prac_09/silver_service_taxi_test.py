from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    print(taxi.price_per_km)
    taxi.drive(18)
    print(taxi)
    assert taxi.get_fare() == 48.80
if __name__ == "__main__":
    main()

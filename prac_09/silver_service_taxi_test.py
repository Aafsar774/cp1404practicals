from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(taxi.price_per_km)

    print(taxi)
    assert taxi.get_fare() > 0
if __name__ == "__main__":
    main()

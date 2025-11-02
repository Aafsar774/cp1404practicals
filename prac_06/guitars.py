"""
Estimate: 60 minutes
Actual: 80 minutes
"""
from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        year = int(input("Year: ").strip())
        cost = float(input("Cost: $").strip())
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    if len(guitars) > 0:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
               vintage = " (vintage)"
            else:
               vintage = ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")
    else:
        print("No guitars!")

main()

from prac_07.guitar import Guitar

csv_file = "guitars.csv"


def main():
    guitars = load_csv(csv_file)
    loaded_guitars(guitars, "Loaded guitars:")

    guitars.sort()
    loaded_guitars(guitars, "Guitars sorted by year from oldest to newest:")


    new_guitars = add_guitars_from_user()
    if new_guitars:
        guitars.extend(new_guitars)
        guitars.sort()
        loaded_guitars(guitars, "All guitars including new entries:")

def load_csv(filename):
    guitars = []
    with open(filename, "r", encoding="utf-8") as guitars_file:
        for line in guitars_file:
            line = line.strip()
            name, year, cost = line.split(",")
            name = name.strip()
            year = year.strip()
            cost = cost.strip()
            guitars.append(Guitar(name=name, year=int(year), cost=float(cost)))
    return guitars


def loaded_guitars(guitars, title):
    print(title)
    for item in guitars:
        print(item)
    print()


def add_guitars_from_user():
    print("Enter new guitars:")
    new_guitars = []
    name = input("Name: ").strip()
    year = int(input("Year: ").strip())
    cost = float(input("Cost: $").strip())
    more_guitars = Guitar(name=name, year=year, cost=cost)
    new_guitars.append(more_guitars)
    print(f"{more_guitars} added.\n")

    return new_guitars

main()

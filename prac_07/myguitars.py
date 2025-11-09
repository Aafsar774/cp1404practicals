from prac_07.guitar import Guitar

csv_file = "guitars.csv"


def main():
    guitars = load_csv(csv_file)
    loaded_guitars(guitars, "Loaded guitars:")

    guitars.sort()
    loaded_guitars(guitars, "Guitars sorted by year from oldest to newest:")


    new_guitars = get_guitars_from_user()
    guitars.extend(new_guitars)
    guitars.sort()
    loaded_guitars(guitars, "All guitars:")
    save_new_guitars(csv_file, guitars)
    print(f"Saved {len(guitars)} guitars to {csv_file}.")

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


def get_guitars_from_user():
    print("Enter new guitars:")
    new_guitars = []
    name = input("Name: ").strip()
    year = int(input("Year: ").strip())
    cost = float(input("Cost: $").strip())
    more_guitars = Guitar(name=name, year=year, cost=cost)
    new_guitars.append(more_guitars)
    print(f"{more_guitars} added.\n")

    return new_guitars

def save_new_guitars(filename, guitars):
    with open(filename, "w", encoding="utf-8", newline="") as guitars_file:
        for guitar in guitars:
            guitars_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

main()

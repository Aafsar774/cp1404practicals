from prac_07.guitar import Guitar

csv_file = "guitars.csv"

def main():
    guitars = load_csv(csv_file)
    loaded_guitars(guitars, "Loaded guitars:")

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



main()

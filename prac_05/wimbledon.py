"""
Estimate: 60 minutes
Actual: 90 minutes
"""

import csv

FILENAME = "wimbledon.csv"

def read_csv_data(filename):
    with open(filename, "r", encoding="utf-8-sig", newline="") as in_file:
        reader = csv.reader(in_file)
        header = next(reader)
        rows = list(reader)
    return header, rows

def count_champions(rows, header):
    champion_idx = header.index("Champion")
    champion_to_wins = {}
    for row in rows:
        champion = row[champion_idx]
        if champion in champion_to_wins:
            champion_to_wins[champion] = champion_to_wins[champion] + 1
        else:
            champion_to_wins[champion] = 1
    return champion_to_wins

def champion_countries(rows, header):
    country_idx = header.index("Country")
    countries = set()
    for row in rows:
        countries.add(row[country_idx])
    return countries

def main():
    header, rows = read_csv_data(FILENAME)
    champion_to_wins = count_champions(rows, header)
    countries = champion_countries(rows, header)

    print("Wimbledon Champions:")
    for champion in sorted(champion_to_wins.keys()):
        print(f"{champion} {champion_to_wins[champion]}")

    print()
    sorted_countries = sorted(countries)
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))

main()

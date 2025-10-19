"""
Estimate: 60 minutes
Actual:
"""

import csv

FILENAME = "wimbledon.csv"

def main():
    with open(FILENAME, "r", encoding="utf-8-sig", newline="") as in_file:
        reader = csv.reader(in_file)
        header = next(reader)
        rows = list(reader)

    champion_idx = header.index("Champion")

    champion_to_wins = {}
    for row in rows:
        champion = row[champion_idx]
        if champion in champion_to_wins:
            champion_to_wins[champion] = champion_to_wins[champion] + 1
        else:
            champion_to_wins[champion] = 1

    print("Wimbledon Champions:")
    for champion in sorted(champion_to_wins.keys()):
        print(f"{champion} {champion_to_wins[champion]}")

main()

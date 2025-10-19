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
        rows = list(reader)            # list of lists

    print(rows , header)

main()

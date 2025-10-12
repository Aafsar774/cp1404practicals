"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    records = read_file(FILENAME)
    print(records)
    display_subject_details(records)

def read_file(filename=FILENAME):
    records = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])  # convert student count to int
        records.append(parts)
    input_file.close()
    return records

def display_subject_details(records):
    for subject_code, lecturer, student_count in records:
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

main()

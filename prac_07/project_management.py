from datetime import datetime
from prac_07.project import Project

text_file = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(text_file)
    print(f"Loaded {len(projects)} projects from {text_file}")

    while True:

         print_menu()
         choice = input(">>> ").strip().lower()
         if choice == "q":
             print("Thank you for using custom-built project management software.")
             break
         elif choice == "l":
             print("Load projects (not implemented yet)")
         elif choice == "s":
             print("Save projects (not implemented yet)")
         elif choice == "d":
             print("Display projects (not implemented yet)")
         elif choice == "f":
             print("Filter by date (not implemented yet)")
         elif choice == "a":
             print("Add new project (not implemented yet)")
         elif choice == "u":
             print("Update project (not implemented yet)")
         else:
             print("Invalid menu choice.")


def load_projects(filename):
    projects = []
    with open(filename, "r", encoding="utf-8") as file:
        file.readline()
        for line in file:
            line = line.strip()
            parts = line.split("\t")
            name = parts[0].strip()
            start_date = datetime.strptime(parts[1].strip(), "%d/%m/%Y").date()
            priority = int(parts[2].strip())
            cost_estimate = float(parts[3].strip())
            completion_percentage = int(parts[4].strip())
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def print_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


main()

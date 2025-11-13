from datetime import datetime
from prac_07.project import Project

text_file = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")

    while True:

         print_menu()
         choice = input(">>> ").strip().lower()
         if choice == "q":
             print("Thank you for using custom-built project management software.")
             break
         elif choice == "l":
             projects=load_projects(text_file)
             print(f"Loaded {len(projects)} projects from {text_file}")
         elif choice == "s":
             print("Save projects")
         elif choice == "d":
             display_projects(projects)
         elif choice == "f":
             filter_by_date(projects)
         elif choice == "a":
             print("Add new project")
         elif choice == "u":
             print("Update project")
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

def display_projects(projects):
    incomplete = []
    complete = []
    for item in projects:
        if item.is_complete():
            complete.append(item)
        else:
            incomplete.append(item)
    incomplete.sort()
    complete.sort()

    print("Incomplete projects:")
    for project in incomplete:
        print(" ", project)
    print("Completed projects:")
    for project in complete:
        print(" ", project)

def get_start_date(project):
    return project.start_date

def filter_by_date(projects):
    date_filter = input("Show projects that start after date (dd/mm/yyyy): ").strip()
    starts = datetime.strptime(date_filter, "%d/%m/%Y").date()

    filtered = []
    for project in projects:
        if project.project_date(starts):
            filtered.append(project)

    filtered.sort(key=get_start_date)

    for project in filtered:
        print(project)

main()

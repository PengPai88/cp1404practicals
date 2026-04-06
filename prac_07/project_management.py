"""
CP1404/CP5632 Practical - Project Management Program.
Load/save projects from TXT/CSV, menu-driven interface with all required features.
Estimated time to complete: 180 minutes
Actual time to complete: 160 minutes
"""
import csv
from datetime import datetime, date
from project import Project

DEFAULT_FILENAME = "projects.txt"


def load_projects(filename):
    """Load projects from a tab-delimited text file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, 'r') as in_file:
            in_file.readline()  # Consume header
            for line in in_file:
                line = line.strip()
                if not line:
                    continue
                # Split tab-delimited line
                parts = line.split('\t')
                # Parse values and convert types
                name = parts[0]
                start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
                priority = int(parts[2])
                cost_estimate = float(parts[3])
                completion_percent = int(parts[4])
                # Create Project object
                projects.append(Project(name, start_date, priority, cost_estimate, completion_percent))
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found - starting with empty project list.")
    return projects


def save_projects(filename, projects):
    """Save a list of Project objects to a tab-delimited text file."""
    with open(filename, 'w') as out_file:
        # Write header
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        # Write project data
        for project in projects:
            start_date_str = project.start_date.strftime("%d/%m/%Y")
            out_file.write(
                f"{project.name}\t{start_date_str}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percent}\n"
            )
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    """Display projects split into incomplete/completed, sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    completed = [p for p in projects if p.is_complete()]
    # Sort both lists by priority
    incomplete.sort()
    completed.sort()

    print("\nIncomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("\nCompleted projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects that start after a user-specified date, sorted by start date."""
    while True:
        date_input = input("\nShow projects that start after date (dd/mm/yyyy): ").strip()
        try:
            filter_date = datetime.strptime(date_input, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Invalid date format - please use dd/mm/yyyy.")

    # Filter projects
    filtered = [p for p in projects if p.start_date >= filter_date]
    # Sort by start date
    filtered.sort(key=lambda x: x.start_date)

    # Display
    for project in filtered:
        print(project)


def get_new_project():
    """Prompt user for new project details and return a Project object."""
    print("\nLet's add a new project")
    name = input("Name: ").strip()
    # Get start date
    while True:
        date_input = input("Start date (dd/mm/yyyy): ").strip()
        try:
            start_date = datetime.strptime(date_input, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Invalid date format - please use dd/mm/yyyy.")
    # Get priority
    while True:
        priority_input = input("Priority: ").strip()
        try:
            priority = int(priority_input)
            break
        except ValueError:
            print("Please enter a valid integer for priority.")
    # Get cost estimate
    while True:
        cost_input = input("Cost estimate: $").strip()
        try:
            cost_estimate = float(cost_input)
            break
        except ValueError:
            print("Please enter a valid number for cost estimate.")
    # Get completion percentage
    while True:
        comp_input = input("Percent complete: ").strip()
        try:
            completion_percent = int(comp_input)
            break
        except ValueError:
            print("Please enter a valid integer for percentage complete.")

    return Project(name, start_date, priority, cost_estimate, completion_percent)


def update_project(projects):
    """Allow user to select a project and update its completion percentage/priority."""
    # Display project list with indices
    print("\nProjects:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    # Get valid project index
    while True:
        try:
            choice = int(input("Project choice: "))
            if 0 <= choice < len(projects):
                selected = projects[choice]
                break
            else:
                print(f"Please enter a number between 0 and {len(projects)-1}.")
        except ValueError:
            print("Please enter a valid integer.")

    # Display selected project
    print(selected)
    # Get new completion percentage (allow blank)
    comp_input = input("New Percentage: ").strip()
    new_completion = int(comp_input) if comp_input else None
    # Get new priority (allow blank)
    prio_input = input("New Priority: ").strip()
    new_priority = int(prio_input) if prio_input else None
    # Update project
    selected.update_details(new_completion, new_priority)
    print(f"Updated project: {selected}")


def main_menu():
    """Display main menu and return user's choice (uppercase)."""
    print("\n- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")
    return input(">>> ").upper()


def main():
    """Main menu-driven function for Project Management Program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)

    while True:
        choice = main_menu()
        if choice == 'L':
            filename = input("Enter filename to load: ").strip()
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Enter filename to save: ").strip()
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            projects.append(get_new_project())
        elif choice == 'U':
            if projects:
                update_project(projects)
            else:
                print("No projects to update!")
        elif choice == 'Q':
            # Ask to save to default file
            save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").lower()
            if save_choice in ['y', 'yes']:
                save_projects(DEFAULT_FILENAME, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice - please try again.")


if __name__ == "__main__":
    main()
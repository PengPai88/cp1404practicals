"""
CP1404/CP5632 Practical - My Guitars program.
Read guitars from csv, allow user to add new guitars, sort, and save back to csv.
"""
import csv
from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as in_file:
            reader = csv.reader(in_file)
            for row in reader:
                if row:  # Skip empty rows
                    name = row[0].strip()
                    year = int(row[1])
                    cost = float(row[2])
                    guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"File {filename} not found - starting with empty list.")
    return guitars


def save_guitars(filename, guitars):
    """Save a list of Guitar objects to a CSV file."""
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def get_new_guitar():
    """Prompt user for new guitar details and return a Guitar object."""
    print("\nEnter new guitar details:")
    name = input("Name: ").strip()
    while True:
        try:
            year = int(input("Year: "))
            break
        except ValueError:
            print("Please enter a valid integer for year.")
    while True:
        try:
            cost = float(input("Cost: $"))
            break
        except ValueError:
            print("Please enter a valid number for cost.")
    return Guitar(name, year, cost)


def main():
    """Main function for My Guitars program."""
    FILENAME = "guitars.csv"
    guitars = load_guitars(FILENAME)

    # Display loaded guitars
    if guitars:
        print("\nLoaded Guitars:")
        for guitar in guitars:
            print(guitar)
    else:
        print("\nNo guitars loaded.")

    # Allow user to add new guitars
    while True:
        add_more = input("\nAdd a new guitar? (y/n): ").lower()
        if add_more != 'y':
            break
        guitars.append(get_new_guitar())

    # Sort guitars by year (oldest to newest)
    guitars.sort()

    # Display sorted guitars
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

    # Save guitars back to CSV
    save_guitars(FILENAME, guitars)
    print(f"\nGuitars saved to {FILENAME}")


if __name__ == "__main__":
    main()
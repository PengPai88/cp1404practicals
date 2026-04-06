"""
Demo for using pickle and json to save and load objects.
CP1404/CP5632 Practical
"""

import pickle
import json
from datetime import datetime


class Person:
    """Simple demo class for testing pickling."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.created = datetime.now()

    def __str__(self):
        return f"{self.name} ({self.age}) - created {self.created}"


def run_pickle_demo():
    """Demonstrate pickling and unpickling objects."""
    print("=== Pickle Demo ===")

    # Create some objects
    people = [
        Person("Alice", 20),
        Person("Bob", 21),
        Person("Charlie", 19)
    ]

    # Save (pickle) objects to a binary file
    with open("people.pkl", "wb") as out_file:
        pickle.dump(people, out_file)
    print("Saved objects to people.pkl")

    # Load (unpickle) objects from file
    with open("people.pkl", "rb") as in_file:
        loaded_people = pickle.load(in_file)

    print("\nLoaded objects:")
    for person in loaded_people:
        print(person)

    # Pickle single object
    test = Person("Test", 99)
    with open("single.pkl", "wb") as f:
        pickle.dump(test, f)

    with open("single.pkl", "rb") as f:
        loaded_test = pickle.load(f)
    print("\nSingle loaded object:", loaded_test)


def run_json_demo():
    """Demonstrate JSON saving/loading (cannot save datetime objects)."""
    print("\n=== JSON Demo (cannot serialize datetime objects) ===")
    person = Person("JSON Test", 50)

    # Convert to dict first for JSON
    person_dict = {
        "name": person.name,
        "age": person.age,
        "created": str(person.created)
    }

    with open("person.json", "w") as f:
        json.dump(person_dict, f, indent=4)

    with open("person.json") as f:
        loaded = json.load(f)

    print("Loaded JSON dict:", loaded)


def main():
    run_pickle_demo()
    run_json_demo()
    print("\nAll demos complete!")


if __name__ == '__main__':
    main()
"""
CP1404/CP5632 Practical - Guitar class with __lt__ method for sorting by year.
Represent a guitar with name, year, and cost attributes.
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Less than operator: Compare guitars by year (for sorting)."""
        return self.year < other.year

    def get_age(self):
        """Calculate and return the age of the guitar (2024 as current year)."""
        return 2024 - self.year

    def is_vintage(self):
        """Return True if guitar is vintage (50+ years old)."""
        return self.get_age() >= 50


def run_tests():
    """Test Guitar class methods and __lt__ operator."""
    guitar1 = Guitar("Fender Stratocaster", 2014, 765.40)
    guitar2 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar3 = Guitar("Line 6 JTV-59", 2010, 1512.90)

    print(guitar1)
    print(guitar2)
    print(guitar3)

    # Test age calculation
    assert guitar1.get_age() == 10
    assert guitar2.get_age() == 102
    assert guitar3.get_age() == 14

    # Test vintage check
    assert guitar1.is_vintage() is False
    assert guitar2.is_vintage() is True
    assert guitar3.is_vintage() is False

    # Test sorting
    guitars = [guitar1, guitar2, guitar3]
    guitars.sort()
    assert guitars == [guitar2, guitar3, guitar1]
    print("\nSorted by year:")
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    run_tests()
"""
CP1404/CP5632 Practical - Project class for Project Management Program.
Estimated time to complete: 180 minutes
Actual time to complete: 160 minutes
"""
from datetime import date


class Project:
    """Represent a Project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date  # datetime.date object
        self.priority = priority  # integer
        self.cost_estimate = cost_estimate  # float
        self.completion_percent = completion_percent  # integer

    def __str__(self):
        """Return formatted string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percent}%")

    def __lt__(self, other):
        """Less than operator: Compare projects by priority (for sorting)."""
        return self.priority < other.priority

    def is_complete(self):
        """Helper method: Check if project is 100% complete."""
        return self.completion_percent == 100

    def update_details(self, new_completion=None, new_priority=None):
        """Helper method: Update completion percentage and/or priority (if provided)."""
        if new_completion is not None:
            self.completion_percent = new_completion
        if new_priority is not None:
            self.priority = new_priority


def run_tests():
    """Test Project class methods and __lt__ operator."""
    from datetime import datetime
    date1 = datetime.strptime("12/09/2021", "%d/%m/%Y").date()
    date2 = datetime.strptime("20/07/2022", "%d/%m/%Y").date()
    project1 = Project("Build Car Park", date1, 2, 600000.0, 95)
    project2 = Project("Organise Pantry", date2, 1, 25.0, 55)

    print(project1)
    print(project2)

    # Test is_complete
    assert project1.is_complete() is False
    project1.update_details(new_completion=100)
    assert project1.is_complete() is True

    # Test sorting by priority
    projects = [project1, project2]
    projects.sort()
    assert projects == [project2, project1]


if __name__ == "__main__":
    run_tests()
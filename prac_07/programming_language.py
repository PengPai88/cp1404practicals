"""
CP1404/CP5632 Practical - Programming Language class with Pointer Arithmetic field.
Represent information about a programming language, including support for pointer arithmetic.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Provide string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}, Pointer Arithmetic={self.pointer_arithmetic}")

    def __repr__(self):
        """Provide developer-friendly representation of a ProgrammingLanguage."""
        return f"{vars(self)}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def has_pointer_arithmetic(self):
        """Helper method: Check if language supports pointer arithmetic."""
        return self.pointer_arithmetic


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983, True)
    print(python)
    print(c_plus_plus)
    assert python.is_dynamic() is True
    assert c_plus_plus.has_pointer_arithmetic() is True
    assert python.has_pointer_arithmetic() is False


if __name__ == "__main__":
    run_tests()
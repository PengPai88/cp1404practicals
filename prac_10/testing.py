import doctest
from car import Car


def repeat_string(s, n):
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("python is fun")
    'Python is fun.'
    """
    if not phrase:
        return ""
    sentence = phrase.capitalize()
    if not sentence.endswith("."):
        sentence += "."
    return sentence


def run_tests():
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car1 = Car(fuel=10)
    assert car1.fuel == 10

    car2 = Car()
    assert car2.fuel == 0


run_tests()
doctest.testmod()
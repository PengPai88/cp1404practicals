"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
Updated to handle Pointer Arithmetic field in ProgrammingLanguage class.
"""
import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    in_file = open('languages.csv', 'r')
    # File format is like: Language,Typing,Reflection,Year,PointerArithmetic
    in_file.readline()  # Consume header
    for line in in_file:
        # Strip newline and split into parts
        parts = line.strip().split(',')
        # Convert string values to appropriate booleans
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"
        # Construct ProgrammingLanguage object
        language = ProgrammingLanguage(
            parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic
        )
        languages.append(language)
    in_file.close()
    # Display all languages
    for language in languages:
        print(language)


def using_csv():
    """Language file reader version using the csv module."""
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()


def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    reader = csv.reader(in_file)
    for row in reader:
        language = Language._make(row)
        print(repr(language))
    in_file.close()


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    in_file = open("languages.csv", "r")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))
    in_file.close()


if __name__ == "__main__":
    main()
    # using_csv()
    # using_namedtuple()
    # using_csv_namedtuple()
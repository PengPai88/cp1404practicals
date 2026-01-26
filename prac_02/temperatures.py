

def main():

    print("C - Convert Celsius to Fahrenheit")
    print("F - Convert Fahrenheit to Celsius")
    print("Q - Quit")

    choice = input("Choose an option: ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")

        print("\nC - Convert Celsius to Fahrenheit")
        print("F - Convert Fahrenheit to Celsius")
        print("Q - Quit")
        choice = input("Choose an option: ").upper()

    print("Goodbye!")


def celsius_to_fahrenheit(celsius):

    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):

    return 5 / 9 * (fahrenheit - 32)


main()

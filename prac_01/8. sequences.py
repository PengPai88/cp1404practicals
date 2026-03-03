def display_sequence_menu():
    print("\n1. Show even numbers from x to y")
    print("2. Show odd numbers from x to y")
    print("3. Show squares of numbers from x to y")
    print("4. Exit")

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer!")

def main():
    x = get_valid_integer("Enter start number (x): ")
    y = get_valid_integer("Enter end number (y): ")
    if x > y:
        x, y = y, x

    display_sequence_menu()
    choice = get_valid_integer("Enter your choice (1-4): ")

    while choice != 4:
        if choice == 1:
            print("Even numbers:", end=' ')
            for num in range(x, y + 1):
                if num % 2 == 0:
                    print(num, end=' ')
        elif choice == 2:
            print("Odd numbers:", end=' ')
            for num in range(x, y + 1):
                if num % 2 != 0:
                    print(num, end=' ')
        elif choice == 3:
            print("Squares:", end=' ')
            for num in range(x, y + 1):
                print(num** 2, end=' ')
        else:
            print("Invalid choice! Please enter 1-4.")

        display_sequence_menu()
        choice = get_valid_integer("Enter your choice (1-4): ")

    print("Exiting program...")

if __name__ == "__main__":
    main()
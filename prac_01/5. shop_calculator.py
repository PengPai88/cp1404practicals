

def calculate_total_price():
    while True:
        try:
            number_of_items = int(input("Number of items: "))
            if number_of_items < 0:
                print("Invalid number of items!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer!")

    total = 0.0
    for i in range(number_of_items):
        while True:
            try:
                price = float(input("Price of item: "))
                if price < 0:
                    print("Price cannot be negative!")
                else:
                    total += price
                    break
            except ValueError:
                print("Please enter a valid number!")

    if total > 100:
        total *= 0.9

    print(f"Total price for {number_of_items} items is ${total:.2f}")

if __name__ == "__main__":
    calculate_total_price()
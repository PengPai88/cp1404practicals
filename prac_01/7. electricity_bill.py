TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

def calculate_electricity_bill():
    print("Electricity bill estimator 2.0")
    while True:
        tariff_choice = input("Which tariff? 11 or 31: ")
        if tariff_choice == "11":
            cents_per_kwh = TARIFF_11 * 100
            break
        elif tariff_choice == "31":
            cents_per_kwh = TARIFF_31 * 100
            break
        else:
            print("Invalid tariff choice! Please enter 11 or 31.")

    while True:
        try:
            daily_use = float(input("Enter daily use in kWh: "))
            if daily_use < 0:
                print("Daily use cannot be negative!")
            else:
                break
        except ValueError:
            print("Please enter a valid number!")

    while True:
        try:
            billing_days = int(input("Enter number of billing days: "))
            if billing_days < 0:
                print("Billing days cannot be negative!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer!")

    total_cents = cents_per_kwh * daily_use * billing_days
    total_dollars = total_cents / 100
    print(f"Estimated bill: ${total_dollars:.2f}")

if __name__ == "__main__":
    calculate_electricity_bill()
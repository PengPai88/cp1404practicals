def main():
    number_of_months = int(input("How many months? "))
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_report(incomes)

def print_report(incomes):
    print("\nIncome Report")
    print("-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month  {month} - Income: ${income:9.2f} Total: ${total:9.2f}")

if __name__ == "__main__":
    main()
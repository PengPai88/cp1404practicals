def calculate_bonus(sales):
    if sales < 1000:
        return sales * 0.1
    else:
        return sales * 0.15

def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        bonus = calculate_bonus(sales)
        print(f"Bonus: ${bonus:.2f}")
        sales = float(input("Enter sales: $"))
    print("Exiting program...")

if __name__ == "__main__":
    main()
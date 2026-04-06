from car import Car

MENU = "d) drive\nr) refuel\nq) quit"

def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(name, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()

    while choice != "q":
        if choice == "d":
            distance = int(input("How many km do you wish to drive? "))
            while distance < 0:
                print("Distance must be >= 0")
                distance = int(input("How many km do you wish to drive? "))
            driven = car.drive(distance)
            if car.fuel == 0:
                print(f"The car drove {driven}km and ran out of fuel.")
            else:
                print(f"The car drove {driven}km.")
        elif choice == "r":
            fuel = int(input("How many units of fuel do you want to add to the car? "))
            while fuel < 0:
                print("Fuel amount must be >= 0")
                fuel = int(input("How many units of fuel do you want to add to the car? "))
            car.add_fuel(fuel)
            print(f"Added {fuel} units of fuel.")
        else:
            print("Invalid choice")

        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()

    print(f"\nGood bye {car.name}'s driver.")

if __name__ == '__main__':
    main()
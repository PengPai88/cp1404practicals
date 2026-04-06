from car import Car

def main():
    limo = Car("Limousine", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo)

if __name__ == '__main__':
    main()
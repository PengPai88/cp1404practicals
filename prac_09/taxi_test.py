"""Test Taxi class functionality."""
from prac_09.taxi import Taxi


def main():
    """Test Taxi class."""
    # Create taxi with name "Prius 1", fuel 100 (price_per_km is class variable)
    my_taxi = Taxi("Prius 1", 100)

    # Drive 40km
    my_taxi.drive(40)

    # Print details and fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart fare and drive 100km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print updated details and fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
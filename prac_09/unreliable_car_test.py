"""Test UnreliableCar class functionality."""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar with multiple drive attempts."""
    # Create cars with different reliability
    reliable_car = UnreliableCar("Reliable", 100, 90)
    unreliable_car = UnreliableCar("Unreliable", 100, 10)

    # Test driving each car multiple times
    for i in range(10):
        print(f"\nAttempt {i + 1}:")
        print(f"{reliable_car.name} drove {reliable_car.drive(10)}km")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(10)}km")

    # Statistical test (1000 attempts)
    print("\n\nStatistical Test (1000 attempts):")
    total_reliable = 0
    total_unreliable = 0
    for _ in range(1000):
        total_reliable += reliable_car.drive(1)
        total_unreliable += unreliable_car.drive(1)

    print(f"90% reliable car drove {total_reliable}km (expected ~900)")
    print(f"10% reliable car drove {total_unreliable}km (expected ~100)")


if __name__ == "__main__":
    main()
"""Test SilverServiceTaxi class functionality."""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi with assertions."""
    # Create SilverServiceTaxi with fanciness 2
    taxi = SilverServiceTaxi("Test Taxi", 100, 2)

    # Test 18km trip (expected fare: (18 * 1.23 * 2) + 4.50 = 48.78 → rounded to 48.80)
    taxi.drive(18)
    fare = taxi.get_fare()
    print(taxi)
    print(f"Fare for 18km trip: ${fare:.2f}")
    assert fare == 48.80, f"Expected fare 48.80, got {fare}"

    # Test reset fare
    taxi.start_fare()
    taxi.drive(10)
    expected_fare = (10 * 1.23 * 2) + 4.50
    expected_fare = round(expected_fare * 10) / 10
    assert taxi.get_fare() == expected_fare, "Fare calculation error after reset"
    print(f"\nFare for 10km trip (reset): ${taxi.get_fare():.2f}")
    print("All tests passed!")


if __name__ == "__main__":
    main()
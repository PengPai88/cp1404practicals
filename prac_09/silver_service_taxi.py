"""
CP1404/CP5632 Practical
SilverServiceTaxi class inheriting from Taxi
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with fanciness and flagfall."""
    flagfall = 4.50  # Class variable for flagfall charge

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        # Scale price_per_km by fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate fare including flagfall (rounded to 10c)."""
        # Use parent class fare calculation + flagfall
        base_fare = super().get_fare()
        total_fare = base_fare + self.flagfall
        return round(total_fare * 10) / 10  # Maintain 10c rounding
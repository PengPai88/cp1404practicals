"""
CP1404/CP5632 Practical
UnreliableCar class inheriting from Car
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that has a reliability factor."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability  # 0-100 float

    def drive(self, distance):
        """
        Drive the car only if a random number is less than reliability.
        Return distance driven (0 if not reliable).
        """
        random_chance = random.randint(0, 100)
        if random_chance < self.reliability:
            # Drive normally
            distance_driven = super().drive(distance)
        else:
            # Car fails to drive
            distance_driven = 0
        return distance_driven
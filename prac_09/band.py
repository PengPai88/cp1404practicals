"""Band class for managing musicians."""


class Band:
    """Represent a Band consisting of multiple Musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of the Band."""
        musician_strings = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"

    def add(self, musician):
        """Add a Musician to the Band."""
        self.musicians.append(musician)

    def play(self):
        """Return string of each musician playing their instrument (or needing one)."""
        play_strings = [musician.play() for musician in self.musicians]
        return "\n".join(play_strings)
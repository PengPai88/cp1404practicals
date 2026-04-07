"""
CP1404/CP5632 Practical
Tree classes (from lecture, used for inheritance practical)
"""
import random

DEFAULT_TRUNK_HEIGHT = 2
DEFAULT_LEAVES = 6


class Tree:
    """Represent a tree with a trunk and leaves."""

    def __init__(self):
        """Constructor for a Tree object."""
        self._trunk_height = DEFAULT_TRUNK_HEIGHT
        self._number_of_leaves = DEFAULT_LEAVES

    def __str__(self):
        """Return string representation of the tree."""
        return self.get_ascii_leaves() + self.get_ascii_trunk()

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        result = ""
        leaves = self._number_of_leaves
        if leaves % 3 > 0:
            result += "#" * (leaves % 3) + "\n"
            leaves -= leaves % 3
        while leaves > 0:
            result += "###\n"
            leaves -= 3
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        result = ""
        for _ in range(self._trunk_height):
            result += " |\n"
        return result

    def grow(self, sunlight, water):
        """Grow a tree based on sunlight and water."""
        self._trunk_height += random.randint(0, water)
        self._number_of_leaves += random.randint(0, sunlight)


class EvenTree(Tree):
    """Represent a tree that grows leaves in even multiples of 3."""

    def grow(self, sunlight, water):
        """Grow evenly (clean rows)."""
        super().grow(sunlight, water)
        # Ensure leaves are a multiple of 3
        self._number_of_leaves -= self._number_of_leaves % 3


class UpsideDownTree(Tree):
    """Represent a tree that looks upside down."""

    def __str__(self):
        """Return upside-down string representation."""
        return self.get_ascii_trunk() + self.get_ascii_leaves()


class WideTree(Tree):
    """Represent a wide tree: rows of 6 leaves, double-width trunk."""

    def get_ascii_leaves(self):
        """Return leaves in rows of 6."""
        result = ""
        leaves = self._number_of_leaves
        if leaves % 6 > 0:
            result += "#" * (leaves % 6) + "\n"
            leaves -= leaves % 6
        while leaves > 0:
            result += "######\n"
            leaves -= 6
        return result

    def get_ascii_trunk(self):
        """Return double-width trunk."""
        result = ""
        for _ in range(self._trunk_height):
            result += "  ||  \n"
        return result


class QuickTree(Tree):
    """A tree that grows much faster (no randomness)."""

    def grow(self, sunlight, water):
        """Grow instantly based on full sunlight/water."""
        self._trunk_height += water
        self._number_of_leaves += sunlight


class FruitTree(Tree):
    """A tree with fruit (dots) above leaves."""

    def __init__(self):
        """Initialise with fruit."""
        super().__init__()
        self.fruit = 1

    def grow(self, sunlight, water):
        """Grow normally plus random fruit gain/loss."""
        super().grow(sunlight, water)
        if random.randint(1, 2) == 1:
            self.fruit += 1
        if random.randint(1, 5) == 1 and self.fruit > 0:
            self.fruit -= 1

    def get_ascii_leaves(self):
        """Return fruit dots first, then leaves."""
        result = ""
        # Fruit
        fruit = self.fruit
        if fruit % 3 > 0:
            result += "." * (fruit % 3) + "\n"
            fruit -= fruit % 3
        while fruit > 0:
            result += "...\n"
            fruit -= 3
        # Leaves
        leaves = self._number_of_leaves
        if leaves % 3 > 0:
            result += "#" * (leaves % 3) + "\n"
            leaves -= leaves % 3
        while leaves > 0:
            result += "###\n"
            leaves -= 3
        return result


class PineTree(Tree):
    """A pine tree with triangular star shape."""

    def __init__(self):
        """Initialise with 4 leaves (1+3)."""
        super().__init__()
        self._number_of_leaves = 4

    def grow(self, sunlight, water):
        """Grow trunk normally, add full triangular rows of leaves."""
        self._trunk_height += random.randint(0, water)
        if random.randint(0, sunlight) > 2:
            total = self._number_of_leaves
            row = 1
            while total > 0:
                total -= row
                row += 2
            self._number_of_leaves += row

    def get_ascii_leaves(self):
        """Return triangular star leaves."""
        result = ""
        total = self._number_of_leaves
        row = 1
        while total > 0:
            total -= row
            spaces = " " * ((self._number_of_leaves - row) // 2)
            result += spaces + "*" * row + "\n"
            row += 2
        return result

    def get_ascii_trunk(self):
        """Return centered trunk."""
        result = ""
        max_width = self._number_of_leaves if self._number_of_leaves % 2 else self._number_of_leaves - 1
        spaces = " " * ((max_width - 1) // 2)
        for _ in range(self._trunk_height):
            result += spaces + "|\n"
        return result
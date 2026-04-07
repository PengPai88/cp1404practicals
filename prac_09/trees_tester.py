"""
CP1404/CP5632 Practical
Testing/example client code for trees classes
When you complete all the subclasses, you'll see that they behave differently.

"""
from trees import Tree, EvenTree, UpsideDownTree, WideTree, QuickTree, FruitTree, PineTree

TREES = [Tree(), EvenTree(), UpsideDownTree(), WideTree(), QuickTree(), FruitTree(), PineTree()]


def main():
    """Demo code to show trees growing."""
    print("Initial trees:")
    for tree in TREES:
        print(type(tree).__name__)
        print(tree)

    print("Growing...")
    for tree in TREES:
        tree.grow(4, 2)

    print("Trees after growing:")
    for tree in TREES:
        print(type(tree).__name__)
        print(tree)


if __name__ == '__main__':
    main()

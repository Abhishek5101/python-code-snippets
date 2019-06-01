class Inventory:
    """
    This is our Parent class
    """

    def __init__(self):
        print("Parent class running __init__()")
        self.slots = []

    def add_item(self, item):
        # We DEFINE add_items, it takes an argument named item
        print("Inventory - Parent class is running its code.")
        self.slots.append(item)


class SortedInventory(Inventory):
    """
    We are inheriting Inventory,
    so Inventory is the Parent class.

    We inherit its already existing abilities; like the method add_item.
    That means add_item is inherited and already exists.
    """

    # Added these lines.
    def add_item(self, item):
        # the moment I redefine this `add_item` inside the child class
        # i am REPLACING the implementation that I inherited from Inventory.
        print("This is running in the Child Class - SortedInventory.")
        self.slots.append(item)  # even if the implementation is the same.


if __name__ == '__main__':
    inventory = SortedInventory()
    inventory.add_item(3)

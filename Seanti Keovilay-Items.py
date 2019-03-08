class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Inventory(Item):
    def __init__(self, name):
        super(Inventory, self).__init__(name, 0)
        self.items = []
        self.space = 100

    def add_item(self, item):
        self.items.append(item)
        self.space -= 100
        print("You added a item in the bag.")
        print(self.space)

    def remove_item(self, item):
        self.items.remove(item)
        self.space += 100
        print("You remove the item.")
        print(self.space)

    def combine_item(self, item1, item2):
        if isinstance(item1, Flashlight) and isinstance(item2, Battery):
            item1.batteries = item2
        if isinstance(item2, Flashlight) and isinstance(item1, Battery):
            item2.batteries = item1
            print("You combine %s and %d together.")


class Flashlight(Item):
    def __init__(self):
        super(Flashlight, self).__init__("Flashlight", 5)
        self.batteries = None


class Battery(Item):
    def __init__(self):
        super(Battery, self).__init__("Battery", 2)

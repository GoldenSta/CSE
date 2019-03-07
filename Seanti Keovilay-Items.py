class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Inventory(object):
    def __init__(self):
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

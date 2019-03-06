class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Inventory(object):
    def __init__(self):
        self.items = {}


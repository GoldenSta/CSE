class Item(object):
    def __init__(self, name, weight, description):
        self.name = name
        self.weight = weight
        self.description = description


class Inventory(Item):
    def __init__(self, name):
        super(Inventory, self).__init__(name, 0, None)
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
        if isinstance(item1, FishingPole) and isinstance(item2, Hook):
            item1.hook = item2
        if isinstance(item2, FishingPole) and isinstance(item1, Hook):
            item2.hook = item1
            print("You combine %s and %d together.")


class Flashlight(Item):
    def __init__(self):
        super(Flashlight, self).__init__("Flashlight", 5, "The flashlight is old.")
        self.batteries = None


class Battery(Item):
    def __init__(self):
        super(Battery, self).__init__("Battery", 2, "You found some batters")


class Keys(Item):
    def __init__(self):
        super(Keys, self).__init__("Keys", 1, "The keys are rusting a little.")


class Pills(Item):
    def __init__(self):
        super(Pills, self).__init__("Pills", 6, "Sometimes you get sick so you take at least 3.")


class Phone(Item):
    def __init__(self):
        super(Phone, self).__init__("Phone", 8, "You listen to music in hope it calms you down")
        self.energy = 100


class Marble(Item):
    def __init__(self):
        super(Marble, self).__init__("Marble", 1, "Its a orange marble with a slightly darker, rad star in the middle.")


class Camera(Item):
    def __init__(self):
        super(Camera, self).__init__("Camera", 7, "Taking pictures or videos with the camera is you past time.")
        self.energy = 100


class Shovel(Item):
    def __init__(self):
        super(Shovel, self).__init__("Shovel", 15, "There are two spikes on either side of the handle.")


class FishingPole(Item):
    def __init__(self):
        super(FishingPole, self).__init__("Fishing Pole", 12, "The hook is missing somewhere.")
        self.hook = None


class Hook(Item):
    def __init__(self):
        super(Hook, self).__init__("Hook", 8, "It was stuck the cupboard in the kitchen.")

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
        print("You added a item in the bag.")

    def remove_item(self, item):
        self.items.remove(item)
        print("You remove the item.")

    def combine_item(self, item1, item2):
        if isinstance(item1, Flashlight) and isinstance(item2, Battery):
            item1.batteries = item2
            print("You combine the items together.")
        if isinstance(item2, Flashlight) and isinstance(item1, Battery):
            item2.batteries = item1
            print("You combine the items together.")
        if isinstance(item1, FishingPole) and isinstance(item2, Hook):
            item1.hook = item2
            print("You combine the items together.")
        if isinstance(item2, FishingPole) and isinstance(item1, Hook):
            item2.hook = item1
            print("You combine the items together.")
        if isinstance(item1, Box) and isinstance(item2, Coin):
            item1.box = item2
            print("You combine the items together.")
        if isinstance(item2, Box) and isinstance(item1, Coin):
            item2.box = item1
            print("You combine the items together.")


class Flashlight(Item):
    def __init__(self, name):
        super(Flashlight, self).__init__(name, 5, "The flashlight is old and the top is crack slightly.")
        self.batteries = None


class Battery(Item):
    def __init__(self, name):
        super(Battery, self).__init__(name, 2, "You found some batteries.")
        self.flashlight = None


class Keys(Item):
    def __init__(self, name):
        super(Keys, self).__init__(name, 1, "The keys are rusting a little.")


class Medicine(Item):
    def __init__(self, name):
        super(Medicine, self).__init__(name, 6, "Sometimes you get sick so you take at least 3.")


class Phone(Item):
    def __init__(self, name):
        super(Phone, self).__init__(name, 8, "You listen to music in hope it calms you down")
        self.energy = 100


class Marble(Item):
    def __init__(self, name):
        super(Marble, self).__init__(name, 1, "Its a orange marble with a slightly darker, rad star in the middle.")


class Camera(Item):
    def __init__(self, name):
        super(Camera, self).__init__(name, 7, "Taking pictures or videos with the camera is you past time. "
                                              "The lens on the camera is broken. ")
        self.energy = 100


class Shovel(Item):
    def __init__(self, name):
        super(Shovel, self).__init__(name, 15, "There are two spikes on either side of the handle.")


class FishingPole(Item):
    def __init__(self, name):
        super(FishingPole, self).__init__(name, 12, "The hook is missing somewhere.")
        self.hook = None


class Hook(Item):
    def __init__(self, name):
        super(Hook, self).__init__(name, 8, "It was stuck the cupboard in the kitchen.")
        self.FishingPole = None


class Book(Item):
    def __init__(self, name):
        super(Book, self).__init__(name, 10, "The book is called 'A Wrinkle in Time'. You loved the book")


class StuffedAnimal(Item):
    def __init__(self, name):
        super(StuffedAnimal, self).__init__(name, 6, "Its a stuffed bunny. The fur seems old and dirty.")


class Sweater(Item):
    def __init__(self, name):
        super(Sweater, self).__init__(name, 9, "The sweater is still intact and it didn't seem ripped.")


class Coin(Item):
    def __init__(self, name):
        super(Coin, self).__init__(name, 4, "The coin is small. It looks like you could fit it in the box.")
        self.box = None


class Crystal(Item):
    def __init__(self, name):
        super(Crystal, self).__init__(name, 12, "Shine it in the light and it makes a rainbow")


class Box(Item):
    def __init__(self, name):
        super(Box, self).__init__(name, 13, "The box is dirty from digging it from the ground.")
        self.coin = None


class Character(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


battery = Battery("Battery")
flashlight = Flashlight("Flashlight")
coin = Coin("Coin")
box = Box("Box")
player_bag = Inventory("Bag")
player_bag.add_item(coin)
player_bag.remove_item(coin)
player_bag.add_item(battery)
player_bag.combine_item(flashlight, battery)
player_bag.combine_item(box, coin)

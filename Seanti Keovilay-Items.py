class Item(object):
    def __init__(self, name):
        self.name = name


class Flashlight(Item):
    def __init__(self, name):
        super(Item, self).__init__(name)
        self.battery = 100
        self.switch = False

    def switch_on(self):
        self.switch = True
        print("You turn the flashlight on.")

    def battery_left(self):
        self.battery -= 5
        print("You only have %s left." % self.battery)

    def switch_off(self):
        self.switch = False
        print("You turn the flashlight off.")

class Key(object):
    def __init__(self):

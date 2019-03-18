class Room(object):
    # This is a constructor
    def __init__(self, name, description, north=None, south=None, west=None, east=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east


class Dog(object):
    def __init__(self, breed="pug", dob=2/4/5, color="Pale Gray", energy=100, gender="girl", name="Lala"):
        self.breed = breed
        self.color = color
        self.energy_left = energy
        self.dob = dob
        self.gender = gender
        self.name = name


class Player(object):
    def __init__(self, starting_location):
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and finds the variable of the room.

        :param direction: A string (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]
        # getarr(R19A, "north")


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


class Pills(Item):
    def __init__(self, name):
        super(Pills, self).__init__(name, 6, "Sometimes you get sick so you take at least 3.")


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
Road = Room("Old Road", "The road that brought you here.", "Your Old House", "Your Car", None, None)
Car = Room("Your Car", "You arrived in the car with a bag inside.", "Road", None, None, None)
House = Room("Your Old House", "This is the house you grew up in your life.", "Front Door", "Road", None, None)
Backyard = Room("The Backyard", "You always play here whenever something bad happen inside the house", None,
                "Back Door", None, "Big Tree")
West_Forest = Room("West Side Forest", "You can hear the birds chirping from the north. There is a playground straight"
                                       "ahead.", "Field", None, "Playground", "West Door")
Big_Tree = Room("Big Tree", "The tree you planted back grew bigger than you thought it would.", None, None, "Backyard",
                "Crystal Lake")
Field = Room("Abandon Field", "The field had been abandoned for many years.", "Grassy Hill", "West Forest", None, None)
Playground = Room("Old Playground", "It looks like it about to fall apart.", None, None, None, "West Forest")
East_Forest = Room("East Forest", "Keep going east, you can see the barn from here. North, there is a lake.",
                   "Crystal Lake", None, "East Door", "Barn")
Crystal_Lake = Room("Crystal Lake", "You loved going fishing here with your friends or family.", None,
                    "East Forest", "Big Tree", None)
Barn = Room("Old Barn", "It's filled with hay and nothing else.", "Mini Farm", "Tool Shed", "East Forest", None)
Tool_Shed = Room("Tool Shed", "There is a fishing pole and a shovel inside.", "Barn", None, None, None)
Mini_Farm = Room("Mini Farm", "You grew different types of plants here.", None, "Barn", None, None)
Grassy_Hill = Room("Grassy Hill", "You loved to cloud gaze here or star gaze.", None, "Field", None, None)
Cave = Room("Abandoned Cave", "You never went inside there as it was too dark to see.", None, None, None, "Grassy Hill")
Front_Door = Room("Front Door", "It leads to the living room if open.", "Living Room", "Road", None, None)
Living_Room = Room("Living Room", "There is nothing inside the living room expect for the west door.", "Kitchen", None,
                   "West Door", "Hallway")
West_Door = Room("West Door", "It leads to the West Forest.", None, None, "West Forest", "Living Room")
Hallway = Room("Hallway", "There is a bedroom to the north and the bathroom in the south. There is a door leading"
                          "to the East Forest", "Bedroom", "Bathroom", None, "East Door")
Kitchen = Room("Moldy Kitchen", "The kitchen hasn't been clean for years.", "Back Door", "Living Room", None, None)
Back_Door = Room("Back Door", "It leads to the backyard.", "Backyard", "Kitchen", None, None)
Bedroom = Room("Your Bedroom", "Everything is still in the same place.", None, "Hallway", None, None)
Bathroom = Room("Broken Bathroom", "The place have been collected cobwebs.", "Hallway", None, None, None)
East_Door = Room("East Door", "The door leads to the East Forest.", None, None, "Hallway", "East Forest")

player = Player(Road)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True

# controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        print("Bye")
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")

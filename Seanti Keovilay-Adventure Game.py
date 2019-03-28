class Room(object):
    def __init__(self, name, description, north=None, south=None, west=None, east=None, item=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.item = item


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

    def pick_up_item(self, item):
        self.items.append(item)
        print("You added a item in the bag.")

    def drop_item(self, item):
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
        super(Flashlight, self).__init__(name, 5, "The flashlight is old and the top is crack slightly. "
                                                  "At least it still works, maybe.")
        self.batteries = None


class Battery(Item):
    def __init__(self, name):
        super(Battery, self).__init__(name, 2, "You found some batteries. Lucky that you found some for the flashlight "
                                               "but wondered why they were here. Meh, nothing makes sense anyway.")
        self.flashlight = None


class Keys(Item):
    def __init__(self, name):
        super(Keys, self).__init__(name, 1, "The keys are rusting from old age. You don't know how long the keys "
                                            "were here. Maybe around 3 or 4 years.")


class Medicine(Item):
    def __init__(self, name):
        super(Medicine, self).__init__(name, 6, "Sometimes you get sick so you take at least 3.")


class Phone(Item):
    def __init__(self, name):
        super(Phone, self).__init__(name, 8, "You listen to music in hope it calms you down.")
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


player_bag = Inventory("Bag")
shovel = Shovel("Shovel")
battery = Battery("Battery")
flashlight = Flashlight("Flashlight")
coin = Coin("Coin")
box = Box("Box")
keys = Keys("Keys")
fishing_pole = FishingPole("FishingPole")
phone = Phone("Phone")
stuffed_animal = StuffedAnimal("StuffedAnimal")
medicine = Medicine("Medicine")
marble = Marble("Marble")
camera = Camera("Camera")
crystal = Crystal("Crystal")
hook = Hook("Hook")
book = Book("A Wrinkle in Time")
sweater = Sweater("Sweater")

Road = Room("Old Road", "The road that brought you here. You look around the road just to see nothing but your car "
                        "and the house. ", "House", "Car", None, None)
Car = Room("Your Car", "You arrived in the car with a bag inside. You kind of wish you didn't come here but oh well, "
                       "you're here now.", "Road", None, None, None, "Bag")
House = Room("Your Old House", "This is the house you grew up in your whole life. The house seems rundown but "
                               "still holding up and well. As you walk closer, you see something shinny on the ground.",
             "Front_Door", "Road", None, None, "Coin")
Backyard = Room("The Backyard", "You always play here whenever something bad happen inside the house", None,
                "Back_Door", None, "Big_Tree", "Battery")
West_Forest = Room("West Forest", "The west forest doesn't seems too bad. You can hear the birds chirping from "
                                  "the north. There is a playground straight ahead.", "Field", None, "Playground",
                   "West_Door", "Flashlight")
Big_Tree = Room("Big Tree", "The tree you planted back grew bigger than you thought it would. You could build a tree "
                            "house up there but there are birds resting in some branches.", None, None,
                "Backyard", "Crystal_Lake", "Box")
Field = Room("Abandon Field", "The field had been abandoned for many years. The field is where you would finds "
                              "different things that were lost.", "Grassy_Hill", "West_Forest", None, None)
Playground = Room("Old Playground", "It looks like it about to fall apart. The monkey bars look ready to snap, "
                                    "the slides were griffith and the swings are lying on the ground.", None, None,
                  None, "West_Forest", "StuffedAnimal")
East_Forest = Room("East Forest", "Keep going east, you can see the barn from here. North, there is a lake.",
                   "Crystal_Lake", None, "East_Door", "Barn")
Crystal_Lake = Room("Crystal Lake", "You loved going fishing here with your friends or family. As you walked closer to "
                                    "the lake, you see something shinny in the water. You tired to reach for it but "
                                    "couldn't as the water was too deep.", None, "East_Forest", "Big_Tree",
                    None, "Crystal")
Barn = Room("Old Barn", "It's filled with hay and nothing else. The barn used to have animals running around while the "
                        "horses stay in their pen.", "Mini_Farm", "Tool_Shed", "East_Forest", None)
Tool_Shed = Room("Tool Shed", "You entered the shed to see a shovel and a fishing pole. You thought for a moment "
                              "that maybe you can use the fishing pole to get the thing out of the lake.",
                 "Barn", None, None, None, "FishingPole")
Mini_Farm = Room("Mini Farm", "You grew different types of plants here. You didn't like to buy the plants at the store "
                              "so you grew your own.", None, "Barn", None, None, "Shovel")
Grassy_Hill = Room("Grassy Hill", "You loved to cloud gaze here or star gaze.", None, "Field", "Cave", None, "Phone")
Cave = Room("Abandoned Cave", "You never went inside there as it was too dark to see.", None, None,
            None, "Grassy_Hill", "Marble")
Front_Door = Room("Front Door", "It leads to the living room if open.", "Living_Room", "Road", None, None)
Living_Room = Room("Living Room", "There is nothing inside the living room expect for the west door.", "Kitchen", None,
                   "West_Door", "Hallway", "Book")
West_Door = Room("West Door", "It leads to the West Forest.", None, None, "West_Forest", "Living_Room")
Hallway = Room("Hallway", "There is a bedroom to the north and the bathroom in the south. There is a door leading"
                          "to the East Forest", "Bedroom", "Bathroom", "Living_Room", "East_Door", "Camera")
Kitchen = Room("Moldy Kitchen", "The kitchen hasn't been clean for years.", "Back_Door", "Living_Room",
               None, None, "Hook")
Back_Door = Room("Back Door", "It leads to the backyard.", "Backyard", "Kitchen", None, None)
Bedroom = Room("Your Bedroom", "Everything is still in the same place.", None, "Hallway", None, None, "Sweater")
Bathroom = Room("Broken Bathroom", "The place have been collected cobwebs.", "Hallway", None, None, None, "Medicine")
East_Door = Room("East Door", "The door leads to the East Forest.", None, None, "Hallway", "East_Forest")

player = Player(Road)

directions = ['north', 'south', 'east', 'west']
playing = True

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    print(player.current_location.item)

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
    elif "Pick up " in command:
        item_name = command[8:]
        found_item = None
        for item in player.current_location.item:
            if item_name == item_name:
                found_item = item
        if found_item is None:
            print("I don't see a item")
        else:
            player.inventory.append(found_item)
            player.current_location.item.remove(found_item)
    else:
        print("Command not recognized.")

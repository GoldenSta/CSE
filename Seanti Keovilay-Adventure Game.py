from termcolor import colored


class Room(object):
    def __init__(self, name, description, north=None, south=None, west=None, east=None, _item=None):
        if _item is None:
            _item = []
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.item = _item


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
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Inventory(Item):
    def __init__(self, name, items=None):
        super(Inventory, self).__init__(name, None)
        if items is None:
            items = []
        self.items = items

    def pick_up_item(self, _item):
        self.items.append(_item)
        print("You added a item in the bag.")

    def drop_item(self, _item):
        self.items.remove(_item)
        print("You remove the item.")


class Flashlight(Item):
    def __init__(self, name):
        super(Flashlight, self).__init__(name, "The flashlight is old and the top is crack slightly. At least it "
                                               "still works, maybe.")


class Battery(Item):
    def __init__(self, name):
        super(Battery, self).__init__(name, "You found some batteries. Lucky that you found some for the flashlight "
                                            "but wondered why they were here. Meh, nothing makes sense anyway.")


class Medicine(Item):
    def __init__(self, name):
        super(Medicine, self).__init__(name, "Sometimes you get sick when you were a child. Sometimes the medicine "
                                             "\nwould taste funny but it made you feel better.")


class Phone(Item):
    def __init__(self, name):
        super(Phone, self).__init__(name, "You listen to music in hope it calms you down. \nYour parents really didn't "
                                          "understand your taste in music. \nThe screen is cracked and it doesn't look "
                                          "like it works anymore.")
        self.energy = 100


class Marble(Item):
    def __init__(self, name):
        super(Marble, self).__init__(name, "Its a orange marble with a red star in the middle. The marble looks like "
                                           "its made from glass.")


class Camera(Item):
    def __init__(self, name):
        super(Camera, self).__init__(name, "Taking pictures or videos with the camera is you past time. The lens on "
                                           "the \ncamera is broken. Its a shame that its broken but maybe the videos "
                                           "or pictures aren't deleted.")
        self.energy = 100


class Shovel(Item):
    def __init__(self, name):
        super(Shovel, self).__init__(name, "There are two spikes on either side of the handle. The shovel is worn out "
                                           "and beat up by the years of being used to help for the farm.")


class FishingPole(Item):
    def __init__(self, name):
        super(FishingPole, self).__init__(name, "The fishing pole seems like it could need some repair but its too old "
                                                "already. Looking closer at the fishing pole, the hook is "
                                                "missing somewhere.")


class Hook(Item):
    def __init__(self, name):
        super(Hook, self).__init__(name, "The hook used to be a silver color but now its a rusty brown color. \nIt "
                                         "seems to be also bend back a little but it still works.")


class Book(Item):
    def __init__(self, name):
        super(Book, self).__init__(name, "The book is called 'A Wrinkle in Time'. You loved the book when you were "
                                         "a kid. \nYour mom would read it to you every night and sometimes your dad "
                                         "would read for you.")


class StuffedAnimal(Item):
    def __init__(self, name):
        super(StuffedAnimal, self).__init__(name, "Its a stuffed bunny which the fur seems old and dirty. This was the "
                                                  "first and last stuffed animal you were given to by your grandpa "
                                                  "before he passed away. Since then you would bring it everywhere you "
                                                  "would go to.")


class Sweater(Item):
    def __init__(self, name):
        super(Sweater, self).__init__(name, "The sweater is still intact and it didn't seem ripped.")


class Coin(Item):
    def __init__(self, name):
        super(Coin, self).__init__(name, "The coin looks small. It has a carving of a dragon wrap around a fire. \nThe "
                                         "dragon is a silver color and the fire is a bronze color.")


class Crystal(Item):
    def __init__(self, name):
        super(Crystal, self).__init__(name, "Shine it in the light and it makes a rainbow.")


class Box(Item):
    def __init__(self, name):
        super(Box, self).__init__(name, "The box is dirty from digging it from the ground. Looking closer, the box "
                                        "has a butterfly design on top with vines of roses going around the box. The "
                                        "vines are attached to the butterfly.")


class Machete(Item):
    def __init__(self, name):
        super(Machete, self).__init__(name, "The machete seems old and rusty. It looks like its been under water for "
                                            "a very long time.")


class Notebook(Item):
    def __init__(self, name):
        super(Notebook, self).__init__(name, "Your notebook wis still filled with things you drew about or writing "
                                             "what happen today. There are lots of drawings about the ocean or on "
                                             "land. There is even a writing part of the notebook but it seems faded. "
                                             "The cover of the notebook is black with a faded white title.")


class Pen(Item):
    def __init__(self, name):
        super(Pen, self).__init__(name, "Its a white pen with a star printed on one side. The pen seems out of ink "
                                        "when you shake it.")


class Seeds(Item):
    def __init__(self, name):
        super(Seeds, self).__init__(name, "A packet of sunflower seeds were left in the dust. There are some dust "
                                          "covering the pictures of the sunflower.")


class Note(Item):
    def __init__(self, name):
        super(Note, self).__init__(name, "Welcome to the game. The directions are north(n), south(s), east(e), and "
                                         "\nwest(w). There are no ups or downs. To grab items, type 'pick up' and the "
                                         "name of the item. \nTo drop items, type 'drop' and the name of the item. "
                                         "\nDon't expected to be a fighting type game, its just walking around and "
                                         "pick or drop items. \nYou don't fight monsters, gain amour or anything else. "
                                         "If you want to exit the game, type quit(q) or exit.")


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
fishing_pole = FishingPole("FishingPole")
phone = Phone("Phone")
stuffed_animal = StuffedAnimal("StuffedAnimal")
medicine = Medicine("Medicine")
marble = Marble("Marble")
camera = Camera("Camera")
crystal = Crystal("Crystal")
hook = Hook("Hook")
book = Book("Book")
sweater = Sweater("Sweater")
machete = Machete("Machete")
notebook = Notebook("Notebook")
pen = Pen("Pen")
seeds = Seeds("Seeds")
note = Note("Note")

Somewhere = Room("Somewhere", "Just read the note and you will understand. \nThe exit is west of you. \nType 'pick up' "
                              "and the name of the item.", None, None, "Road", None, [note])
Road = Room("Old Road", "The road that brought you here. You look around the road just \nto see nothing but your car "
                        "and the house. And no its not 'Old Town Road'.", "House", "Car", None, None, [phone])
Car = Room("Car", "You arrived in the car with a bag inside. You kind of wish you didn't \ncome here but oh well, "
                  "you're here now.", "Road", None, None, None, [player_bag])
House = Room("Old House", "This is the house you grew up in your whole life. \nThe house seems rundown but "
                          "still holding up and well. \nAs you walk closer, you see something shinny on the ground.",
             "Front_Door", "Road", None, None, [coin])
Backyard = Room("The Backyard", "You always play here whenever something bad happen inside the house", None,
                "Back_Door", None, "Big_Tree", [battery])
West_Forest = Room("West Forest", "The west forest doesn't seems too bad. You can hear the birds chirping from "
                                  "the north. There is a playground straight ahead.", "Field", None, "Playground",
                   "West_Door", [flashlight])
Big_Tree = Room("Big Tree", "The tree you planted back grew bigger than you thought it would. You could build a tree "
                            "house up there but there are birds resting in some branches.", None, None,
                "Backyard", "Crystal_Lake", [box])
Field = Room("Abandon Field", "The field had been abandoned for many years. The field is where you would finds "
                              "different things that were lost.", "Grassy_Hill", "West_Forest", None, None, [notebook])
Playground = Room("Old Playground", "It looks like it about to fall apart. The monkey bars look ready to snap, "
                                    "the slides were griffith and the swings are lying on the ground.", None, None,
                  None, "West_Forest", [stuffed_animal])
East_Forest = Room("East Forest", "Keep going east, you can see the barn from here. North, there is a lake.",
                   "Crystal_Lake", None, "East_Door", "Barn", [crystal])
Crystal_Lake = Room("Crystal Lake", "You loved going fishing here with your friends or family. As you walked closer to "
                                    "the lake, you see something shinny in the water. You tired to reach for it but "
                                    "couldn't as the water was too deep.", None, "East_Forest", "Big_Tree",
                    None, [machete])
Barn = Room("Old Barn", "It's filled with hay and nothing else. The barn used to have animals running around while the "
                        "horses stay in their pen. You look around and see a shovel where it was suppose to be in "
                        "the tool shed.", "Mini_Farm", "Tool_Shed", "East_Forest", None, [shovel])
Tool_Shed = Room("Tool Shed", "You entered the shed to see a fishing pole. You thought for a moment that maybe "
                              "you can use the fishing pole to get the thing out of the lake.",
                 "Barn", None, None, None, [fishing_pole])
Mini_Farm = Room("Mini Farm", "You grew different types of plants here. You didn't like to buy the plants at the store "
                              "so you grew your own.", None, "Barn", None, None, [seeds])
Grassy_Hill = Room("Grassy Hill", "You loved to cloud gaze here or star gaze. There used to be just plain grass but "
                                  "now there are some wild flowers growing.", None, "Field", "Cave", None, [pen])
Cave = Room("Abandoned Cave", "You never went inside there as it was too dark to see. If you walk in closer, you would "
                              "see a item shaped like a bat.", None, None, None, "Grassy_Hill", [marble])
Front_Door = Room("Front Door", "It leads to the living room if open.", "Living_Room", "House", None, None)
Living_Room = Room("Living Room", "There is nothing inside the living room expect for the west door.", "Kitchen",
                   "Front_Door", "West_Door", "Hallway", [book])
West_Door = Room("West Door", "It leads to the West Forest. The door has a carving of a sakura tree. The colors has "
                              "been fading for a while.", None, None, "West_Forest", "Living_Room")
Hallway = Room("Hallway", "There is a bedroom to the north and the bathroom in the south. There is a door leading"
                          "to the East Forest", "Bedroom", "Bathroom", "Living_Room", "East_Door", [camera])
Kitchen = Room("Kitchen", "The kitchen hasn't been clean for years. There are some plants growing through the cracks "
                          "on the floor.", "Back_Door", "Living_Room",
               None, None, [hook])
Back_Door = Room("Back Door", "It leads to the backyard.", "Backyard", "Kitchen", None, None)
Bedroom = Room("Bedroom", "Everything is still in the same place. \nThere is your bed in the corner near the window. "
                          "\nThere is a desk at the other corner with old art supplies. \nThe bedroom doesn't have a "
                          "dresser but a closet instead. \nThere is something inside the closet if you look closer.",
               None, "Hallway", None, None, [sweater])
Bathroom = Room("Bathroom", "The place have been collected cobwebs. There is a cupboard with something inside.",
                "Hallway", None, None, None, [medicine])
East_Door = Room("East Door", "The door leads to the East Forest.", None, None, "Hallway", "East_Forest")

player = Player(Somewhere)

directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']
playing = True

while playing:
    print(colored(player.current_location.name, 'cyan'))
    print(colored(player.current_location.description, 'blue'))

    if len(player.current_location.item) > 0:
        print(colored("There is a item.", 'magenta'))
        for num, current_item in enumerate(player.current_location.item):
            print(colored(str(num + 1) + ": ", 'magenta') + colored(current_item.name, 'magenta'))
    command = input(colored(">_", 'green'))
    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command.lower() in ['q', 'quit', 'exit']:
        print(colored("Bye", 'red'))
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print(colored("I can't go that way.", 'red'))
    elif "pick up " in command:
        item_name = command[8:]
        found_item = None
        for item in player.current_location.item:
            if item.name.lower() == item_name.lower():
                found_item = item
                print(colored("You pick up the %s." % item_name, 'red'))
                print(colored(item.description, 'magenta'))
        if found_item is None:
            print(colored("I don't see a item", 'red'))
        else:
            player.inventory.append(found_item)
            player.current_location.item.remove(found_item)
    elif "drop " in command:
        item_name = command[5:]
        drop_item = None
        for item in player.inventory:
            if item.name.lower() == item_name.lower():
                drop_item = item
                player.inventory.remove(drop_item)
                player.current_location.item.append(drop_item)
                print(colored("You drop the %s." % item_name, 'red'))
    else:
        print(colored("Command not recognized.", 'red'))

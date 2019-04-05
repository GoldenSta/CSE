class Room(object):
    def __init__(self, name, description, north=None, south=None, west=None, east=None, _item=None):
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
        self.space = 100

    def pick_up_item(self, _item):
        self.items.append(_item)
        print("You added a item in the bag.")

    def drop_item(self, _item):
        self.items.remove(_item)
        print("You remove the item.")

    def combine_item(self, item1, item2):
        if self.items is not None:
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
        super(Flashlight, self).__init__(name, "The flashlight is old and the top is crack slightly. At least it "
                                               "still works, maybe.")
        self.batteries = None


class Battery(Item):
    def __init__(self, name):
        super(Battery, self).__init__(name, "You found some batteries. Lucky that you found some for the flashlight "
                                            "but wondered why they were here. Meh, nothing makes sense anyway.")
        self.flashlight = None


class Keys(Item):
    def __init__(self, name):
        super(Keys, self).__init__(name, "The keys are rusting from old age. You don't know how long the keys were "
                                         "here. Maybe around 3 or 4 years.")


class Medicine(Item):
    def __init__(self, name):
        super(Medicine, self).__init__(name, "Sometimes you get sick when you were a child. Sometimes the medicine "
                                             "would taste funny but made you feel better.")


class Phone(Item):
    def __init__(self, name):
        super(Phone, self).__init__(name, "You listen to music in hope it calms you down. Your parents really didn't "
                                          "understand your taste in music.")
        self.energy = 100


class Marble(Item):
    def __init__(self, name):
        super(Marble, self).__init__(name, "Its a orange marble with a rad star in the middle. The marble looks like "
                                           "its made from glass.")


class Camera(Item):
    def __init__(self, name):
        super(Camera, self).__init__(name, "Taking pictures or videos with the camera is you past time. The lens on "
                                           "the camera is broken. Its a shame that its broken but maybe the videos or "
                                           "pictures aren't deleted.")
        self.energy = 100


class Shovel(Item):
    def __init__(self, name):
        super(Shovel, self).__init__(name, "There are two spikes on either side of the handle. The shovel is worn out "
                                           "and beat up by the years of being used to dig holes.")


class FishingPole(Item):
    def __init__(self, name):
        super(FishingPole, self).__init__(name, "The fishing pole seems like it could need some repair but its too old "
                                                "already. Looking closer at the fishing pole, the hook is "
                                                "missing somewhere.")
        self.hook = None


class Hook(Item):
    def __init__(self, name):
        super(Hook, self).__init__(name, "The hook used to be a silver color but now its a rusty brown color. It seems "
                                         "to be also bend back a little but it still works.")
        self.FishingPole = None


class Book(Item):
    def __init__(self, name):
        super(Book, self).__init__(name, "The book is called 'A Wrinkle in Time'. You loved the book")


class StuffedAnimal(Item):
    def __init__(self, name):
        super(StuffedAnimal, self).__init__(name, "Its a stuffed bunny. The fur seems old and dirty.")


class Sweater(Item):
    def __init__(self, name):
        super(Sweater, self).__init__(name, "The sweater is still intact and it didn't seem ripped.")


class Coin(Item):
    def __init__(self, name):
        super(Coin, self).__init__(name, "The coin looks small. It has a carving of a dragon wrap around a fire. The "
                                         "dragon is a silver color and the fire is a bronze color.")
        self.box = None


class Crystal(Item):
    def __init__(self, name):
        super(Crystal, self).__init__(name, "Shine it in the light and it makes a rainbow")


class Box(Item):
    def __init__(self, name):
        super(Box, self).__init__(name, "The box is dirty from digging it from the ground.")
        self.coin = None


class Machete(Item):
    def __init__(self, name):
        super(Machete, self).__init__(name, "The machete seems old and rusty. It looks like its been under water for "
                                            "a very long time.")


class Stone(Item):
    def __init__(self, name):
        super(Stone, self).__init__(name, "The stone feels smooth and the color looks beautiful in the light. The "
                                          "color is a light orange with a bit of yellow around it.")


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


class Rose(Item):
    def __init__(self, name):
        super(Rose, self).__init__(name, "Its a blackish red rose sitting by the front door. It still has its petals "
                                         "intact but it shouldn't since you don't know how its not dead. Weirdly "
                                         "enough that it doesn't have any thorns on the stem.")


class SakuraFlower(Item):
    def __init__(self, name):
        super(SakuraFlower, self).__init__(name, "The flower ")


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
machete = Machete("Machete")
stone = Stone("Stone")
notebook = Notebook("Notebook")
pen = Pen("Pen")
seeds = Seeds("Seeds")
rose = Rose("Rose")
sakuraflower = SakuraFlower("SakuraFlower")

Road = Room("Old Road", "The road that brought you here. You look around the road just to see nothing but your car "
                        "and the house. ", "House", "Car", None, None, [phone])
Car = Room("Your Car", "You arrived in the car with a bag inside. You kind of wish you didn't come here but oh well, "
                       "you're here now.", "Road", None, None, None, [player_bag])
House = Room("Your Old House", "This is the house you grew up in your whole life. The house seems rundown but "
                               "still holding up and well. As you walk closer, you see something shinny on the ground.",
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
Cave = Room("Abandoned Cave", "You never went inside there as it was too dark to see.", None, None,
            None, "Grassy_Hill", [marble])
Front_Door = Room("Front Door", "It leads to the living room if open.", "Living_Room", "Road", None, None, [rose])
Living_Room = Room("Living Room", "There is nothing inside the living room expect for the west door.", "Kitchen", None,
                   "West_Door", "Hallway", [book])
West_Door = Room("West Door", "It leads to the West Forest. The door has a carving of a sakura tree. The colors has "
                              "been fading for a while.", None, None, "West_Forest", "Living_Room", [sakuraflower])
Hallway = Room("Hallway", "There is a bedroom to the north and the bathroom in the south. There is a door leading"
                          "to the East Forest", "Bedroom", "Bathroom", "Living_Room", "East_Door", [camera])
Kitchen = Room("Moldy Kitchen", "The kitchen hasn't been clean for years.", "Back_Door", "Living_Room",
               None, None, [hook])
Back_Door = Room("Back Door", "It leads to the backyard.", "Backyard", "Kitchen", None, None, [keys])
Bedroom = Room("Your Bedroom", "Everything is still in the same place.", None, "Hallway", None, None, [sweater])
Bathroom = Room("Broken Bathroom", "The place have been collected cobwebs.", "Hallway", None, None, None, [medicine])
East_Door = Room("East Door", "The door leads to the East Forest.", None, None, "Hallway", "East_Forest", {stone})

player = Player(Road)

directions = ['north', 'south', 'east', 'west']
playing = True

while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    if len(player.current_location.item) > 0:
        print("You found a item.")
        for num, current_item in enumerate(player.current_location.item):
            print(str(num + 1) + ": " + current_item.name)
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
    elif "pick up " in command:
        item_name = command[8:]
        found_item = None
        for item in player.current_location.item:
            if item_name == item_name:
                found_item = item
                print("You pick up the %s." % item_name)
                print(current_item.description)
        if found_item is None:
            print("I don't see a item")
        else:
            player.inventory.append(found_item)
            player.current_location.item.remove(found_item)
    elif "drop " in command:
        item_name = command[5:]
        drop_item = None
        for item in player.inventory:
            if item_name == item_name:
                drop_item = item
                player.inventory.remove(drop_item)
                print("You drop the %s." % item_name)
    elif "combine " in command:
        words = command.split()
        if len(words) > 2:
            item1 = words[1]
            item2 = words[2]
        combine_item = None
        print("You combine %s and %s together." % (item1, item2))

    else:
        print("Command not recognized.")

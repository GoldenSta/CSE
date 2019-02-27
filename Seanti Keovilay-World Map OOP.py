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


# There are the instances of the rooms (Instantiation)


# Option 1 - Use the variables, but fix later
R19A = Room("Mr. Wiebe's Room", None)
parking_lot = Room("The Parking Lot", None, R19A)
R19A.north = parking_lot

# Option 2 - Use Strings, but more difficult controller
R19A = Room("Mr. Wiebe's Room", "parking_lot")
parking_lot = Room("The Parking Lot", None, R19A)


# my own
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
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")

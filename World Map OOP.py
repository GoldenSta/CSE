class Room(object):
    # This is a constructor
    def __init__(self, name, description, north=None, south=None, west=None, east=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east
# There are the instances of the rooms (Instantiation)


# Option 1 - Use the variables, but fix later
R19A = Room("Mr. Wiebe's Room")
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

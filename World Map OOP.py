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

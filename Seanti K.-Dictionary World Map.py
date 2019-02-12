world_map = {
    "Road": {
        'NAME': "Old Road",
        'DESCRIPTION': "The road that brought you here.",
        'PATHS': {
            'NORTH': "Your Old House",
            'SOUTH': "Your Car"
        }
    },
    'Your Car': {
        'NAME': "Your Car",
        'DESCRIPTION': "You arrived in the car with a bag inside.",
        'PATHS': {
            'NORTH': "Road",
        }
    },
    "Your Old House": {
        'NAME': "Your Old House",
        'DESCRIPTION': "This is the house you grew up in your life.",
        'PATHS': {
            'NORTH': "Front Door",
            'SOUTH': "Road"
        }
    },
    'Backyard': {
        'NAME': "The Backyard",
        'DESCRIPTION': "You always play here whenever something bad happen inside the house",
        'PATHS': {
            'SOUTH': "Back Door",
            'EAST': "Big Tree"
        }
    },
    'West Forest': {
        'NAME': "West Side Forest",
        'DESCRIPTION': "You can hear the birds chirping from the north. There is a playground straight ahead.",
        'PATHS': {
            'NORTH': "Field",
            'WEST': "Playground",
            'EAST': "West Door"
        }
    },
    'Big Tree': {
        'NAME': "Big Tree",
        'DESCRIPTION': "The tree you planted back grew bigger than you thought it would.",
        'PATHS': {
            'EAST': "Crystal Lake",
            'WEST': "Backyard"
        }
    },
    'Field': {
        'NAME': "Abandon Field",
        'DESCRIPTION': "The field had been abandoned for many years.",
        'PATHS': {
            'SOUTH': "West Forest",
            'NORTH': "Grassy Hill"
        }
    },
    'Playground': {
        'NAME': "Old Playground",
        'DESCRIPTION': "It looks like it about to fall apart.",
        'PATHS': {
            'EAST': "West Forest"
        }
    },
    'East Forest': {
        'NAME': "East Forest",
        'DESCRIPTION': "Keep going east, you can see the barn from here. North, there is a lake.",
        'PATHS': {
            'WEST': "East Door",
            'EAST': "Barn",
            'NORTH': " Crystal Lake"
        }
    },
    'Crystal Lake': {
        'NAME': "Crystal Lake",
        'DESCRIPTION': "You loved going fishing here with your friends or family.",
        'PATHS': {
            'WEST': "Big Tree",
            'SOUTH': "East Forest"
        }
    },
    'Barn': {
        'NAME': "Old Barn",
        'DESCRIPTION': "It's filled with hay and nothing else.",
        'PATHS': {
            'WEST': "East Forest",
            'SOUTH': "Tool Shed",
            'NORTH': "Mini Farm"
        }
    },
    'Tool Shed': {
        'NAME': "Tool Shed",
        'DESCRIPTION': "There is a fishing pole and a shovel inside.",
        'PATHS': {
            'NORTH': "Barn"
        }
    },
    'Mini Farm': {
        'NAME': "Mini Farm",
        'DESCRIPTION': "You grew different types of plants here.",
        'PATHS': {
            'SOUTH': "Barn"
        }
    },
    'Grassy Hill': {
        'NAME': "Grassy Hill",
        'DESCRIPTION': "You loved to cloud gaze here or star gaze.",
        'PATHS': {
            'SOUTH': "Field"
        }
    },
    'Cave': {
        'NAME': "Abandoned Cave",
        'DESCRIPTION': "You never went inside there as it was too dark to see.",
        'PATHS': {
            'EAST': "Grassy Hill"
        }
    },
    'Front Door': {
        'NAME': "Front Door",
        'DESCRIPTION': "It leads to the living room if open.",
        'PATHS': {
            'SOUTH': "Road",
            'NORTH': "Living Room"
        }
    },
    'Living Room': {
        'NAME': "Living Room",
        'DESCRIPTION': "There is nothing inside the living room expect for the west door.",
        'PATHS': {
            'WEST': "West Door",
            'EAST': "Hallway"
        }
    },
    'West Door': {
        'NAME': "West Door",
        'DESCRIPTION': "It leads to the West Forest.",
        'PATHS': {
            'EAST': "Living Room",
            'WEST': "West Forest"
        }
    },
    'Hallway': {
        'NAME': "East Hallway",
        'DESCRIPTION': "There is a bedroom to the north and the bathroom in the south. There is a door leading to the "
                       "East Forest",
        'PATHS': {
            'NORTH': "Bedroom",
            'SOUTH': "Bathroom",
            'EAST': "East Door"
        }
    },
    'Kitchen': {
        'NAME': "Moldy Kitchen",
        'DESCRIPTION': "The kitchen hasn't been clean for years.",
        'PATHS': {
            'SOUTH': "Living Room",
            'NORTH': "Back Door"
        }
    },
    'Back Door': {
        'NAME': "Back Door",
        'DESCRIPTION': "It leads to the backyard.",
        'PATHS': {
            'NORTH': "Backyard",
            'SOUTH': "Kitchen"
        }
    },
    'Bedroom': {
        'NAME': "Your Bedroom",
        'DESCRIPTION': "Everything is still in the same place.",
        'PATHS': {
            'SOUTH': "Hallway"
        }
    },
    'Bathroom': {
        'NAME': "Broken Bathroom",
        'DESCRIPTION': "The place have been collected cobwebs.",
        'PATHS': {
            'NORTH': "Hallway"
        }
    },
    'East Door': {
        'NAME': "East Door",
        'DESCRIPTION': "The door leads to the East Forest.",
        'PATHS': {
            'EAST': "East Forest",
            'WEST': "Hallway"
        }
    }
}

# other variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["Road"]  # This is your current location
playing = True

# controller
while playing:
    print(current_node["NAME"])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")

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
            'NORTH': "Backyard",
            'WEST': "West Side Forest",
            'EAST': "East Side Forest",
            'SOUTH': "Road"
        }
    },
    'Backyard': {
        'NAME': "The Backyard",
        'DESCRIPTION': "You always play here whenever something bad happen inside the house",
        'PATHS': {
            'SOUTH': "Your Old House",
            'EAST': "Big Tree"
        }
    },
    'West Side Forest': {
        'NAME': "West Side Forest",
        'DESCRIPTION': "You can hear the birds chirping from the north. There is a playground in front of you.",
        'PATHS': {
            'NORTH': "Field",
            'WEST': "Playground",
            'EAST': "Your Old House"
        }
    },
    'Big Tree': {
        'NAME': "Big Tree",
        'DESCRIPTION': "The tree you planted back grew bigger than you thought it would.",
        'PATHS': {
            'EAST': "Lake",
            'WEST': "Backyard"
        }
    },
    'Field': {
        'NAME': "Abandon Field",
        'DESCRIPTION': "The field had been abandoned for many years.",
        'PATHS': {
            'SOUTH': "West Side Forest",
            'NORTH': "Grassy Hill"
        }
    },
    'Playground': {
        'NAME': "Old Playground",
        'DESCRIPTION': "It looks like it about to fall apart.",
        'PATHS': {
            'EAST': "West Side Forest"
        }
    },
    'East Side Forest': {
        'NAME': "East Side Forest",
        'DESCRIPTION': "Keep going east, you can see the barn from here. North, there is a lake.",
        'PATHS': {
            'WEST': "Your Old House",
            'EAST': "Barn",
            'NORTH': "Lake"
        }
    },
    'Crystal Lake': {
        'NAME': "Crystal Lake",
        'DESCRIPTION': "You loved going fishing here with your friends or family.",
        'PATHS': {
            'WEST': "Big Tree",
            'SOUTH': "East Side Forest"
        }
    },
    'Barn': {
        'NAME': "Old Barn",
        'DESCRIPTION': "It's filled with hay and nothing else.",
        'PATHS': {
            'WEST': "East Side Forest",
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

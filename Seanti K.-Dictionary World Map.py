world_map = {
    "Road": {
        'NAME': "Old Road",
        'DESCRIPTION': "The road brought you here.",
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
        'NAME': "Your Old Backyard",
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
        'DESCRIPTION': "The tree you planted back then grew really big.",
        'PATHS': {
            
        }
    }
}

# other variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["Road"]  # This is your current location
playing = True

# controller
while playing:
    print("Do you remember the place?")
    print(current_node["NAME"])
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

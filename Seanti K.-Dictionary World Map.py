world_map = {
    "Rl9A": {
        'NAME': "Old Road",
        'DESCRIPTION': "This is where it all began.",
        'PATHS': {
            'NORTH': "Your Old House"
        }
    },
    'Car': {
        'NAME': "Your Car",
        'DESCRIPTION': "You arrived in the car with a bag inside.",
        'PATHS': {
            'SOUTH': "R19A"
        }
    }
}

# other variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["Rl9A"]  # This is your current location
playing = True

# controller
while playing:
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

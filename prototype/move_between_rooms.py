"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# Set the player's starting room.
current_room = "Great Hall"

# Create the gameplay loop.
while current_room != "exit":

    # Display the player's current room.
    print("You are currently in the", current_room)

    # Ask the player for a movement command or exit.
    command = input("Enter a direction (north, south, east, west) or exit: ")

    # If the player chooses exit, end the game.
    if command == "exit":
        current_room = "exit"

    # If the player enters a valid direction, move to the new room.
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]

    # If the command is not valid, display an error message.
    else:
        print("Invalid command. Please try again.")

# TODO: Run and debug all milestone cases in prototype/README.md.

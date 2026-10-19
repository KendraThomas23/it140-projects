"""Project Two starter for the student's text-based adventure game."""

# TODO: Kendra Thomas


def show_instructions():
    """Display the game objective and available commands."""
    print("Welcome to the Haunted Mansion!")
    print("Collect all six items before entering the Attic.")
    print("Move commands: north, south, east, west")
    print("To collect an item, type: get item name")
    print("Type quit to exit the game.")
    pass


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("\nYou are in the", current_room)
    print("Inventory:", inventory)
    pass

    if rooms[current_room]["item"] is not None:
        print("You see a", rooms[current_room]["item"])

def main():
    """Run the main gameplay loop."""
    rooms = {
        "Entrance Hall": {
            "north": "Kitchen",
            "east": "Dining Room",
            "item": None

        },
        "Kitchen": {
            "south": "Entrance Hall",
            "east": "Study",
            "item": "Flashlight"
        },
        "Dining Room": {
            "west": "Entrance Hall",
            "south": "Basement",
            "item": "Silver Coin"
        },
        "Basement": {
            "north": "Dining Room",
            "east": "Library",
            "item": "Rope"
        },
        "Study": {
            "west": "Kitchen",
            "east": "Bedroom",
            "item": "Ancient Book"
        },
        "Library": {
            "west": "Basement",
            "north": "Bedroom",
            "item": "Old Key"
        },
        "Bedroom": {
            "west": "Study",
            "south": "Library",
            "north": "Attic",
            "item": "Skeleton Key"
        },
        "Attic": {
            "south": "Bedroom",
            "item": None

    # TODO:   
            current_room = "Entrance Hall"
    inventory = []

    # TODO: 
    show_instructions()

    playing = True

    # TODO: Create the gameplay loop.
    while playing:
        show_status(current_room, inventory, rooms)

        if current_room == "Attic":
            if len(inventory) == 6:
                print("You collected all six items!")
                print("You defeated the Shadow! You win!")
            else:
                print("The Shadow caught you! You lose!")
            break

        command = input("Enter your move: ").lower().strip()

        if command == "quit":
            print("Thanks for playing!")
            playing = False

        elif command.startswith("get "):
            item_name = command[4:].strip().lower()
            room_item = rooms[current_room]["item"]

            if room_item is not None and item_name == room_item.lower():
                inventory.append(room_item)
                rooms[current_room]["item"] = None
                print("You collected the", room_item)
            else:
                print("That item is not available here.")

        elif command in rooms[current_room]:
            current_room = rooms[current_room][command]

        else:
            print("Invalid command. Try again.")
    pass


if __name__ == "__main__":
    main()

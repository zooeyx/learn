"""Text Adventure — an interactive text-based game.

Commands: go <direction>, look, take <item>, inventory, use <item>, quit
"""


class Room:
    """A room in the adventure."""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # direction -> Room
        self.items = []  # list of item names

    def __str__(self):
        return f"\n--- {self.name} ---\n{self.description}"

    # TODO: Add connect(direction, room) method
    # TODO: Add get_exits() method returning available directions


class Player:
    """The player character."""

    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    # TODO: Add move(direction) method
    # TODO: Add take(item_name) method
    # TODO: Add show_inventory() method


def build_world():
    """Create rooms and connections, return starting room."""
    # TODO: Create rooms
    # Hint: entrance = Room("Entrance", "A dark cave entrance...")
    # Hint: hallway = Room("Hallway", "A long stone hallway...")

    # TODO: Connect rooms
    # Hint: entrance.connect("north", hallway)
    # Hint: hallway.connect("south", entrance)

    # TODO: Place items
    # Hint: entrance.items.append("torch")

    # TODO: Return the starting room
    pass


def main():
    start = build_world()
    if start is None:
        print("TODO: Implement build_world() first!")
        return

    player = Player(start)

    print("=== Text Adventure ===")
    print("Type 'help' for commands.\n")
    print(player.current_room)

    # TODO: Game loop
    # Hint: while True:
    #           command = input("> ").strip().lower()
    #           if command == "quit": break
    #           elif command == "look": print(player.current_room)
    #           elif command.startswith("go "): player.move(command[3:])
    #           ...

    print("TODO: Implement the game loop!")


if __name__ == "__main__":
    main()

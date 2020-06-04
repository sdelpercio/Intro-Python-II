from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# create items
rusty_sword = Item(
    "Rusty sword", "rough to the touch, a relic from past eras.")
mirror = Item("Mirror", "your face reflects as you stare into it.")
silver_dagger = Item(
    "Silver dagger", "useful against those without a reflection...")
rubber_chicken = Item("Rubber chicken", "SQAWWW")
gold_coin = Item("Gold coin", "from a previous time. Should be worth a lot!")

# Add items to rooms
room['outside'].items.append(rusty_sword)
room['foyer'].items.append(rubber_chicken)
room['foyer'].items.append(mirror)
room['overlook'].items.append(silver_dagger)
room['treasure'].items.append(gold_coin)


#
# Main
#

# Make a new player object that is currently in the 'outside' room, declare vars
new_player = Player(room['outside'])


# Initialize Game
print("> Welcome to the Room Game. It's totally fun...")
print("> You are a poor thief searching for gold, find the treasure to win the game!")
print('')
print(
    "> Controls: [n] move north [e] move east [s] move south [w] move west [q] quit game")
print("> Tip! Try to *look* for items, *pickup* items, or *use* items!")
print('')

# create loop
while True:
    # opening statement
    print('')
    print(new_player.current_room)
    print('')
    action = input("What do you want to do?")

    # quit game
    if action == 'q':
        print('> Thanks for playing.')
        break

    # movement actions
    elif action in ['n', 'e', 's', 'w']:
        new_player.move(action)
        continue

    elif len(action) == 2:
        if action[0] in ['pickup', 'take', 'grab']:
            new_player.pickup(action[1])
            continue
        elif action[0] in ['look', 'search', 'find']:
            new_player.look_for_items()
            continue
        elif action[0] in ['use']:
            new_player.use_item(action[1])
            continue
        else:
            print("> Doesn't look like you can do that...")

    else:
        print('> Action not recognized. Try again.')


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

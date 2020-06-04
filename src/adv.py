# import files
from room import Room
from player import Player
from item import Item
#import modules
import time

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

sword = Item("sword", "rusty and rough to the touch, a relic from past eras.")
mirror = Item("mirror", "your face reflects as you stare into it.")
dagger = Item("dagger", "useful against those without a reflection...")
chicken = Item("chicken", "SQAWWW")
coin = Item("coin", "from a previous time. Should be worth a lot!")


# Add items to rooms
room['outside'].items.append(sword)
room['foyer'].items.append(chicken)
room['foyer'].items.append(mirror)
room['overlook'].items.append(dagger)
room['treasure'].items.append(coin)


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

    # check for boss battle
    if new_player.current_room.name == "Treasure Chamber":
        print("> Suddenly a Vampire descends from the ceiling!!")
        print("> You have 15 seconds to decide before certain DOOM!")
        now = time.time()
        future = now + 15

    action = input("What do you want to do?  ").split()

    # time check for boss battle
    if new_player.current_room.name == "Treasure Chamber":
        if time.time() > future:
            print("> The Vampire sucks your bLoOoOoD")
            print("> You Died.")
            break

    # quit game
    if action[0] == 'q':
        print('> Thanks for playing.')
        break

    # movement actions
    elif action[0] in ['n', 'e', 's', 'w']:
        print('')
        new_player.move(action[0])
        continue

    elif action[0] in ['look', 'search', 'find']:
        print('')
        new_player.look_for_items()
        continue

    elif len(action) > 1:
        if action[0] in ['pickup', 'take', 'grab']:
            print('')
            result = new_player.pickup(action[1])
            if result == False:
                print(f"> Couldn't pickup {action[1]}")
            continue
        elif action[0] in ['use']:
            print('')
            result = new_player.use_item(action[1])
            if result == True:
                print("You won! Congratulations!")
                break
            continue
        else:
            print('')
            print("> Doesn't look like you can do that...")

    else:
        print('')
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

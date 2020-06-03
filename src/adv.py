from room import Room
from player import Player
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room, declare vars
new_player = Player(room['outside'])
blocked = "Doesn't appear you can move that way..."

# Initialize Game
print("Welcome to the Room Game. It's totally fun...")
print("You are a poor thief searching for gold, find the treasure to win the game!")
print('')
print(
    "Controls: [n] move up [e] move right [s] move down [w] move left [q] quit game")
print('')

while True:
    print('')
    print(new_player.room)

    action = input("What do you want to do?")

    if action == 'q':
        print('Thanks for playing.')
        break

    if action == 'n':
        if new_player.room.n_to:
            new_player.room = new_player.room.n_to
            continue
        else:
            print(blocked)
            continue
    if action == 'e':
        if new_player.room.e_to:
            new_player.room = new_player.room.e_to
            continue
        else:
            print(blocked)
            continue
    if action == 's':
        if new_player.room.s_to:
            new_player.room = new_player.room.s_to
            continue
        else:
            print(blocked)
            continue
    if action == 'w':
        if new_player.room.w_to:
            new_player.room = new_player.room.w_to
            continue
        else:
            print(blocked)
            continue


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

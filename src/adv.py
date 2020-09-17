import sys

from room import Room
from player import Player
from item import Item
from item import LightSource

# Declare all the items
item = {
    'coin':  Item("coin",
                     "All the money in the world"),

    'sword':    Item("sword", "This is a samurai sword"),

    'stone':  Item("stone",
                     "very polished stone"),

    'bread':    Item("bread", "Delicious with all the energy to fight"),
    'water':    Item("water", "Quench your thirst"),
    'gold':     Item("gold", "Tons of gold"),
    'torch':    LightSource("torch", "needed for dark rooms")
}

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

    'attic': Room("Dark Room", """You need a light source in this room.""")
}

room['attic'].is_light = False

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['outside'].s_to = room['attic']
room['attic'].n_to = room['outside']

room['outside'].items.append(item['coin'])
room['outside'].items.append(item['torch'])
room['foyer'].items.append(item['sword'])
room['overlook'].items.append(item['stone'])
room['narrow'].items.append(item['bread'])
room['treasure'].items.append(item['water'])
room['attic'].items.append(item['gold'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Mukesh", room['outside'])

def isLightSource(items):
    for item in items:
        if isinstance(item, LightSource):
            return True

def printRoomItems(room):
    if room.is_light or isLightSource(room.items) or isLightSource(player1.items):
        print(f'You are in room: {room.name}')
        print(f'Room description: {room.desc}')
        print(f'Room items:')
        for item in room.items:
            print(f'{item.name}')
    else:
        print("It\'s pitch black! You need a light source to see items in this room.")

def printLocation(room):
    print('------------------------------------')
    printRoomItems(room)
    print(f'Player items:')
    for item in player1.items:
        print(f'{item.name}')
    print('------------------------------------')

def handleOneLetterInput(user):
    if user == 'n':
        if player1.current_room.n_to != "":
            player1.current_room = player1.current_room.n_to
        else:
            print("This move is not allowed.")
    elif user == 's':
        if player1.current_room.s_to != "":
            player1.current_room = player1.current_room.s_to
        else:
            print("This move is not allowed.")
    elif user == 'e':
        if player1.current_room.e_to != "":
            player1.current_room = player1.current_room.e_to
        else:
            print("This move is not allowed.")
    elif user == 'w':
        if player1.current_room.s_to != "":
            player1.current_room = player1.current_room.w_to
        else:
            print("THIS MOVE IS NOT ALLOWED!!!!!!.")
    elif user == 'i' or 'inventory':
        print(f'Player items:')
        for item in player1.items:
            print(f'{item.name}')
    else:
        print("Invalid selection. Please try again.")

def handleTwoWordsInput(user):
    if user.split()[0]=="take" or user.split()[0]=="get" :
        if (item[user.split()[1]] in player1.current_room.items):
            player1.items.append(item[user.split()[1]])
            player1.current_room.items.remove(item[user.split()[1]])
            item[user.split()[1]].on_take()
        else:
            print("Sorry, this item doesn't exist.")
    elif user.split()[0]=="drop":
        if (item[user.split()[1]] in player1.items):
            player1.current_room.items.append(item[user.split()[1]])
            player1.items.remove(item[user.split()[1]])
            item[user.split()[1]].on_drop()
        else:
            print("Sorry, this item doesn't exist.")      
    else:
        print("Invalid selection. Please try again.")

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
printLocation(player1.current_room)

user = str(input("[n,s,e,w] Enter a cardinal direction to play    [q] Quit\n"))

#gamplay loop
while not user == 'q':
    if len(user.split())==1:
        handleOneLetterInput(user)
    elif len(user.split())==2:
        handleTwoWordsInput(user)
    else:
        print("Invalid selection. Please try again.")
    printLocation(player1.current_room)
    print("Please choose to continue...")
    user = str(input("[n,s,e,w] Enter a cardinal direction to play    [q] Quit\n"))
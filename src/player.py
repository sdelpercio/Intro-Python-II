# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room, items=None):
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        try:
            room_desired = getattr(self.current_room, f'{direction}_to')
            self.current_room = room_desired
        except AttributeError:
            print("> Doesn't appear you can move that way...")

    def look_for_items(self):
        if len(self.current_room.items) >= 1:
            for i in self.current_room.items:
                print(f"> You see a {i}")
        else:
            print("> There aren't any items in here")

    def pickup(self, item):
        if len(self.current_room.items) >= 1:
            for i in self.current_room.items:
                print('> Searching...')
                if item == i.name:
                    self.items.append(i)
                    self.current_room.items.remove(i)
                    print(f"> You picked up a {i.name}!")
                    return True
            return False
        else:
            return False

    def use_item(self, item):
        item_names = [i.name for i in self.items]
        if item in item_names:
            if item == 'dagger' and self.current_room.name == "Treasure Chamber":
                print(f"> You slash the Vampire with the silver dagger!")
                print('> The Vampire recoils, and turns to dust!')
                print('...')
                return True
            else:
                print("> Doesn't seem to have any use...")
        else:
            print("> You don't have that item.")

    def __str__(self):
        return self.current_room

    def __repr__(self):
        return f"(current_room={self.current_room})"

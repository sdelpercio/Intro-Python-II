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
            for item in self.current_room.items:
                print(f"> You see a {item.name}")
        else:
            print("> There isn't any items in here")

    def pickup(self, item):
        pass

    def use_item(self, item):
        pass

    def __str__(self):
        return self.current_room

    def __repr__(self):
        return f"(current_room={self.current_room})"

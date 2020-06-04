# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return textwrap.fill(f"> You're in the {self.name}.\n{self.description}", width=60)

    def __repr__(self):
        return textwrap.fill(f'(name={self.name}, description={self.description})', width=60)

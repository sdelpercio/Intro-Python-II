import textwrap


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return textwrap.fill(f"{self.name}, {self.description}", width=60)

    # def __repr__(self):
    #     return textwrap.fill(f"{self.name}, {self.description}", width=60)

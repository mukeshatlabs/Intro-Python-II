# Write a class to hold player information, e.g. what room they are in
# currently.

class Item:
    def __init__(self, name="", desc=""):
        self.name = name
        self.desc = desc
    def on_take(self):
        print(f'You have picked up {self.name}')
    def on_drop(self):
        print(f'You have dropped up {self.name}')
    def __str__(self):
        return(f'Name: {self.name}, Description: {self.desc}')

class LightSource(Item):
    def __init__(self, name="", desc=""):
        super().__init__(name,desc)
    def on_take(self):
        print(f'You have picked up {self.name}')
    def on_drop(self):
        print(f'It\'s not wise to drop your source of light! You dropped: {self.name}')
    def __str__(self):
        return(f'Name: {self.name}, Description: {self.desc}')


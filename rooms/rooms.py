class Room:

    def __init__(self, description, items, monsters, paths):
        self.description = description
        self.items = items
        self.monsters = monsters
        self.paths = paths

    def interact(self):
        #player interactions here, return number of room player travels to
        pass

list_of_rooms=[
    Room("An easy room with no monsters",["Potion"],[],[1]),
    Room("A hard room with some lemons",["Lemon","Lemon"],["Monster"],[0])]

current_room=0
game_over=False
while not game_over:
    current_room=list_of_rooms[current_room].interact()
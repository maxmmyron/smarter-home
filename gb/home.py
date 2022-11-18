class Home():
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)


class Room(Home):
    def __init__(self, name):
        self.name = name
        self.temperature = 21
        self.lights = 0


home = Home()

home.add_room(Room("living_room"))
home.add_room(Room("kitchen"))

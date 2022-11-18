# home.py
# handles home state class and general home state logic

class Home:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    # adds a new room to the home. if the room already exists, an exception is raised
    def add_room(self, name, light=False, temperature=21):
        # check if room already exists
        for room in self.rooms:
            if room.name == name:
                raise Exception("Room already exists")

        # add room to home
        new_room = Room(name, light, temperature)
        self.rooms.append(new_room)

    # updates the home state to match closer to the target state
    # throws an exception if the target state does not match the structure of the home state
    def update(self, target):
        # ensure home state and target state have same structure
        if self.name != target.name:
            raise Exception("Home state name does not match target state name")
        if len(self.rooms) != len(target.rooms):
            raise Exception(
                "Home state room count does not match target state room count")

        for i in range(len(self.rooms)):
            if self.rooms[i].name != target.rooms[i].name:
                raise Exception(
                    "Room state name does match target state name at index " + str(i))

        has_updated = False

        # iterate through rooms and attempt to change state
        for i in range(len(self.rooms)):
            state_room = self.rooms[i]
            target_room = target.rooms[i]

            # has_updated will turn (and remain) True if any room has updated
            has_updated = has_updated or state_room.update(target_room)

        return has_updated


class Room:
    # creates a new room with a name, light boolean, and temperature
    def __init__(self, name, light, temperature):
        self.name = name

        self.light = light
        self.temperature = temperature

    # updates the room state to match closer to the target room state
    def update(self, target):
        if (self.light == target.light and self.temperature == target.temperature):
            return False

        # change state of room

        self.__setattr__("light", target.light)

        tempChange = 1 if target.temperature > self.temperature else -1
        self.__setattr__("temperature", self.temperature + tempChange)

        return True

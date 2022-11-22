# home.py
# handles home state class and general home state update logic

class Home:
    def __init__(self, name):
        self.name = name
        self.rooms = []

        # usage is a list of [light, temp_up, temp_down] usage.
        # usage[0] tracks whether light is on (constant energy usage)
        # usage[1] tracks whether temperature has increased between updates
        # usage[2] tracks whether temperature has decreased between updates
        # usage[1] and usage[2] are mutually exclusive with one another
        self.usage = [0, 0, 0]

    # adds a new room to the home. if the room already exists, an exception is raised
    def add_room(self, name, light=False, temperature=21):
        # check if room already exists
        for room in self.rooms:
            if room.name == name:
                raise Exception("Room already exists")

        self.rooms.append(Room(name, light, temperature))

    def set_room(self, name, light, temperature):
        for room in self.rooms:
            if room.name == name:
                room.light = light if light is not None else room.light
                room.temperature = temperature if temperature is not None else room.temperature

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
            if state_room.update(target_room):
                has_updated = True

        # update last usage
        self.__update_usage()

        return has_updated

    # updates the usage statistics of the home
    def __update_usage(self):
        self.usage = [0, 0, 0]

        for room in self.rooms:
            room_usage = room.usage
            self.usage[0] += room_usage[0]
            self.usage[1] += room_usage[1]
            self.usage[2] += room_usage[2]


class Room:
    # creates a new room with a name, light boolean, and temperature
    def __init__(self, name, light, temperature):
        self.name = name

        self.light = light
        self.temperature = temperature
        self.usage = [0, 0, 0]

        # private variable to track temperature difference
        self.__temp_diff = 0

    # updates the room state to match closer to the target room state
    def update(self, target):
        has_updated = False

        if (self.light != target.light or self.temperature != target.temperature):
            has_updated = True

        self.light = target.light

        # clamp __temp_diff to range [-1 1]
        self.__temp_diff = min(
            max(target.temperature - self.temperature, -1), 1)
        self.temperature += self.__temp_diff

        self.__update_usage()

        return has_updated

    # private: updates the usage statistics of the room
    def __update_usage(self):
        self.usage[0] = int(self.light)
        self.usage[1] = 1 if self.__temp_diff > 0 else 0
        self.usage[2] = 1 if self.__temp_diff < 0 else 0

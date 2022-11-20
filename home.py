# home.py
# handles home state class and general home state logic

class Home:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.last_usage = [0, 0, 0]

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
        # reset last usage to 0s
        self.last_usage = [0, 0, 0]

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

            # add room usage to home usage
            self.last_usage[0] += state_room.last_usage[0]
            self.last_usage[1] += state_room.last_usage[1]
            self.last_usage[2] += state_room.last_usage[2]

        return has_updated

    def get_last_usage(self):
        return self.last_usage


class Room:
    # creates a new room with a name, light boolean, and temperature
    def __init__(self, name, light, temperature):
        self.name = name

        self.light = light
        self.temperature = temperature
        self.last_usage = [0, 0, 0]

    # updates the room state to match closer to the target room state
    def update(self, target):
        if (self.light == target.light and self.temperature == target.temperature):
            return False

        # change state of room
        self.light = target.light
        temp_diff = 1 if target.temperature > self.temperature else -1
        self.temperature += temp_diff

        # update last usage
        self.last_usage[0] = int(self.light)
        self.last_usage[1] = int(temp_diff > 0)
        self.last_usage[2] = int(temp_diff < 0)

        return True

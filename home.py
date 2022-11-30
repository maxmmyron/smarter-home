# home.py
# handles home state class and general home state update logic

class Home:
    def __init__(self, name):
        '''
        creates a new Home object with the specified name.

        name: the name of the home
        '''

        self.name = name
        '''the name of the home'''

        self.rooms = []
        '''a list of rooms in the home. each room is a Room object'''

        self.usage = [0, 0, 0]
        '''
        a list of usage statistics for the home.

        - usage[0] tracks whether light or not the is on (constant energy usage)
        - usage[1] tracks whether temperature has increased between updates
        - usage[2] tracks whether temperature has decreased between updates
        '''

        self.temp_step = 0.1
        self.light_step = 0.1

    def equals(self, home):
        for i in range(len(self.rooms)):
            if self.rooms[i] != home.rooms[i]:
                return False
        return True

    def add_room(self, name, light=False, temperature=21, x=0, y=0):
        '''
        adds a new room to the home.

        name: the name of the room
        light: whether or the light is on or not. defaults to False
        temperature: the temperature of the room. defaults to 21

        raises an exception if a room with the specified name already exists
        '''

        # check if room already exists
        for room in self.rooms:
            if room.name == name:
                raise Exception("Room already exists")

        self.rooms.append(Room(name, light, temperature, x, y))

    def set_room(self, name, light, temperature, x=None, y=None):
        '''
        instantly sets the state of the specified room to the provided state values

        name: the name of the room to set state

        light: whether the light is on or not
        temperature: the temperature of the room

        returns True if the room was found

        raises an exception if the room does not exist
        '''

        for room in self.rooms:
            if room.name == name:
                room.light = light if light is not None else room.light
                room.temperature = temperature if temperature is not None else room.temperature

                room.x = x if x is not None else room.x
                room.y = y if y is not None else room.y

                return True

        raise Exception("Room does not exist")

    def update(self, target):
        '''
        updates the home state to match closer to the target state

        target: the target state to update to. must match home state in number of rooms and room names.

        returns:
        - True if the home state was updated closer to the target state
        - False if the home state was not updated closer to the target state

        raises an exception if the target state does not match the structure of the original state
        '''

        # ensure home state and target state have same structure
        if len(self.rooms) != len(target.rooms):
            raise Exception(
                "Home state room count does not match target state room count")

        for i in range(len(self.rooms)):
            if self.rooms[i].name != target.rooms[i].name:
                raise Exception(
                    "Room state name does match target state name at index " + str(i))

        # track whether any room was updated or not
        has_updated = False

        # iterate through rooms and attempt to change state
        for i in range(len(self.rooms)):
            state_room = self.rooms[i]
            target_room = target.rooms[i]

            # has_updated will turn (and remain) True if any room has updated
            if state_room.update(target_room):
                has_updated = True

        # update last usage
        self._update_usage()

        return has_updated

    def _update_usage(self):
        '''
        private

        updates the overall usage statistics of the home.
        takes usage statistics from each room and aggregates them into a single usage struct.
        '''

        self.usage = [0, 0, 0]

        for room in self.rooms:
            room_usage = room.usage
            self.usage[0] += room_usage[0]
            self.usage[1] += room_usage[1]
            self.usage[2] += room_usage[2]


class Room:
    def __init__(self, name, light, temperature, x, y, temp_step=0.1, light_step=0.1):
        '''
        creates a new Room object with the specified name, light boolean, and temperature

        name: the name of the room
        light: whether the light is on or not
        temperature: the temperature of the room
        '''
        self.name = name

        # TODO: allow for light to be a float value (0-1) to represent dimming
        self.light = light
        # TODO: specify a "temperature step" size so it doesn't increase by integer steps
        self.temperature = temperature
        self.usage = [0, 0, 0]

        self.x = x
        self.y = y

        self.temp_step = temp_step
        self.light_step = light_step

        self._temp_diff = 0
        '''
        private

        tracks the last difference between the target temperature and the current temperature.
        used to calculate usage statistics.
        '''

    def __eq__(self, room):
        if self.light == room.light and self.temperature == room.temperature:
            return True
        else:
            return False

    # updates the room state to match closer to the target room state
    def update(self, target):
        '''
        updates the room state to match closer to the target state

        target: the target state to update to. must match room state in name.
        '''

        has_updated = False

        if (self.light != target.light or self.temperature != target.temperature):
            has_updated = True

        # set light to target (since it's just a boolean value)
        self.light = target.light

        # clamp temp_diff to tempstemp range to prevent overshoot
        self._temp_diff = min(
            max(target.temperature - self.temperature, -self.temp_step), self.temp_step)
        self.temperature += self._temp_diff

        self._update_usage()

        return has_updated

    def _update_usage(self):
        '''
        private

        updates the usage statistics of the room.
        '''

        self.usage[0] = int(self.light)
        self.usage[1] = 1 if self._temp_diff > 0 else 0
        self.usage[2] = 1 if self._temp_diff < 0 else 0

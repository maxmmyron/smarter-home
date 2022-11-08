class homeObject:
    '''Class for creating objects that represent devices in the home.
       Each object has a variable to track its state and an id. '''

    def __init__(self, id):
        self._state = 0
        self._id = id
        self._tempDelta = 5
        self._energyUse = 100

    def changeState(self):
        if self._state == 0:
            self._state = 1
        else:
            self._state = 0

    def returnState(self):
        return self._state


class light(homeObject):
    '''Class for creating objects that represent lights in the home
       Each light has a variable to track its state (on or off) and
       an id.'''
    pass


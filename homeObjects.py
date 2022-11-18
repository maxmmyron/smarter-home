class homeObject:
    '''Class for creating objects that represent devices in the home.
       Each object has a variable to track its state and an id. '''

    def __init__(self, id):
        self._state = 0
        self._id = id
        self._energyUse = 100

    def changeState(self):
        if self._state == 0:
            self._state = 1
        else:
            self._state = 0
        return self._state

    def returnState(self):
        return self._state


class light(homeObject):
    '''Class for creating objects that represent lights in the home
       Each light has a variable to track its state (on or off) and
       an id.'''
    pass

class thermometer(homeObject):
    '''Class for creating objects that represent thermometers in 
       the home.
       Each thermometer has a variable to track its current temperature
       and an id.'''

    def __init__(self, id):
        super().__init__(id)
        self._temp = 0

    def returnTemp(self):
        return self._temp

    def setTemp(self, temp):
        self._temp = temp
from light import homeObject

class thermometer(homeObject):
    '''Class for creating objects that represent thermometers in 
       the home.
       Each thermometer has a variable to track its current temperature
       and an id.'''

    def __init__(self, id):
        super().__init__(id)
        self._temp = 0

    def returnCurrentTemp(self):
        return self._temp

class heater(homeObject):
    '''Class for creating objects that represent heaters in 
       the home.
       Each thermometer has a variable to track its state (on or off)
       and an id.'''
    pass

class airConditioner(homeObject):
    '''Class for creating objects that represent air conditioners in 
       the home.
       Each thermometer has a variable to track its state (on or off)
       and an id.'''
    pass
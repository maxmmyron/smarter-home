class homeObject:
    '''Class for creating objects that represent devices in the home.
       Each object has a variable to track its state and an id. '''

    def __init__(self, id):
        self._state = 0
        self._id = id
        self._energyUse = 0
        self._tempDelta = 5
        self._energyUse = 100
        self._database = {}

    def changeState(self):
        if self._state == 0:
            self._state = 1
        else:
            self._state = 0

    def returnState(self):
        return self._state

    # to save the data in case of losing data when switching to another system
    def returnLastData(self,database,today):
        x = database[today]
        return x

    def storeInDatabase(self,today,tomorrow,database,energyUsage):
        # detect if there is a new day, then update the dict(database)
        if today != tomorrow:  
            today = tomorrow
            database[today] = 0
        else:
            if self.returnLastData(database,today) == 0:
                database[today] = energyUsage
            else:
                database[today] = energyUsage + self.returnLastData(database,today)


class light(homeObject):
    def __init__(self,id,state):
        homeObject.__init__(self,id)
        self._state = state
    def changeState(self,state):
        self._state = state
    def returnState(self):
        return self._state
    

class heater(homeObject):
    def __init__(self,id,state,temp):
        homeObject.__init__(self,id)
        self._temp = temp
        self._state = state
    def changeState(self,state):
        self._state = state
        
    def returnState(self):
        return super().returnState()
    
    def setTemp(self,temp):
        self._temp = temp
    
    def getTemp(self):
        return self._temp
        
        
class airConditioner(homeObject):
    def __init__(self,id,state,temp):
        homeObject.__init__(self,id)
        self._temp = temp
        self._state = state
    def changeState(self,state):
        self._state = state
        
    def returnState(self):
        return super().returnState()
    
    def setTemp(self,temp):
        self._temp = temp
    
    def getTemp(self):
        return self._temp

def Exit():
    print("------------------------------------------------------------------------")
    print("                             Main Page")
    print("------------------------------------------------------------------------")
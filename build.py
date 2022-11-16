from homeObject import *
from sys import *
x1 = light(1,0)
x2 = heater(2,0,25)
x3 = airConditioner(3,0,25)

import time
import datetime
today = datetime.datetime.now().strftime('%Y-%m-%d')
lightDatabase = {today:0}
heaterDatabase = {today:0}
airConditionerDatabase = {today:0}
coreDatabase = {today:0}

def returnDatabase(database):
    return database   

def totalUsage(lightDatabase,heaterDatabase,airConditionerDatabase):
    x = lightDatabase[today]
    y = heaterDatabase[today]
    z = airConditionerDatabase[today]
    total = x + y + z
    coreDatabase[today] = total
    return coreDatabase

#light System
def lightSys():
    global today
    global start1
    global end1
    tomorrow = datetime.datetime.now().strftime('%Y-%m-%d')
    lightData = 0 #watts
    lightUsage = 0
    
    while True:
        print("-------------------------------------")
        print(" Welcome to the light control System")
        print("-------------------------------------")
        print("1. returnState; 2. changeState;  Exit(press q)")
        options = input("Select Function:")
        # return state
        if options == "1":
            print("Current State:" , x1.returnState())
        # set state
        elif options == "2":
            while True:
                set = input("Set you state (0/1)： (press 'q' to Exit)")
                if set == "0" and x1.returnState() == 0:
                    print("Light is already off, you mean turn it on?")
                    print("press 'q' to Exit")
                elif set=="1" and x1.returnState() == 1:
                    print("Light is already on, you mean turn it off?")
                    print("press 'q' to Exit")
                else:
                    if set == "0":
                        end1 = time.time()
                        x1.changeState(0)
                        print("Light is Off.")
                        lightData = round(25 / 60 * (end1 - start1),2)
                        lightUsage += lightData
                        print("This period using",lightData,"watts.") 
                        x1.storeInDatabase(today,tomorrow,lightDatabase,lightUsage) 
                        lightUsage = 0 
                        end1 = 0 # reset
                        break
                    elif set=="1":
                        start1 = time.time()
                        x1.changeState(1)
                        print("Light is on.")
                        break
                    elif set == "q":
                        break
                    else:
                        print("Wrong number, please try again.")
                        False 
                               
        #exit the system
        elif options == "q":
            Exit()
            break
    


# Heater System        
def heaterSys():      
    global today
    global start2
    global end2
    tomorrow = datetime.datetime.now().strftime('%Y-%m-%d')
    heaterData = 0
    heaterUsage = 0    
    while True:
        # Heater System(1)
        print("------------------------------------------------------------------------")
        print("                Welcome to the Heater control System")
        print("------------------------------------------------------------------------")
        print("1. returnState; 2. changeState; 3. setTemp; 4. getTemp; Exit(press q)")
        options = input("Select Function:")
        # return state
        if options == "1":
            print("Current State:" , x2.returnState())
        # set state
        elif options == "2":
            while True:
                set = input("Set you state (0/1)： (press 'q' to Exit)")
                if set == "0" and x2.returnState() == 0:
                    print("Heater is already off, you mean turn it on?")
                    print("press 'q' to Exit")
                elif set=="1" and x2.returnState() == 1:
                    print("Heater is already on, you mean turn it off?")
                    print("press 'q' to Exit")
                else: 
                    if set == "0":
                        x2.changeState(0)
                        print("Heater is Off.")
                        end2 = time.time()
                        heaterData = round(25 / 60 * (end2 - start2),2)
                        heaterUsage += heaterData
                        print("This period using",heaterData,"watts.") 
                        x2.storeInDatabase(today,tomorrow,heaterDatabase,heaterUsage)   
                        heaterUsage = 0 
                        end2 = 0 # reset
                        break
                    elif set=="1":
                        start2 = time.time()
                        x2.changeState(1)
                        print("Heater is on.")
                        break
                    elif set == "q":
                        break
                    else:
                        print("Wrong number, please try again.")
                        False
        # set temp            
        elif options == "3":
            setT = input("Please input the Temperature you want to set:")
            if int(setT)>=16 and int(setT)<=28:
                x2.setTemp(setT)
                print("You have successfully set the temperature to", setT)
            else:
                print("Invalid, please try again.")
        
        # get current scheduled temp
        elif options == "4":
            print("Current scheduled Temperature:",x2.getTemp())
        
        elif options == "q":
            Exit()
            break

#AirConditioner System
def airCondiSys():
    global today
    global start3
    global end3
    tomorrow = datetime.datetime.now().strftime('%Y-%m-%d')
    airConditionerData = 0
    airConditionerUsage = 0
    while True:
        print("------------------------------------------------------------------------")
        print("             Welcome to the AirConditioner control system")
        print("------------------------------------------------------------------------")
        print("1. returnState; 2. changeState; 3. setTemp; 4. getTemp; 5. Exit(press q)")
        options = input("Select Function:")
        # return state
        if options == "1":
            print("Current State:" , x3.returnState())
        # set state
        elif options == "2":
            while True:
                set = input("Set you state (0/1)： (press 'q' to Exit)")
                if set == "0" and x3.returnState() == 0:
                    print("AirConditioner is already off, you mean turn it on?")
                    print("press 'q' to Exit")
                elif set=="1" and x3.returnState() == 1:
                    print("AirConditioner is already on, you mean turn it off?")
                    print("press 'q' to Exit")
                else: 
                    if set == "0":
                        x3.changeState(0)
                        print("AirConditioner is Off.")
                        end3 = time.time()
                        airConditionerData = round(25 / 60 * (end3 - start3),2)
                        airConditionerUsage += airConditionerData
                        print("This period using",airConditionerData,"watts.") 
                        x3.storeInDatabase(today,tomorrow,airConditionerDatabase,airConditionerUsage)  
                        airConditionerUsage = 0 
                        end3 = 0 # reset 
                        break
                    elif set=="1":
                        start3 = time.time()
                        x3.changeState(1)
                        print("AirConditioner is on.")
                        break
                    elif set == "q":
                        break
                    else:
                        print("Wrong number, please try again.")
                        False
        # set temp            
        elif options == "3":
            setT = input("Please input the Temperature you want to set:")
            if int(setT)>=16 and int(setT)<=28:
                x3.setTemp(setT)
                print("You have successfully set the temperature to", setT)
            else:
                print("Invalid, please try again.")
        
        # get current scheduled temp
        elif options == "4":
            print("Current scheduled Temperature:",x3.getTemp())   

        elif options == "q":
            Exit()
            break 

from light import * 
from temp import *

def sys_init(list):
    # init system
    _is_running = True

    light = list[0]
    heater = list[1]
    ac = list[2] 
    thermometer = list[3]
    roomName = list[4]

    
    print("-------------------------------------------------------")
    print(" Welcome to the America Moth Smart Home control System")
    while _is_running:
        print("-------------------------------------------------------")
        print("1. Light System. 2. Temperature System.")
        option = input("Please select your options:")
        # Light System
        if option == "1":
            if light.returnState() == 0:
                print(roomName + " light is currently off, would you like to turn it off?")
            else: 
                print(roomName + " light is currently on, would you like to turn it on?")
            check = input("(Y/N): ")
            if check =="Y" or check == "y":
                if light.changeState() == 0:
                    print(roomName + " light has been turned off")
                else: 
                    print(roomName + " light has been turned on")
                break
            else:
                break
                
        # Temp system
        elif option == "2":
            sysChoice = input("Please make your choice:1(Heater)/2(Airconditioner):")
            # Heater System(1)
            if sysChoice =="1":
                print("1. returnState; 2. changeState; 3. setTemp; 4. getTemp;")
                options = input("Select Function:")
                # return state
                if options == "1":
                    print("Current State:" , ac.returnState())
                # set state
                elif options == "2":
                    while True:
                        set = input("Set you state (0/1)：")
                        if set == "0":
                            heater.changeState(0)
                            print("Heater is Off.")
                            break
                        elif set=="1":
                            heater.changeState(1)
                            print("Heater is on.")
                            break
                        else:
                            print("Wrong number, please try again.")
                            False
                # set temp            
                elif options == "3":
                    setT = input("Please input the Temperature you want to set:")
                    if setT>="16" and setT<="28":
                        heater.setTemp(int(setT))
                        print("You have successfully set the temperature to", setT)
                        thermometer.setTemp(int(setT))
                    else:
                        print("Invalid, please try again.")

                    # energy use start to record
                
                # get current scheduled temp
                elif options == "4":
                    print("Current scheduled Temperature:",heater.getTemp())

            # Airconditioner System(2)
            elif sysChoice == "2":
                print("1. returnState; 2. changeState; 3. setTemp; 4. getTemp;")
                options = input("Select Function:")
                # return state
                if options == "1":
                    print("Current State:" , ac.returnState())
                # set state
                elif options == "2":
                    while True:
                        set = input("Set you state (0/1)：")
                        if set == "0":
                            ac.changeState(0)
                            print("Airconditioner is Off.")
                            break
                        elif set=="1":
                            ac.changeState(1)
                            print("Airconditioner is on.")
                            break
                        else:
                            print("Wrong number, please try again.")
                            False
                # set temp            
                elif options == "3":
                    setT = input("Please input the Temperature you want to set:")
                    if setT>="16" and setT<="28":
                        ac.setTemp(int(setT))
                        print("You have successfully set the temperature to", setT)
                    else:
                        print("Invalid, please try again.")

                    # energy use start to record
                
                # get current scheduled temp
                elif options == "4":
                    print("Current scheduled Temperature:",ac.getTemp())
            else:
                print("No such system exist.")

        # double check to exit the system
        elif option== "q":
            check = input("Y/N:")
            if check =="Y" or check == "y":
                _is_running = False
                print("exiting system")
            else:
                continue
from GetterAndSetter import * 
from build import *


def sys_init():
    # init system
    _is_running = True
    print("-------------------------------------------------------")
    print(" Welcome to the America Moth Smart Home control System")
    print("-------------------------------------------------------")
    while _is_running:
        print("1. Light System. 2. Temperature System. 3. Database(Energy Usage data)  Exit(press q)")
        option = input("Please select your options:")
        # Light System
        if option == "1":
            lightSys()

        # Temp system
        elif option == "2":
            sysChoice = input("Please make your choice:1(Heater)/2(Airconditioner):")
            if sysChoice =="1":
                heaterSys()

            # Airconditioner System(2)
            elif sysChoice == "2":
                airCondiSys()
            else:
                print("No such system exist.")
        
        elif option == "3":
            print("Light Energy Usage:",returnDatabase(lightDatabase))
            print("Heater Energy Usage:",returnDatabase(heaterDatabase))
            print("AirConditioner Energy Usage:",returnDatabase(airConditionerDatabase))
            print("Total Energy Usage:",totalUsage(lightDatabase,heaterDatabase,airConditionerDatabase))


        # double check to exit the system
        elif option== "q":
            check = input("Y/N:")
            if check =="Y" or check == "y":
                _is_running = False
                print("exiting system")
            else:
                continue




# run system
sys_init()



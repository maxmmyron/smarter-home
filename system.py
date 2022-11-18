from homeObjects import * 

def sys_init(list):
    # init system
    _is_running = True

    light = list[0]
    thermometer = list[1]
    roomName = list[2]
 
    print("-------------------------------------------------------")
    print(" Welcome to the America Moth Smart Home control System")
    while _is_running:
        print("-------------------------------------------------------")
        print("1. Light System. 2. Temperature System.")
        option = input("Please select your options: ")
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
            print(roomName + " temperature is currently " + str(thermometer.returnTemp()) + ", would you like to change?")
            check = input("(Y/N): ")
            if check =="Y" or check == "y":
                setT = input("Please input the Temperature you want to set:")
                if setT >="0" and setT<="28":
                    thermometer.setTemp(int(setT))
                    print("You have successfully set the temperature to ", setT)
                else:
                    print("Invalid, please try again.")
                break
            else:
                break

        # double check to exit the system
        elif option== "q":
            check = input("Y/N:")
            if check =="Y" or check == "y":
                _is_running = False
                print("exiting system")
            else:
                continue
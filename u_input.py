def sys_init(room):
    # init system
    _is_running = True
 
    print("-------------------------------------------------------")
    print(" Welcome to the America Moth Smart Home control System")
    while _is_running:
        print("-------------------------------------------------------")
        print("1. Light System. 2. Temperature System.")
        option = input("Please select your options: ")
        # Light System
        if option == "1":
            if room.light == 0:
                print(room.name + " light is currently off, would you like to turn it off?")
            else: 
                print(room.name + " light is currently on, would you like to turn it on?")
            check = input("(Y/N): ")
            if check =="Y" or check == "y":
                if room.light == 0:
                    room.light = 1
                    print(room.name + " light has been turned off")
                else: 
                    room.light = 0
                    print(room.name + " light has been turned on")
                break
            else:
                break
                
        # Temp system
        elif option == "2":
            print(room.name + " temperature is currently " + str(room.temperature) + ", would you like to change?")
            check = input("(Y/N): ")
            if check =="Y" or check == "y":
                setT = int(input("Please input the Temperature you want to set:"))
                if setT >= 0 and setT <= 28:
                    room.temperature = setT
                    print("You have successfully set the temperature to ", str(setT))
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
                print("Exiting system")
            else:
                continue
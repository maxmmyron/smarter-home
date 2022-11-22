def sys_init(room):
    # init system
    _is_running = True
 
    while _is_running:
        print("1. " + room.name + " Light System. 2. " + room.name + " Temperature System.")
        option = input("Please select your option: ")

        # Light System
        if option == "1":
            if room.light == 0:
                print(room.name + " light is currently off, would you like to turn it on?")
            else: 
                print(room.name + " light is currently on, would you like to turn it off?")
            check = input("(Y/N): ")
            if check =="Y" or check == "y":
                if room.light == 0:
                    room.light = 1
                    print(room.name + " light has been turned on, exiting system \n")
                else: 
                    room.light = 0
                    print(room.name + " light has been turned off, exiting system \n")
                break
            else:
                print("Exiting system \n")
                break
                
        # Temp system
        elif option == "2":
            setT = None
            print(room.name + " temperature is currently " + str(room.temperature) + ".")
            while type(setT) != int:    
                setT = input("Please input the temperature you want to set: ")
                try:
                    setT = int(setT)
                except: 
                    print("Invalid input")
                else:
                    if setT >= 0 and setT <= 28:
                        room.temperature = setT
                        print("You have successfully set the temperature to", str(setT))
                    else:
                        print("Invalid, please try again.")
                    print("Exiting system \n")
            break
            

        # double check to exit the system
        elif option == "q" or option == "Q":
            print("Exiting system \n")
            break
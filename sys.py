from light import * 
def sys_init():
    # init system
    _is_running = True

    x1 = light(1,0)
    x2 = heater(2,0,25)
    x3 = airConditioner(3,0,25)
    print("-------------------------------------------------------")
    print(" Welcome to the America Moth Smart Home control System")
    while _is_running:
        print("-------------------------------------------------------")
        print("1. Light System. 2. Temperature System.")
        option = input("Please select your options:")
        # Light System
        if option == "1":
            print("1. returnState. 2. changeState")
            options = input("Select Function:")
            # return state
            if options == "1":
                print("Current State:" , x1.returnState())
            # set state
            elif options == "2":
                while True:
                    set = input("Set you state (0/1)：")
                    if set == "0":
                        x1.changeState(0)
                        print("Light is Off.")
                        break
                    elif set=="1":
                        x1.changeState(1)
                        print("Light is on.")
                        break
                    else:
                        print("Wrong number, please try again.")
                        False
        # Temp system
        elif option == "2":
            sysChoice = input("Please make your choice:1(Heater)/2(Airconditioner):")
            # Heater System(1)
            if sysChoice =="1":
                print("1. returnState; 2. changeState; 3. setTemp; 4. getTemp;")
                options = input("Select Function:")
                # return state
                if options == "1":
                    print("Current State:" , x2.returnState())
                # set state
                elif options == "2":
                    while True:
                        set = input("Set you state (0/1)：")
                        if set == "0":
                            x3.changeState(0)
                            print("Heater is Off.")
                            break
                        elif set=="1":
                            x3.changeState(1)
                            print("Heater is on.")
                            break
                        else:
                            print("Wrong number, please try again.")
                            False
                # set temp            
                elif options == "3":
                    setT = input("Please input the Temperature you want to set:")
                    if setT>="16" and setT<="28":
                        x3.setTemp(setT)
                        print("You have successfully set the temperature to", setT)
                    else:
                        print("Invalid, please try again.")

                    # energy use start to record
                
                # get current scheduled temp
                elif options == "4":
                    print("Current scheduled Temperature:",x3.getTemp())

            # Airconditioner System(2)
            elif sysChoice == "2":
                print("1. returnState; 2. changeState; 3. setTemp; 4. getTemp;")
                options = input("Select Function:")
                # return state
                if options == "1":
                    print("Current State:" , x2.returnState())
                # set state
                elif options == "2":
                    while True:
                        set = input("Set you state (0/1)：")
                        if set == "0":
                            x2.changeState(0)
                            print("Airconditioner is Off.")
                            break
                        elif set=="1":
                            x2.changeState(1)
                            print("Airconditioner is on.")
                            break
                        else:
                            print("Wrong number, please try again.")
                            False
                # set temp            
                elif options == "3":
                    setT = input("Please input the Temperature you want to set:")
                    if setT>="16" and setT<="28":
                        x2.setTemp(setT)
                        print("You have successfully set the temperature to", setT)
                    else:
                        print("Invalid, please try again.")

                    # energy use start to record
                
                # get current scheduled temp
                elif options == "4":
                    print("Current scheduled Temperature:",x2.getTemp())
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




# run system
sys_init()

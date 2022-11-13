import keyboard
from light import * 
def sys_init():
    # init system
    _is_running = True

    x1 = light(1,0)
    print("--------------------------------------------")
    print("Welcome to the XXX Smart Home control System")
    while _is_running:
        print("--------------------------------------------")
        print("1. Light System. 2. Temperature System.")
        option = input("Please select your options:")
        if option == "1":
            print("1. returnState. 2. changeState")
            options = input("Select Function:")
            # return state
            if options == "1":
                print("Current State:" , x1.returnState())
            # set state
            elif options == "2":
                while True:
                    set = input("Set you state:")
                    if set == "0":
                        x1.changeState(0)
                        print("Light is Off.")
                        break
                    elif set=="1":
                        x1.changeState(1)
                        print("Light is on.")
                        break
                    else:
                        print("Wrong number, please input again.")
                        False

        elif option == "2":
            print(2222)
        if keyboard.is_pressed('q'):
            _is_running = False
            print("exiting system")


# run system
sys_init()



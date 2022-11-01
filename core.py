# primary loop function. Runs once per second and
# checks for event requests from users or schedule breakpoints

# when running program, exit by holding down "q" key.

import time
import keyboard

# total of time running from start of loop
_runtime = 0

# delta time in ms. specifies delay between loop calls.
_delta = 500

# system state. tracks whether or not system is currently idling or updating home state.
# 0 - "idle"
# 1 - "update"
sys_state = 0

# primary loop functionq


def loop():
    global _runtime
    _runtime += _delta
    print("running: time elapsed: " + str(_runtime))
    if sys_state:
        print("updating sys state")
    else:
        print("system idling")

    # TODO: implement state update logic


# primary system function. handles init of system. akin to "turning on" smart home.
def sys_init():
    # init system
    _is_running = True

    # TODO: implement state init logic

    while _is_running:
        loop()
        time.sleep(_delta / 1000)
        # read for q input to exit
        if keyboard.is_pressed('q'):
            _is_running = False
            print("exiting system")


# run system
sys_init()

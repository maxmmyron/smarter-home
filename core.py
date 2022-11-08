# primary loop function. Runs once per second and
# checks for event requests from users or schedule breakpoints

# when running program, exit by holding down "q" key.

import time
import keyboard

# total of time running from start of loop
runtime = 0

# delta time in ms. specifies delay between loop calls.
delta = 500

# system state. tracks whether or not system is currently idling or updating home state.
# 0 - "idle"
# 1 - "update"
sys_state = 0

# schedule is a double array where:
# schedule[0] = times in ms
# schedule[1] = house states to set at paired time
schedule = [
    [10000],
    [
        {
            "living_room": {
                "light": 0,
                "temperature": 21,
            },
            "kitchen": {
                "light": 1,
                "temperature": 24,
            }
        }
    ]
]

# represent users as an array where a user is:
# user.id = user id
# user.is_admin = whether or not user has admin privileges
users = [
    {id: 0, "is_admin": True},
    {id: 1, "is_admin": False},
    {id: 2, "is_admin": False},
    {id: 3, "is_admin": False},
]

# house state is a dictionary of all devices in the house
house_state = {
    "living_room": {
        "lights": 1,
        "temperature": 24,
    },
    "kitchen": {
        "lights": 0,
        "temperature": 22,
    },
}

# the target state that the system will attempt to reach
target_state = None

# primary loop functionq


def loop():
    # declare global variables
    global runtime
    global sys_state
    global target_state

    # update runtime by delta
    runtime += delta

    # get times and schedules
    times = schedule[0]
    schedules = schedule[1]

    # check if current time is in schedule struct, and if so, set target state.
    for i in range(len(times)):
        if times[i] <= runtime:
            target_state = schedules[i]
            # update system state to "update"
            sys_state = 1

    if sys_state:
        # if the target state and current state equal, set system state to "idle"
        if target_state == house_state:
            sys_state = 0
        else:
            print("updating home state")
    else:
        print("system idling")


# primary system function. handles init of system. akin to "turning on" smart home.
def sys_init():
    # init system
    _is_running = True

    # TODO: implement state init logic

    while _is_running:
        loop()
        time.sleep(delta / 1000)
        # read for q input to exit
        if keyboard.is_pressed('q'):
            _is_running = False
            print("exiting system")


# run system
sys_init()

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
    [2500],
    [
        {
            "living_room": {
                "lights": 0,
                "temperature": 21,
            },
            "kitchen": {
                "lights": 1,
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


# state update
def update_state():
    global target_state

    print(house_state)
    print(target_state)

    did_update = False

    for room in target_state:
        current_light_state = house_state[room]["lights"]
        target_light_state = target_state[room]["lights"]

        current_temp_state = house_state[room]["temperature"]
        target_temp_state = target_state[room]["temperature"]

        if current_light_state != target_light_state:
            house_state[room]["lights"] = target_light_state
            did_update = True
            print("updated light state in " + room + " from " +
                  str(current_light_state) + " to " + str(target_light_state))

        if current_temp_state > target_temp_state:
            house_state[room]["temperature"] -= 1
            did_update = True
            print("decreased temperature in " + room +
                  " from " + str(current_temp_state))
        elif current_temp_state < target_temp_state:
            house_state[room]["temperature"] += 1
            did_update = True
            print("increased temperature in " + room +
                  " from " + str(current_temp_state))

    if not did_update:
        print("no updates made; house state is already at target state")

    return did_update


# primary loop function
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
            # if sys state is idle, perform initial update loop logic
            if sys_state == 0:
                target_state = schedules[i]
                # update system state to "update"
                sys_state = 1

            # if system state is in "update", perform update loop logic
            did_update = update_state()

            # if no updates were made, set system state to "idle"
            sys_state = 0 if not did_update else 1

    if sys_state:
        # if the target state and current state equal, set system state to "idle"
        if target_state == house_state:
            sys_state = 0
        else:
            print("updating home state")
    else:
        print("system idling")

    print("runtime: " + str(runtime))


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

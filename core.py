# core.py
# initializes the core system and runs the primary logic loop.

import datetime

from home import Home
from db import Database
from schedule import Schedule
import copy

db = None
home = None
schedule = None

# runtime stats
runtime = 0
day_length = 24000
delta = 500  # eqiv to 30 min increments
day = datetime.date.today()


def loop():
    global runtime, day, day_length, delta, db, home, schedule

    if (runtime - day_length > 0):
        # update day
        day = datetime.date.today() + datetime.timedelta(days=1)
        db.add_date(day)
        runtime = 0

    # input_state = check_input()

    # schedule_state = schedule.check_schedule(runtime)

    # set target state to input state if input state is not None
    # otherwise set target state to schedule state
    # otherwise set target state to current state (no change)

    #target = (input_state or schedule_state) or home_state

    home.update(target)

    db.add_usage(home.usage)

    runtime += delta


def init():
    global db, home, schedule

    # init db
    db = Database("db")

    # init home & rooms
    # initial home state is home at 00:00
    home = Home("home")

    # add rooms to home
    home.add_room("kitchen")
    home.add_room("lounge")
    home.add_room("bedroomA")
    home.add_room("bedroomB")

    schedule = create_schedule(home)


def create_schedule(home):
    # init schedule
    schedule = Schedule()

    # NOTE: we can conveniently copy the home object
    # to create breakpoints. However since = assignment
    # only creates a reference to the original object
    # and we don't want to change the original home state,
    # we need to use deepcopy() to create a copy that
    # doesn't reference the OG home object.

    # "wake up" breakpoint
    wakeup_breakpoint = copy.deepcopy(home)  # create a deep copy
    wakeup_breakpoint.set_room("kitchen", True, 22)
    schedule.add_breakpoint("06:00", wakeup_breakpoint)

    # "leave for work"
    leave_breakpoint = copy.deepcopy(home)
    leave_breakpoint.set_room("kitchen", False, 19)
    leave_breakpoint.set_room("lounge", False, 19)
    leave_breakpoint.set_room("bedroomA", False, 19)
    leave_breakpoint.set_room("bedroomB", False, 19)
    schedule.add_breakpoint("08:00", leave_breakpoint)

    # "arrive from work" breakpoint
    arrive_breakpoint = copy.deepcopy(home)
    arrive_breakpoint.set_room("kitchen", True, 22)
    arrive_breakpoint.set_room("lounge", True, 22)
    arrive_breakpoint.set_room("bedroomA", False, 21)
    arrive_breakpoint.set_room("bedroomB", False, 21)
    schedule.add_breakpoint("17:00", arrive_breakpoint)

    # "late night" breakpoint
    late_breakpoint = copy.deepcopy(home)
    late_breakpoint.set_room("kitchen", False, 19)
    late_breakpoint.set_room("lounge", False, 22)
    late_breakpoint.set_room("bedroomA", True, 22)
    late_breakpoint.set_room("bedroomB", True, 22)
    schedule.add_breakpoint("20:00", late_breakpoint)

    # "bedtime" breakpoint
    sleep_breakpoint = copy.deepcopy(home)
    sleep_breakpoint.set_room("kitchen", False, 19)
    sleep_breakpoint.set_room("lounge", False, 19)
    sleep_breakpoint.set_room("bedroomA", False, 21)
    sleep_breakpoint.set_room("bedroomB", False, 21)
    schedule.add_breakpoint("22:00", sleep_breakpoint)

    return schedule

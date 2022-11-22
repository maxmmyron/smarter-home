# core.py
# initializes the core system and runs the primary logic loop.

import datetime

from home import Home
from db import Database
from schedule import Schedule
import copy
from time import sleep

db = None
home = None
schedule = None

# runtime stats
__tod = datetime.date.today()

day = datetime.datetime(year=__tod.year, month=__tod.month,
                        day=__tod.day, hour=0, minute=0)
'''current day and time'''

__delta = 30
'''delta in minutes to add per loop cycle'''

__loop_delta = 0.1
'''sleep time of loop in seconds'''


def loop():
    global runtime, day, __delta, db, home, schedule

    # extract date and time values from day
    date = day.date()
    time = day.time().strftime("%H:%M")

    # TODO: implement user input class
    input_state = None

    # get the schedule breakpoint current day
    # TODO: implement as "get_last_breakpoint()" such that it will continue to return the last breakpoint even if time has passed.
    schedule_state = schedule.get_breakpoint(time)

    # set target state to input state if input state is not None
    # otherwise set target state to schedule state
    # otherwise set target state to current state (no change)
    target = input_state if input_state is not None else schedule_state if schedule_state is not None else home

    # update closer to target state
    home.update(target)

    # add current state to db
    db.add_usage(date, home.usage)

    print("date: " + str(date) + " time: " + str(time))

    # update date and time
    day += datetime.timedelta(minutes=__delta)

    sleep(0.1)
    loop()


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

    loop()


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


if __name__ == "__main__":
    init()

# core.py
# initializes the core system and runs the primary logic loop.

import datetime

from home import Home
from db import Database

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

    db = Database("db")

    home = Home("home")

    home.add_room("kitchen")
    home.add_room("lounge")
    home.add_room("bedroomA")
    home.add_room("bedroomB")

    # set up database, home, and schedule
    pass

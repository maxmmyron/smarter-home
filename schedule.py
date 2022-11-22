# schedule.py
# handles schedule creation and management

import datetime


class Schedule:
    def __init__(self):
        self.breakpoints = {}

    # adds a new breakpoint state to the schedule at the specified time
    def add_breakpoint(self, time, home):
        if (time in self.breakpoints):
            raise Exception("Breakpoint already exists")

        if (not self.__validate_time(time)):
            raise Exception("Invalid time")

        self.breakpoints[time] = home
        return True

    # checks the schedule for a breakpoint at the specified time, and returns it if it exists
    def get_breakpoint(self, time):
        if (not self.__validate_time(time)):
            raise Exception("Invalid time")

        if (time in self.breakpoints):
            return self.breakpoints[time]

        return None

    # private: validates time string passed in when adding / getting a breakpoint
    def __validate_time(self, time):
        if (datetime.datetime.strptime(time, "%H:%M")):
            return True
        else:
            raise ValueError("Incorrect date format, should be HH:MM")

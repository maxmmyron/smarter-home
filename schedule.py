# schedule.py
# handles schedule creation and management

import datetime


class Schedule:
    '''Schedule class. Handles schedule creation and management.'''

    def __init__(self):
        '''creates a new schedule'''
        self.breakpoints = {}

    def add_breakpoint(self, time, home):
        '''
        adds a new breakpoint state to the schedule at the specified time

        time: the time of the breakpoint in the format "HH:MM"
        home: the home state to set at the specified time.

        raises an exception if:
        - the time is invalid
        - a breakpoint already exists at the specified time
        '''

        self.__validate_time(time)

        if (time in self.breakpoints):
            raise Exception("Breakpoint already exists")

        self.breakpoints[time] = home
        return True

    def get_breakpoint(self, time):
        '''
        checks the schedule for a breakpoint at the specified time

        time: the time of the breakpoint in the format "HH:MM"

        returns:
        - the breakpoint, if there is a breakpoint at the specified time
        - None, if there is no breakpoint at the specified time


        raises an exception if the time is invalid
        '''
        self.__validate_time(time)

        if (time in self.breakpoints):
            return self.breakpoints[time]

        return None

    # private: validates time string passed in when adding / getting a breakpoint
    def __validate_time(self, time):
        '''
        validates the time string passed in when adding / getting a breakpoint

        raises an exception if the time is not valid
        '''
        try:
            datetime.datetime.strptime(time, "%H:%M")
        except ValueError:
            raise ValueError("Incorrect date format, should be HH:MM")

        return True

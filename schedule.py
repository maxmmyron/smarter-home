# schedule.py
# handles schedule creation and management

import datetime


class Schedule:
    '''Schedule class. Handles schedule creation and management.'''

    def __init__(self):
        '''creates a new schedule'''
        self.breakpoints = {}

    def set_breakpoint(self, time, home):
        '''
        defines a breakpoint state to the schedule at the specified time. if a breakpoint already exists at the specified time, it will be overwritten.

        time: the time of the breakpoint in the format "HH:MM"
        home: the home state to set at the specified time.

        raises an exception if:
        - the time is invalid
        '''

        self._validate_time(time)

        self.breakpoints[time] = home

    def get_breakpoint(self, time):
        '''
        gets the last matching breakpoint before the specified time

        time: the time of the breakpoint in the format "HH:MM"

        returns:
        - the breakpoint, if there is a breakpoint at/before the specified time
        - None, if there is no breakpoint before the specified time
        '''

        self._validate_time(time)

        last_breakpoint = None

        for breakpoint in self.breakpoints:
            if breakpoint == time:
                last_breakpoint = self.breakpoints[breakpoint]
            if breakpoint > time:
                break

        # return the last breakpoint before the specified time
        return last_breakpoint

    def _validate_time(self, time):
        '''
        validates the time string passed in when adding / getting a breakpoint

        raises an exception if the time is not valid
        '''
        try:
            datetime.datetime.strptime(time, "%H:%M")
        except ValueError:
            raise ValueError("Incorrect date format, should be HH:MM")

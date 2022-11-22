# db.py
# handles database setup and update logic.
# keeps track of home state

import datetime


class Database:
    '''
    Database class. handles database setup for home system usage statistics.
    '''

    def __init__(self, name, date=datetime.date.today()):
        '''
        creates a new Database object with the specified name.

        name: the name of the database
        date: the date to start tracking usage from. must be a datetime.date object. defaults to today.
        '''

        self.name = name
        self.usage = {date.strftime("%d-%m-%Y"): [0, 0, 0]}
        '''
        a dictionary of usage statistics for the home.

        form of {date: [light, temp_up, temp_down]}
        '''

    def add_usage(self, date, usage=[0, 0, 0]):
        '''
        adds the specified usage to the database at the date.

        date: the date to add usage to. must be a datetime.date object.
        If the date does not exist, it will be created and added to the database.

        usage: a usage statistics struct to add to the database
        '''

        date = date.strftime("%d-%m-%Y")

        if usage == None:
            return

        if date not in self.usage:
            self.usage[date] = usage
            return

        self.usage[date][0] += usage[0]
        self.usage[date][1] += usage[1]
        self.usage[date][2] += usage[2]

    def get_usage(self, date):
        '''
        returns the usage statistics for the specified date.

        date: the date to get usage for. must be a datetime.date object *or* a string in the format "%d-%m-%Y"

        returns:
        - a usage statistics struct for the specified date.
        - None if the date does not exist in the database.
        '''

        if type(date) == datetime.date:
            date = date.strftime("%d-%m-%Y")
        else:
            # check if date is in correct format
            try:
                datetime.datetime.strptime(date, "%d-%m-%Y")
            except ValueError:
                raise ValueError("Incorrect data format, should be DD-MM-YYYY")

        if date not in self.usage:
            return None

        return self.usage[date]

# db.py
# handles database setup and update logic.
# keeps track of home state

import datetime


class Database:
    def __init__(self, name, date=datetime.date.today()):
        self.name = name
        self.usage = {date: [0, 0, 0]}

    def add_usage(self, date, usage):
        if usage == None:
            return

        if date in self.usage:
            self.usage[date][0] += usage[0]
            self.usage[date][1] += usage[1]
            self.usage[date][2] += usage[2]
        else:
            self.usage[date] = usage

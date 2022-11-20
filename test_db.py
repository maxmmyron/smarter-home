# test_db.py

import unittest
from home import Home
from db import Database
import datetime


class TestDatabase(unittest.TestCase):
    def test_init(self):
        # build database state
        date = datetime.date.today()
        db = Database("test_db", date)

        self.assertEqual(db.name, "test_db")
        self.assertEqual(db.usage, {date: [0, 0, 0]})

    def test_add_usage_light(self):
        # build database state
        date = datetime.date.today()
        db = Database("test_db", date)

        # build home state
        home = Home("test_home")
        home.add_room("test_room", True, 22)

        # run update on home object to update usage
        home.update(None)

        # add usage to database
        db.add_usage(home.get_last_usage())

        self.assertEqual(db.usage[date], [1, 0, 0])

    def test_add_usage_temp_up(self):
        # build database state
        date = datetime.date.today()
        db = Database("test_db", date)

        # build home state
        home = Home("test_home")
        home.add_room("test_room", False, 20)

        target = Home("test_home")
        target.add_room("test_room", False, 30)

        for i in range(10):
            usage = home.update(target)
            db.add_usage(usage)
            self.assertEqual(db.usage[date], [0, i+1, 0])

    def test_add_usage_temp_down(self):
        # build database state
        date = datetime.date.today()
        db = Database("test_db", date)

        # build home state
        home = Home("test_home")
        home.add_room("test_room", False, 22)

        target = Home("test_home")
        target.add_room("test_room", False, 10)

        for i in range(10):
            usage = home.update(target)
            db.add_usage(usage)
            self.assertEqual(db.usage[date], [0, 0, i+1])

    def test_add_new_date(self):
        # build database state
        date = datetime.date.today()
        db = Database("test_db", date)

        # build home state
        home = Home("test_home")
        home.add_room("test_room", True, 22)

        # add usage to database
        db.add_usage(home.getUsage())

        self.assertEqual(db.usage[date], [1, 0, 0])

        # add new date
        date = datetime.date.today() + datetime.timedelta(days=1)
        db.add_date(date)

        db.add_usage(home.getUsage())

        self.assertEqual(db.usage[date], [0, 0, 0])


if __name__ == "__main__":
    unittest.main()

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
        self.assertEqual(db.usage, {date.strftime("%d-%m-%Y"): [0, 0, 0]})

    def test_add_usage_light(self):
        # build database state
        date = datetime.date.today()
        db = Database("test_db", date)

        # build home state
        home = Home("test_home")
        home.add_room("test_room", True, 22)

        # run update on home object to update usage
        home.update(home)

        # add usage to database
        db.add_usage(date, home.usage)

        self.assertEqual(db.get_usage(date), [1, 0, 0])

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
            home.update(target)
            db.add_usage(date, home.usage)
            self.assertEqual(db.get_usage(date), [0, i+1, 0])

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
            home.update(target)
            db.add_usage(date, home.usage)
            self.assertEqual(db.get_usage(date), [0, 0, i+1])

    def test_add_new_date(self):
        # build database state
        date = datetime.date.today()
        db = Database("test_db", date)

        # build home state
        home = Home("test_home")
        home.add_room("test_room", True, 22)

        # add usage to database
        home.update(home)
        db.add_usage(date, home.usage)

        self.assertEqual(db.get_usage(date), [1, 0, 0])

        # add new date
        date = datetime.date.today() + datetime.timedelta(days=1)

        home.update(home)
        db.add_usage(date, home.usage)

        self.assertEqual(db.get_usage(date), [1, 0, 0])

    def test_get_usage(self):
        date = datetime.date.today()
        db = Database("test_db", date)

        # build home state
        home = Home("test_home")
        home.add_room("test_room", True, 22)

        # add usage to database
        home.update(home)
        db.add_usage(date, home.usage)

        self.assertEqual(db.get_usage(date), [1, 0, 0])
        self.assertEqual(db.get_usage(date.strftime("%d-%m-%Y")), [1, 0, 0])


if __name__ == "__main__":
    # run test_add_new_date to see the error
    unittest.main()

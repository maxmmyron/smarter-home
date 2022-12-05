# test_schedule.py

import unittest

from home import Home
from schedule import Schedule


class TestSchedule(unittest.TestCase):
    def test_schedule(self):
        schedule = Schedule()

        self.assertEqual(schedule.breakpoints, {})

    def test_set_breakpoint(self):
        schedule = Schedule()

        schedule_home = Home("schedule_home")
        schedule_home.add_room("schedule_room", True, 23)

        schedule.set_breakpoint("08:00", schedule_home)

        schedule_breakpoint = schedule.get_last_breakpoint("08:00")

        self.assertEqual(schedule_breakpoint.name, "schedule_home")
        self.assertEqual(
            schedule_breakpoint.rooms[0].name, "schedule_room")
        self.assertEqual(schedule_breakpoint.rooms[0].light, True)
        self.assertEqual(
            schedule_breakpoint.rooms[0].temperature, 23)

    def test_add_duplicate_breakpoint(self):
        schedule = Schedule()

        schedule_home = Home("schedule_home")
        schedule_home.add_room("schedule_room", True, 23)

        schedule.set_breakpoint("08:00", schedule_home)

        schedule_home_new = Home("schedule_home")
        schedule_home_new.add_room("schedule_room", False, 24)

        schedule.set_breakpoint("08:00", schedule_home_new)

        schedule_breakpoint = schedule.get_last_breakpoint("08:00")

        self.assertEqual(schedule_breakpoint.rooms[0].light, False)
        self.assertEqual(schedule_breakpoint.rooms[0].temperature, 24)

    def test_set_breakpoint_invalid_time(self):
        schedule = Schedule()

        schedule_home = Home("schedule_home")
        schedule_home.add_room("schedule_room", True, 23)

        # attempt to add breakpoint with invalid time
        with self.assertRaises(ValueError):
            schedule.set_breakpoint("24:00", schedule_home)

        with self.assertRaises(ValueError):
            schedule.set_breakpoint("00:60", schedule_home)

    def test_get_last_breakpoint(self):
        schedule = Schedule()

        schedule_home = Home("schedule_home")
        schedule_home.add_room("schedule_room", True, 23)

        schedule_homeB = Home("schedule_home")
        schedule_homeB.add_room("schedule_room", False, 24)

        schedule.set_breakpoint("08:00", schedule_home)

        schedule.set_breakpoint("09:00", schedule_homeB)

        schedule_breakpoint = schedule.get_last_breakpoint("08:00")

        self.assertEqual(schedule_breakpoint.name, "schedule_home")
        self.assertEqual(schedule_breakpoint.rooms[0].name, "schedule_room")
        self.assertEqual(schedule_breakpoint.rooms[0].light, True)
        self.assertEqual(schedule_breakpoint.rooms[0].temperature, 23)

        schedule_breakpoint = schedule.get_last_breakpoint("08:30")

        self.assertEqual(schedule_breakpoint, None)

        schedule_breakpoint = schedule.get_last_breakpoint("09:00")

        self.assertEqual(schedule_breakpoint.name, "schedule_home")
        self.assertEqual(schedule_breakpoint.rooms[0].name, "schedule_room")
        self.assertEqual(schedule_breakpoint.rooms[0].light, False)
        self.assertEqual(schedule_breakpoint.rooms[0].temperature, 24)

        schedule_breakpoint = schedule.get_last_breakpoint("09:30")

        self.assertEqual(schedule_breakpoint, None)

    def test_get_last_breakpoint_invalid_time(self):
        schedule = Schedule()

        schedule_home = Home("schedule_home")
        schedule_home.add_room("schedule_room", True, 23)

        schedule.set_breakpoint("08:00", schedule_home)

        # attempt to get breakpoint with invalid time
        with self.assertRaises(ValueError):
            schedule.get_last_breakpoint("24:00")

        with self.assertRaises(ValueError):
            schedule.get_last_breakpoint("00:60")

    def test_get_last_breakpoint_nonexistent_time(self):
        schedule = Schedule()

        nonexistent_breakpoint = schedule.get_last_breakpoint("08:00")

        self.assertEqual(nonexistent_breakpoint, None)


if __name__ == '__main__':
    unittest.main()

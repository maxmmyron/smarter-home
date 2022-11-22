# test_schedule.py

import unittest

from home import Home
from schedule import Schedule


class TestSchedule(unittest.TestCase):
    def test_schedule(self):
        schedule = Schedule()

        self.assertEqual(schedule.breakpoints, {})

    def test_add_breakpoint(self):
        schedule = Schedule()

        schedule_home = Home("schedule_home")
        schedule_home.add_room("schedule_room", True, 23)

        schedule.add_breakpoint("08:00", schedule_home)

        schedule_breakpoint = schedule.get_breakpoint("08:00")

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

        schedule.add_breakpoint("08:00", schedule_home)

        # attempt to add duplicate breakpoint
        with self.assertRaises(Exception):
            schedule.add_breakpoint("08:00", schedule_home)

    def test_add_breakpoint_invalid_time(self):
        schedule = Schedule()

        schedule_home = Home("schedule_home")
        schedule_home.add_room("schedule_room", True, 23)

        # attempt to add breakpoint with invalid time
        with self.assertRaises(ValueError):
            schedule.add_breakpoint("24:00", schedule_home)

        with self.assertRaises(ValueError):
            schedule.add_breakpoint("00:60", schedule_home)

    def test_get_breakpoint(self):
        schedule = Schedule()

        schedule_home = Home("schedule_home")
        schedule_home.add_room("schedule_room", True, 23)

        schedule.add_breakpoint("08:00", schedule_home)

        schedule_breakpoint = schedule.get_breakpoint("08:00")

        self.assertEqual(schedule_breakpoint.name, "schedule_home")
        self.assertEqual(schedule_breakpoint.rooms[0].name, "schedule_room")
        self.assertEqual(schedule_breakpoint.rooms[0].light, True)
        self.assertEqual(schedule_breakpoint.rooms[0].temperature, 23)

    def test_get_breakpoint_invalid_time(self):
        schedule = Schedule()

        schedule_home = Home("schedule_home")
        schedule_home.add_room("schedule_room", True, 23)

        schedule.add_breakpoint("08:00", schedule_home)

        # attempt to get breakpoint with invalid time
        with self.assertRaises(ValueError):
            schedule.get_breakpoint("24:00")

        with self.assertRaises(ValueError):
            schedule.get_breakpoint("00:60")

    def test_get_breakpoint_nonexistent_time(self):
        schedule = Schedule()

        nonexistent_breakpoint = schedule.get_breakpoint("08:00")

        self.assertEqual(nonexistent_breakpoint, None)


if __name__ == '__main__':
    unittest.main()

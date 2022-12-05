# test_core.py

import unittest
from core import Core


class TestCore(unittest.TestCase):
    def test_init(self):
        # build home state
        core = Core()

        self.assertEqual(core.db.name, "db")

        self.assertEqual(core.home.name, "home")
        self.assertEqual(core.home.rooms[0].name, "Sitting Room")
        self.assertEqual(core.home.rooms[0].light, False)
        self.assertEqual(core.home.rooms[0].temperature, 21)

        self.assertEqual(core.home.rooms[1].name, "Kitchen")
        self.assertEqual(core.home.rooms[1].light, False)
        self.assertEqual(core.home.rooms[1].temperature, 21)

        self.assertEqual(core.home.rooms[2].name, "Dining Room")
        self.assertEqual(core.home.rooms[2].light, False)
        self.assertEqual(core.home.rooms[2].temperature, 21)

        self.assertEqual(core.home.rooms[3].name, "Bedroom")
        self.assertEqual(core.home.rooms[3].light, False)
        self.assertEqual(core.home.rooms[3].temperature, 21)

        # assert schedule
        self.assertEqual(len(core.schedule.breakpoints), 5)
        times = ["06:00", "08:00", "17:00", "20:00", "22:00"]

        # assert each breakpoint at time exists
        for i in range(len(core.schedule.breakpoints)):
            self.assertIsNotNone(core.schedule.breakpoints[times[i]])


if __name__ == '__main__':
    unittest.main()

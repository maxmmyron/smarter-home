# test_home.py

import unittest

from home import Home


class TestHome(unittest.TestCase):
    def test_home(self):
        # build home state
        home = Home("test_home")

        self.assertEqual(home.name, "test_home")
        self.assertEqual(home.rooms, [])

    def test_add_room(self):
        # build home state and add rooms
        home = Home("test_home")
        home.add_room("test_room")

        self.assertEqual(home.rooms[0] in home.rooms, True)
        self.assertEqual(home.rooms[0].name, "test_room")
        self.assertEqual(home.rooms[0].light, False)
        self.assertEqual(home.rooms[0].temperature, 21)

    def test_add_duplicate_room(self):
        # build home state and add rooms
        home = Home("test_home")
        home.add_room("test_room")

        # attempt to add duplicate room
        with self.assertRaises(Exception):
            home.add_room("test_room")

    def test_add_custom_room(self):
        # build home state and add rooms
        home = Home("test_home")
        home.add_room("test_room", True, 22)

        self.assertEqual(home.rooms[0] in home.rooms, True)
        self.assertEqual(home.rooms[0].name, "test_room")
        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 22)

    def test_state_change(self):
        # build home state and add rooms
        home = Home("test_home")
        home.add_room("test_room", False, 20)

        # build target home state
        home_target = Home("test_home")
        home_target.add_room("test_room", True, 22)

        # attempt home state change
        self.assertEqual(home.update(home_target), True)
        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 21)

        # finish state change
        self.assertEqual(home.update(home_target), True)
        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 22)

        # attempt home state change to same state
        self.assertEqual(home.update(home_target), False)
        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 22)


if __name__ == "__main__":
    unittest.main()

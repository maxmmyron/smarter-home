# test_home.py

import unittest
from home import Home


class TestHome(unittest.TestCase):
    def test_home(self):
        # build home state
        home = Home("test_home")

        self.assertEqual(home.name, "test_home")
        self.assertEqual(home.rooms, [])
        self.assertEqual(home.usage, [0, 0, 0])

    def test_add_room(self):
        # build home state and add rooms
        home = Home("test_home")
        home.add_room("test_room")

        self.assertEqual(home.rooms[0] in home.rooms, True)
        self.assertEqual(home.rooms[0].name, "test_room")
        self.assertEqual(home.rooms[0].light, False)
        self.assertEqual(home.rooms[0].temperature, 21)
        self.assertEqual(home.rooms[0].usage, [0, 0, 0])

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
        self.assertEqual(home.rooms[0].usage, [0, 0, 0])

    def test_state_change(self):
        # build home state and add rooms
        home = Home("test_home")
        home.add_room("test_room", False, 20)

        # build target home state
        home_target = Home("test_home")
        home_target.add_room("test_room", True, 22)

        # system should reach target state incrementally

        # attempt home state change
        self.assertEqual(home.update(home_target), True)
        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 21)
        self.assertEqual(home.rooms[0].usage, [1, 1, 0])

        # finish state change
        self.assertEqual(home.update(home_target), True)
        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 22)
        self.assertEqual(home.rooms[0].usage, [1, 1, 0])

        # attempt home state change to same state
        self.assertEqual(home.update(home_target), False)
        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 22)
        self.assertEqual(home.rooms[0].usage, [1, 0, 0])

    def test_state_change_multiple_rooms(self):
        home = Home("test_home")

        # build home state and add rooms
        home.add_room("test_room_1")
        home.add_room("test_room_2", True, 24)

        # build target home state
        home_target = Home("test_home")

        home_target.add_room("test_room_1", True, 23)
        home_target.add_room("test_room_2", False, 21)

        # system should reach target state incrementally

        # attempt home state change
        self.assertEqual(home.update(home_target), True)

        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 22)
        self.assertEqual(home.rooms[0].usage, [1, 1, 0])

        self.assertEqual(home.rooms[1].light, False)
        self.assertEqual(home.rooms[1].temperature, 23)
        self.assertEqual(home.rooms[1].usage, [0, 0, 1])

        # continue
        self.assertEqual(home.update(home_target), True)

        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 23)
        self.assertEqual(home.rooms[0].usage, [1, 1, 0])

        self.assertEqual(home.rooms[1].light, False)
        self.assertEqual(home.rooms[1].temperature, 22)
        self.assertEqual(home.rooms[1].usage, [0, 0, 1])

        # continue
        self.assertEqual(home.update(home_target), True)

        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 23)
        self.assertEqual(home.rooms[0].usage, [1, 0, 0])

        self.assertEqual(home.rooms[1].light, False)
        self.assertEqual(home.rooms[1].temperature, 21)
        self.assertEqual(home.rooms[1].usage, [0, 0, 1])

        # attempt finished state change
        self.assertEqual(home.update(home_target), False)

        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 23)
        self.assertEqual(home.rooms[0].usage, [1, 0, 0])

        self.assertEqual(home.rooms[1].light, False)
        self.assertEqual(home.rooms[1].temperature, 21)
        self.assertEqual(home.rooms[1].usage, [0, 0, 0])

    def test_set_room(self):
        home = Home("test_home")

        # build home state and add rooms
        home.add_room("test_room_1")

        home.set_room("test_room_1", True, 23)

        self.assertEqual(home.rooms[0].light, True)
        self.assertEqual(home.rooms[0].temperature, 23)


if __name__ == "__main__":
    unittest.main()

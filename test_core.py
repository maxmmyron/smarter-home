# test_core.py

import unittest
from core import init

class TestCore(unittest.TestCase):
    def test_init(self):
        # build home state
        home = init()

        self.assertEqual(home.name, "test_home")
        self.assertEqual(home.rooms, [])


if __name__ == '__main__':
    unittest.main()

# test_input.py

import unittest
from home import *
from user_input import sys_init
import unittest 
from unittest import mock


class TestUserInput(unittest.TestCase):
   
    @mock.patch('user_input.input', create=True)
    def test_light_sucess(self, answers):
        test_home = Home("test")
        test_home.add_room("test_room", True, 23)
        answers.side_effect = ['1', 'Y']
        sys_init(test_home.rooms[0])
        self.assertEquals(test_home.rooms[0].light, False)
        
    @mock.patch('user_input.input', create=True)
    def test_light_failure(self, answers):
        test_home = Home("test")
        test_home.add_room("test_room", True, 23)
        answers.side_effect = ['1', 'abcdefg']
        sys_init(test_home.rooms[0])
        self.assertEquals(test_home.rooms[0].light, True)

    @mock.patch('user_input.input', create=True)
    def test_light_off(self, answers):
        test_home = Home("test")
        test_home.add_room("test_room", False, 23)
        answers.side_effect = ['1', 'Y']
        sys_init(test_home.rooms[0])
        self.assertEquals(test_home.rooms[0].light, True)

    @mock.patch('user_input.input', create=True)
    def test_temp(self, answers):
        test_home = Home("test")
        test_home.add_room("test_room", True, 23)
        answers.side_effect = ['2', '15']
        sys_init(test_home.rooms[0])
        self.assertEquals(test_home.rooms[0].temperature, 15)

    @mock.patch('user_input.input', create=True)
    def test_temp_negative_input(self, answers):
        test_home = Home("test")
        test_home.add_room("test_room", True, 23)
        answers.side_effect = ['2', '-1']
        sys_init(test_home.rooms[0])
        self.assertEquals(test_home.rooms[0].temperature, 23)

    @mock.patch('user_input.input', create=True)
    def test_temp_non_number_input(self, answers):
        test_home = Home("test")
        test_home.add_room("test_room", True, 23)
        answers.side_effect = ['2', 'a', 'a', 'a', '10']
        sys_init(test_home.rooms[0])
        self.assertEquals(test_home.rooms[0].temperature, 10)


import unittest
import datetime


class TestCore(unittest.TestCase):
    # def test_sys_init(self):
    #     sys_init(False)  # False = don't perform loop logic

    #     self.assertEqual(__system_running, 1)
    #     self.assertEqual(__system_state, 0)

    def test_update_state(self):
        _target_state = {
            "kitchen": {
                "lights": 1,
                "temperature": 22,
            },
        }

        _test_state = {
            "kitchen": {
                "lights": 0,
                "temperature": 20,
            }
        }

        # test that running update_state() will increment the temperature by 1 if the target state temperature is higher
        self.assertEqual(
            update_state(_test_state, _target_state),
            {
                "kitchen": {
                    "lights": 1,
                    "temperature": 21,
                }
            }
        )

        # test that running update_state() will decrement the temperature if the target temp is lower
        _test_state = {
            "kitchen": {
                "lights": 0,
                "temperature": 24,
            }
        }

        self.assertEqual(
            update_state(_test_state, _target_state),
            {
                "kitchen": {
                    "lights": 1,
                    "temperature": 23,
                }
            }
        )

        # test that running update_state() will not make any changes to the state if it is already at the target state

        _test_state = {
            "kitchen": {
                "lights": 1,
                "temperature": 22,
            }
        }

        self.assertEqual(
            update_state(_test_state, _target_state),
            {
                "kitchen": {
                    "lights": 1,
                    "temperature": 22,
                }
            }
        )

    def test_retrieve_schedule_state(self):
        # test that retrieve_schedule_state, given a time, will return the correct schedule

        _time = datetime.time(12, 0)

        _schedule = {
            "12:00": {
                "kitchen": {
                    "lights": 1,
                    "temperature": 22,
                }
            }
        }

        self.assertEqual(
            retrieve_schedule_state(_time, _schedule),
            {
                "kitchen": {
                    "lights": 1,
                    "temperature": 22,
                }
            }
        )

        # test that retrieve_schedule_state, given a time, will return none if there is no schedule for that time

        _time = datetime.time(13, 0)

        self.assertEqual(
            retrieve_schedule_state(_time, _schedule),
            None
        )

        # test that retrieve_schedule_state, given an invalid time, will throw an error

        # valid times are in datetime.time format (hour, minute, second)

    def test_get_user_state(self):
        self.assertEqual(get_user_state(), True)

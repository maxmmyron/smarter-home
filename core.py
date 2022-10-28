# primary loop function. Runs once per second and
# checks for event requests from users or schedule breakpoints
import time

import graphman

# total of time running from start of loop
_runtime = 0

# delta time in ms. specifies delay between loop calls.
_delta = 16


# primary loop function
def loop():
    _runtime += _delta

    # TODO: implement state update logic


# primary system function. handles init of system. akin to "turn on" event.
def sys():
    # init system
    _is_running = True

    # TODO: implement state init logic

    while _is_running:
        loop()
        time.sleep(_delta / 1000)

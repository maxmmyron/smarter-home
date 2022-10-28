# primary loop function. Runs once per second and
# checks for event requests from users or schedule breakpoints
import time

# running total of time running, in ms.
_runtime = 0

# delta time in ms. specifies delay between loop calls.
_delta = 16


# primary loop function
def loop():
    _runtime += _delta


# primary system function. handles init of system. akin to "turn on" event.
def sys():
    _is_running = True

    while _is_running:
        loop()
        time.sleep(_delta / 1000)

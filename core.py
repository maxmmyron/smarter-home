# primary loop function. Runs once per second and
# checks for event requests from users or schedule breakpoints
runtime = 0


# primary loop function
def loop(delta):
    runtime += delta


# primary system function. handles init of system. akin to "turn on" event.
def sys():
    running = True
    delta = 16

    while running:
        loop(delta)

# core.py
# initializes the core system and runs the primary logic loop.

import datetime
import copy
import tkinter as tk

from home import Home
from db import Database
from schedule import Schedule
from user_input import sys_init


class Core(tk.Tk):
    home = None
    db = None
    schedule = None

    _tod = datetime.date.today()

    day = datetime.datetime(
        year=_tod.year, month=_tod.month, day=_tod.day, hour=0, minute=0)

    _delta = 60

    _loop_delta = 1200

    def __init__(self):
        super().__init__()
        self.time = None

        self.title("Home")
        self.geometry("1000x800")
        self.resizable(False, False)

        self._init_data()
        self._init_vis()

    def run(self):
        '''
        starts logic loop and tkinter mainloop
        '''

        self._loop()
        self.mainloop()

    def update_graphics(self):
        for room in self.home.rooms:
            # delete old room data
            self.canvas.delete(room.name)
            self.canvas.delete(room.name + "label")
            self.canvas.delete(room.name + "temp")

            self._build_tk_room(room)

    def _init_vis(self):
        '''
        private

        inits tkinter widgets and builds home from initial home object
        '''

        rooms = self.home.rooms
        self.canvas = tk.Canvas(self, width=500, height=500, bg="white")

        for room in rooms:
            self._build_tk_room(room)

        self.canvas.pack()

        def user_input(self, room):
            sys_init(room)

            self.canvas.delete(room.name)
            if room.light == 1:
                self.canvas.create_rectangle(
                    room.x, room.y, room.x + 200, room.y + 200, tags=room.name, fill="yellow")
            else:
                self.canvas.create_rectangle(
                    room.x, room.y, room.x + 200, room.y + 200, tags=room.name, fill="cyan")
            tempX = room.x + 100
            tempY = room.y + 50
            self.canvas.delete(room.name + "label")
            self.canvas.create_text(
                tempX, tempY, text=room.name, tags=room.name + "label", fill="black", font=('Helvetica 15 bold'))
            self.canvas.delete(room.name + "temp")
            self.canvas.create_text(tempX, tempY + 70, text=str(
                room.temperature), tags=room.name + "temp", fill="red", font=('Helvetica 15 bold'))

        a = tk.Button(self, text=rooms[0].name,
                      command=lambda: user_input(self, rooms[0]))
        b = tk.Button(self, text=rooms[1].name,
                      command=lambda: user_input(self, rooms[1]))
        c = tk.Button(self, text=rooms[2].name,
                      command=lambda: user_input(self, rooms[2]))
        d = tk.Button(self, text=rooms[3].name,
                      command=lambda: user_input(self, rooms[3]))
        a.pack()
        b.pack()
        c.pack()
        d.pack()

        # add a text widget to display the word "Hello"
        self.tempLabel = tk.Label(self, text="")
        self.tempLabel.pack()

        self.dateLabel = tk.Label(self, text="")
        self.dateLabel.pack()

    def _build_tk_room(self, room):
        light_fill = "yellow" if room.light else "cyan"

        self.canvas.create_rectangle(
            room.x, room.y, room.x + 200, room.y + 200, tags=room.name, fill=light_fill)
        self.canvas.create_text(
            room.x + 100, room.y + 50, text=room.name, tags=room.name + "-label", fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(room.x + 100, room.y + 120, text=str(
            room.temperature), tags=room.name + "temp", fill="red", font=('Helvetica 15 bold'))

    def _init_data(self):
        '''
        private

        inits db, home, and schedule
        '''

        # init db
        self.db = Database("db")

        # init home & rooms
        # initial home state is home at 00:00
        self.home = Home("home")

        # add rooms to home
        self.home.add_room("kitchen", False, 21, 50, 50)
        self.home.add_room("lounge", False, 21, 250, 50)
        self.home.add_room("bedroomA", False, 21, 50, 250)
        self.home.add_room("bedroomB", False, 21, 250, 250)

        self.schedule = self._init_schedule(self.home)

    def _init_schedule(self, home):
        '''
        private

        creates a new schedule

        home: the home object to model the schedule breakpoints off of

        returns: a new schedule object
        '''

        schedule = Schedule()

        # NOTE: we can conveniently copy the home object
        # to create breakpoints. However since = assignment
        # only creates a reference to the original object
        # and we don't want to change the original home state,
        # we need to use deepcopy() to create a copy that
        # doesn't reference the OG home object.

        # "wake up" breakpoint
        wakeup_breakpoint = copy.deepcopy(home)  # create a deep copy
        wakeup_breakpoint.set_room("kitchen", True, 22)
        schedule.add_breakpoint("06:00", wakeup_breakpoint)

        # "leave for work"
        leave_breakpoint = copy.deepcopy(home)
        leave_breakpoint.set_room("kitchen", False, 19)
        leave_breakpoint.set_room("lounge", False, 19)
        leave_breakpoint.set_room("bedroomA", False, 19)
        leave_breakpoint.set_room("bedroomB", False, 19)
        schedule.add_breakpoint("08:00", leave_breakpoint)

        # "arrive from work" breakpoint
        arrive_breakpoint = copy.deepcopy(home)
        arrive_breakpoint.set_room("kitchen", True, 22)
        arrive_breakpoint.set_room("lounge", True, 22)
        arrive_breakpoint.set_room("bedroomA", False, 21)
        arrive_breakpoint.set_room("bedroomB", False, 21)
        schedule.add_breakpoint("17:00", arrive_breakpoint)

        # "late night" breakpoint
        late_breakpoint = copy.deepcopy(home)
        late_breakpoint.set_room("kitchen", False, 19)
        late_breakpoint.set_room("lounge", False, 22)
        late_breakpoint.set_room("bedroomA", True, 22)
        late_breakpoint.set_room("bedroomB", True, 22)
        schedule.add_breakpoint("20:00", late_breakpoint)

        # "bedtime" breakpoint
        sleep_breakpoint = copy.deepcopy(home)
        sleep_breakpoint.set_room("kitchen", False, 19)
        sleep_breakpoint.set_room("lounge", False, 19)
        sleep_breakpoint.set_room("bedroomA", False, 21)
        sleep_breakpoint.set_room("bedroomB", False, 21)
        schedule.add_breakpoint("22:00", sleep_breakpoint)

        return schedule

    def _loop(self):
        # extract date and time values from day
        date = self.day.date()
        time = self.day.time().strftime("%H:%M")
        self.time = time

        # TODO: implement user input class
        input_state = None

        # get the schedule breakpoint current day
        # TODO: implement as "get_last_breakpoint()" such that it will continue to return the last breakpoint even if time has passed.
        schedule_state = self.schedule.get_last_breakpoint(time)

        # set target state to input state if input state is not None
        # otherwise set target state to schedule state
        # otherwise set target state to current state (no change)
        target = input_state if input_state is not None else schedule_state if schedule_state is not None else self.home

        # update closer to target state
        update_check = self.home.update(target)
        if update_check == True:
            self.update_graphics()

        # add current state to db
        self.db.add_usage(date, self.home.usage)

        # update tkinter vis
        self._update_vis()

        # update date and time
        self.day += datetime.timedelta(minutes=self._delta)

        self.after(self._loop_delta, self._loop)
        pass

    def _update_vis(self):
        '''
        private

        updates tkinter widgets
        '''

        # update label
        self.tempLabel.config(text=self.home.rooms[0].temperature)
        self.dateLabel.config(text=self.day.strftime("%d/%m/%Y %H:%M"))


if __name__ == "__main__":
    core = Core()
    core.run()

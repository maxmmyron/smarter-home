# core.py
# initializes the core system and runs the primary logic loop.

import datetime
import copy
import tkinter as tk

from home import Home
from db import Database
from schedule import Schedule
from user_input import construct_user_state


class Core(tk.Tk):
    home = None
    db = None
    schedule = None
    schedule_state = None

    _tod = datetime.date.today()

    day = datetime.datetime(
        year=_tod.year, month=_tod.month, day=_tod.day, hour=0, minute=0)

    _delta = 10

    _loop_delta = 1000

    # user override state
    input_state = None

    def __init__(self):
        super().__init__()
        self.time = None

        self.title("Home")
        self.geometry("600x500")
        self.resizable(False, False)

        self._init_data()
        self._init_vis()

    def run(self):
        '''
        starts logic loop and tkinter mainloop
        '''

        print("------------------------------------------------------")
        print("Welcome to the American Moth Smart Home Control System")
        print("-------------------------------------------------------")

        self._loop()
        self.mainloop()

    def _init_data(self):
        '''
        private

        inits db, home, and schedule
        '''

        self.db = Database("db")

        self.home = Home("home")

        # add rooms to home
        self.home.add_room("Sitting Room", False, 21, 0, 0)
        self.home.add_room("Kitchen", False, 21, 200, 0)
        self.home.add_room("Dining Room", False, 21, 0, 200)
        self.home.add_room("Bedroom", False, 21, 200, 200)

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
        wakeup_breakpoint.set_room("Sitting Room", True, 22)
        schedule.set_breakpoint("06:00", wakeup_breakpoint)

        # "leave for work"
        leave_breakpoint = copy.deepcopy(home)
        leave_breakpoint.set_room("Sitting Room", False, 19)
        leave_breakpoint.set_room("Kitchen", False, 19)
        leave_breakpoint.set_room("Dining Room", False, 19)
        leave_breakpoint.set_room("Bedroom", False, 19)
        schedule.set_breakpoint("08:00", leave_breakpoint)

        # "arrive from work" breakpoint
        arrive_breakpoint = copy.deepcopy(home)
        arrive_breakpoint.set_room("Sitting Room", True, 22)
        arrive_breakpoint.set_room("Kitchen", True, 22)
        arrive_breakpoint.set_room("Dining Room", False, 21)
        arrive_breakpoint.set_room("Bedroom", False, 21)
        schedule.set_breakpoint("17:00", arrive_breakpoint)

        # "late night" breakpoint
        late_breakpoint = copy.deepcopy(home)
        late_breakpoint.set_room("Sitting Room", False, 19)
        late_breakpoint.set_room("Kitchen", False, 22)
        late_breakpoint.set_room("Dining Room", True, 22)
        late_breakpoint.set_room("Bedroom", True, 22)
        schedule.set_breakpoint("20:00", late_breakpoint)

        # "bedtime" breakpoint
        sleep_breakpoint = copy.deepcopy(home)
        sleep_breakpoint.set_room("Sitting Room", False, 19)
        sleep_breakpoint.set_room("Kitchen", False, 19)
        sleep_breakpoint.set_room("Dining Room", False, 21)
        sleep_breakpoint.set_room("Bedroom", False, 21)
        schedule.set_breakpoint("22:00", sleep_breakpoint)

        return schedule

    def _init_vis(self):
        '''
        private

        inits tkinter widgets and builds home from initial home object
        '''
        # TODO: improve vis look

        self.dateLabel = tk.Label(self, text="", font=("Arial 13"))
        self.dateLabel.pack(side="right")

        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack(side="top")

        for room in self.home.rooms:
            self._build_tk_room(room)

        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", fill="both",
                          expand=True, padx=10, pady=10)

        state_override_button = tk.Button(
            button_frame, text="Override State", command=self._override_state)
        state_override_button.pack(anchor=tk.CENTER, padx=5, pady=5)

        data_button = tk.Button(button_frame, text="Database",
                                command=lambda: self.db.print_usage())
        data_button.pack(anchor=tk.CENTER, padx=5, pady=5)

    def _override_state(self):
        self.input_state = construct_user_state(self, self.home)

    def _build_tk_room(self, room):
        light_fill = "yellow" if room.light else "cyan"

        self.canvas.create_rectangle(
            room.x, room.y, room.x + 200, room.y + 200, tags=room.name, fill=light_fill)
        self.canvas.create_text(
            room.x + 100, room.y + 50, text=room.name, tags=room.name + "_label", fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(room.x + 100, room.y + 120, text="{:.2f}".format(
            room.temperature), tags=room.name + "_temp", fill="red", font=('Helvetica 15 bold'))

    def _draw(self):
        self.dateLabel.config(text=self.day.strftime("%d/%m/%Y %H:%M"))

        for room in self.home.rooms:
            # delete old room data
            self.canvas.delete(room.name)
            self.canvas.delete(room.name + "_label")
            self.canvas.delete(room.name + "_temp")

            self._build_tk_room(room)

    _last_schedule_state = None

    def _loop(self):
        # extract date and time values from day
        date = self.day.date()
        time = self.day.time().strftime("%H:%M")
        self.time = time

        schedule_state = self.schedule.get_last_breakpoint(time)
        if (schedule_state != self._last_schedule_state):
            # account for day change
            if (not bool(schedule_state)):
                schedule_state = self._last_schedule_state
            else:
                self._last_schedule_state = schedule_state
                self.input_state = None

        # set target state to input state if input state is not None
        # otherwise set target state to schedule state
        # otherwise, set target state to current state (no change)
        target = self.input_state if self.input_state is not None else schedule_state if schedule_state is not None else self.home

        # update closer to target state
        self.home.update(target)

        self._draw()

        # add current state to db
        self.db.add_usage(date, self.home.usage)

        # update date and time
        self.day += datetime.timedelta(minutes=self._delta)

        self.after(self._loop_delta, self._loop)


if __name__ == "__main__":
    core = Core()
    core.run()

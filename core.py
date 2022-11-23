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

    __tod = datetime.date.today()

    day = datetime.datetime(
        year=__tod.year, month=__tod.month, day=__tod.day, hour=0, minute=0)

    __delta = 60

    __loop_delta = 1200

    def __init__(self):
        super().__init__()
        self.time = None

        self.title("Home")
        self.geometry("500x500")
        self.resizable(False, False)

        self.__init_data()
        self.__init_vis()

    def run(self):
        '''
        starts logic loop and tkinter mainloop
        '''

        self.__loop()
        self.mainloop()

    def update_graphics(self):
        for room in self.home.rooms:
            self.my_canvas.delete(room.name)
            if room.light == 1:
                self.my_canvas.create_rectangle(
                    room.x, room.y, room.x + 200, room.y + 200, tags=room.name, fill="yellow")
            else:
                self.my_canvas.create_rectangle(
                    room.x, room.y, room.x + 200, room.y + 200, tags=room.name, fill="cyan")
            tempX = room.x + 100
            tempY = room.y + 50
            self.my_canvas.delete(room.name + "label")
            self.my_canvas.create_text(
                tempX, tempY, text=room.name, tags=room.name + "label", fill="black", font=('Helvetica 15 bold'))
            self.my_canvas.delete(room.name + "temp")
            self.my_canvas.create_text(tempX, tempY + 70, text=str(
                room.temperature), tags=room.name + "temp", fill="red", font=('Helvetica 15 bold'))

    def __init_vis(self):
        '''
        private

        inits tkinter widgets and builds home from initial home object
        '''

        rooms = self.home.rooms
        self.my_canvas = tk.Canvas(self, width=400, height=400, bg="white")

        self.my_canvas.create_rectangle(
            0, 0, 200, 200, tags=rooms[0].name, fill="cyan")
        rooms[0].x = 0
        rooms[0].y = 0
        self.my_canvas.create_text(
            100, 50, text=rooms[0].name, tags=rooms[0].name + "label", fill="black", font=('Helvetica 15 bold'))
        self.my_canvas.create_text(100, 120, text=str(
            rooms[0].temperature), tags=rooms[0].name + "temp", fill="red", font=('Helvetica 15 bold'))

        self.my_canvas.create_rectangle(
            200, 0, 400, 200, tags=rooms[1].name, fill="cyan")
        rooms[1].x = 200
        rooms[1].y = 0
        self.my_canvas.create_text(
            300, 50, text=rooms[1].name, tags=rooms[1].name + "label", fill="black", font=('Helvetica 15 bold'))
        self.my_canvas.create_text(300, 120, text=str(
            rooms[1].temperature), tags=rooms[1].name + "temp", fill="red", font=('Helvetica 15 bold'))

        self.my_canvas.create_rectangle(
            0, 200, 200, 400, tags=rooms[2].name, fill="cyan")
        rooms[2].x = 0
        rooms[2].y = 200
        self.my_canvas.create_text(
            100, 250, text=rooms[2].name, tags=rooms[2].name + "label", fill="black", font=('Helvetica 15 bold'))
        self.my_canvas.create_text(100, 320, text=str(
            rooms[2].temperature), tags=rooms[2].name + "temp", fill="red", font=('Helvetica 15 bold'))

        self.my_canvas.create_rectangle(
            200, 200, 400, 400, tags=rooms[3].name, fill="cyan")
        rooms[3].x = 200
        rooms[3].y = 200
        self.my_canvas.create_text(
            300, 250, text=rooms[3].name, tags=rooms[3].name + "label", fill="black", font=('Helvetica 15 bold'))
        self.my_canvas.create_text(300, 320, text=str(
            rooms[3].temperature), tags=rooms[3].name + "temp", fill="red", font=('Helvetica 15 bold'))
        self.my_canvas.pack()

        def user_input(self, room):
            sys_init(room)

            self.my_canvas.delete(room.name)
            if room.light == 1:
                self.my_canvas.create_rectangle(
                    room.x, room.y, room.x + 200, room.y + 200, tags=room.name, fill="yellow")
            else:
                self.my_canvas.create_rectangle(
                    room.x, room.y, room.x + 200, room.y + 200, tags=room.name, fill="cyan")
            tempX = room.x + 50
            tempY = room.y + 25
            self.my_canvas.delete(room.name + "label")
            self.my_canvas.create_text(
                tempX, tempY, text=room.name, tags=room.name + "label", fill="black", font=('Helvetica 15 bold'))
            self.my_canvas.delete(room.name + "temp")
            self.my_canvas.create_text(tempX, tempY + 70, text=str(
                room.temperature), tags=room.name + "temp", fill="red", font=('Helvetica 15 bold'))

        a = tk.Button(self, text=rooms[0].name,
                      command=lambda: user_input(self, rooms[0]))
        b = tk.Button(self, text=rooms[1].name,
                      command=lambda: user_input(self, rooms[1]))
        c = tk.Button(self, text=rooms[2].name,
                      command=lambda: user_input(self, rooms[2]))
        d = tk.Button(self, text=rooms[3].name,
                      command=lambda: user_input(self, rooms[3]))
        a.pack(side='left', padx=5, pady=5)
        b.pack(side='left', padx=5, pady=5)
        c.pack(side='left', padx=5, pady=5)
        d.pack(side='left', padx=5, pady=5)

        # add a text widget to display the word "Hello"

        self.dateLabel = tk.Label(self, text="", width=30, font=[('Arial 10')])
        self.dateLabel.pack(side='right')

    def __init_data(self):
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
        self.home.add_room("Sitting Room")
        self.home.add_room("Kitchen")
        self.home.add_room("Dining Room")
        self.home.add_room("Bedroom")

        self.schedule = self.__init_schedule(self.home)

    def __init_schedule(self, home):
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
        schedule.add_breakpoint("06:00", wakeup_breakpoint)

        # "leave for work"
        leave_breakpoint = copy.deepcopy(home)
        leave_breakpoint.set_room("Sitting Room", False, 19)
        leave_breakpoint.set_room("Kitchen", False, 19)
        leave_breakpoint.set_room("Dining Room", False, 19)
        leave_breakpoint.set_room("Bedroom", False, 19)
        schedule.add_breakpoint("08:00", leave_breakpoint)

        # "arrive from work" breakpoint
        arrive_breakpoint = copy.deepcopy(home)
        arrive_breakpoint.set_room("Sitting Room", True, 22)
        arrive_breakpoint.set_room("Kitchen", True, 22)
        arrive_breakpoint.set_room("Dining Room", False, 21)
        arrive_breakpoint.set_room("Bedroom", False, 21)
        schedule.add_breakpoint("17:00", arrive_breakpoint)

        # "late night" breakpoint
        late_breakpoint = copy.deepcopy(home)
        late_breakpoint.set_room("Sitting Room", False, 19)
        late_breakpoint.set_room("Kitchen", False, 22)
        late_breakpoint.set_room("Dining Room", True, 22)
        late_breakpoint.set_room("Bedroom", True, 22)
        schedule.add_breakpoint("20:00", late_breakpoint)

        # "bedtime" breakpoint
        sleep_breakpoint = copy.deepcopy(home)
        sleep_breakpoint.set_room("Sitting Room", False, 19)
        sleep_breakpoint.set_room("Kitchen", False, 19)
        sleep_breakpoint.set_room("Dining Room", False, 21)
        sleep_breakpoint.set_room("Bedroom", False, 21)
        schedule.add_breakpoint("22:00", sleep_breakpoint)

        return schedule

    def __loop(self):
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
        self.__update_vis()

        # update date and time
        self.day += datetime.timedelta(minutes=self.__delta)

        self.after(self.__loop_delta, self.__loop)
        pass

    def __update_vis(self):
        '''
        private

        updates tkinter widgets
        '''

        # update label
        self.dateLabel.config(text=self.day.strftime("%d/%m/%Y %H:%M"))


if __name__ == "__main__":
    core = Core()
    core.run()

from tkinter import *

my_window = Tk()
my_window.title("Canvas")
my_window.geometry("3000x1500")

my_canvas = Canvas(my_window, width=1500, height=1000, bg="white")

def house_plan():
    #walls of house
    my_canvas.create_rectangle(100, 100, 300, 300, width="5")
    my_canvas.create_line(300, 100, 350, 100, width="5")
    my_canvas.create_rectangle(350, 100, 550, 300, width="5")
    my_canvas.create_rectangle(100, 350, 300, 500, width="5")
    my_canvas.create_rectangle(300,350, 550, 500, width="5")
    my_canvas.create_line(550,300, 550, 350, width="5")
    my_canvas.create_rectangle(550,300,480,200, width="5")#bathroom

    #doors
    front_door_coord = 0, 400, 200,300 
    my_canvas.create_arc(front_door_coord, start=90, extent=90, fill="red")

my_canvas.pack() 
house_plan() 
my_window.mainloop()
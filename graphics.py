from tkinter import *
from system import sys_init
from light import * 
from temp import *

SittingRoomLight = light(1) 
sitting_room_heating = heater(2)
sitting_room_ac = airConditioner(3)
sitting_room_thermometer = thermometer(4)

kitchen_light = light(5)

homeObjectList = [SittingRoomLight, sitting_room_heating, sitting_room_ac, sitting_room_thermometer, "Sitting Room"]

def graphics():
    my_window = Tk()
    my_window.title("Canvas")
    my_window.geometry("500x500")

    my_canvas = Canvas(my_window, width=500, height=500, bg="white")
    #sitting room lights
    if SittingRoomLight._state == 1:
        #my_canvas.create_rectangle(x1, y1, x2, y2, fill="color") 
        my_canvas.create_rectangle(100, 100, 300, 300, tag="light", fill="yellow")
    else:
        my_canvas.create_rectangle(100, 100, 300, 300, tag="light", fill="cyan")

    def tempIncrease():
        print("hello")
        sys_init(homeObjectList)
        print("done")
        my_canvas.delete("light")
        if SittingRoomLight._state == 1:
            my_canvas.create_rectangle(100, 100, 300, 300, tag="light", fill="yellow")
        else:
            my_canvas.create_rectangle(100, 100, 300, 300, tag="light", fill="cyan")
        my_canvas.delete("label")
        my_canvas.create_text(200,150, text="Sitting Room", tag="label", fill="black", font=('Helvetica 15 bold'))
        my_canvas.delete("temp")
        my_canvas.create_text(200,220, text=str(sitting_room_thermometer._temp), tag="temp", fill="red", font=('Helvetica 15 bold'))

    b = Button(my_window, text="Input", command=tempIncrease)
    b.pack()

    #sitting room lable
    my_canvas.create_text(200,150, text="Sitting Room", tag="label", fill="black", font=('Helvetica 15 bold'))
    my_canvas.create_text(200,220, text=str(sitting_room_thermometer._temp), tags="temp", fill="red", font=('Helvetica 15 bold'))
    my_canvas.pack()   
    my_window.mainloop()

graphics()
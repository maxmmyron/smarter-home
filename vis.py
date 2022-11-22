from tkinter import *
from u_input import sys_init
from home import * 
from core import loop

def graphics(home):
    my_window = Tk()
    my_window.title("Canvas")
    my_window.geometry("500x500")

    my_canvas = Canvas(my_window, width=500, height=500, bg="white")
    #sitting room lights
    if home.rooms[0].light == 1:
        #my_canvas.create_rectangle(x1, y1, x2, y2, fill="color") 
        my_canvas.create_rectangle(100, 100, 300, 300, tag="light", fill="yellow")
    else:
        my_canvas.create_rectangle(100, 100, 300, 300, tag="light", fill="cyan")

    def kitchenInput():
        sys_init(home.rooms[0])
        my_canvas.delete("light")
        if home.rooms[0].light == 1:
            my_canvas.create_rectangle(100, 100, 300, 300, tag="light", fill="yellow")
        else:
            my_canvas.create_rectangle(100, 100, 300, 300, tag="light", fill="cyan")
        my_canvas.delete("label")
        my_canvas.create_text(200,150, text=home.rooms[0].name, tag="label", fill="black", font=('Helvetica 15 bold'))
        my_canvas.delete("temp")
        my_canvas.create_text(200,220, text=str(home.rooms[0].temperature), tag="temp", fill="red", font=('Helvetica 15 bold'))

    b = Button(my_window, text="Kitchen", command=kitchenInput)
    b.pack()

    #sitting room lable
    my_canvas.create_text(200,150, text=home.rooms[0].name, tag="label", fill="black", font=('Helvetica 15 bold'))
    my_canvas.create_text(200,220, text=str(home.rooms[0].temperature), tags="temp", fill="red", font=('Helvetica 15 bold'))
    my_canvas.pack()   
    my_window.mainloop()
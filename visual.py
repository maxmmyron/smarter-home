from tkinter import *
from user_input import sys_init
from home import * 

home = Home("home")

# add rooms to home
home.add_room("Kitchen")
home.add_room("Lounge")
home.add_room("BedroomA")
home.add_room("BedroomB")


def graphics(home):
    print("-------------------------------------------------------")
    print(" Welcome to the America Moth Smart Home control System")
    print("-------------------------------------------------------")
    rooms = home.rooms
    my_window = Tk()
    my_window.title("Canvas")
    my_window.geometry("800x800")

    my_canvas = Canvas(my_window, width=500, height=500, bg="white")

    my_canvas.create_rectangle(50, 50, 250, 250, tags=rooms[0].name, fill="cyan")
    rooms[0].x = 50
    rooms[0].y = 50
    my_canvas.create_text(150,100, text=rooms[0].name, tags=rooms[0].name + "label", fill="black", font=('Helvetica 15 bold'))
    my_canvas.create_text(150,170, text=str(rooms[0].temperature), tags=rooms[0].name + "temp", fill="red", font=('Helvetica 15 bold'))
 
    my_canvas.create_rectangle(250, 50, 450, 250, tags=rooms[1].name, fill="cyan")
    rooms[1].x = 250
    rooms[1].y = 50
    my_canvas.create_text(350,100, text=rooms[1].name, tags=rooms[1].name + "label", fill="black", font=('Helvetica 15 bold'))
    my_canvas.create_text(350,170, text=str(rooms[1].temperature), tags=rooms[1].name + "temp", fill="red", font=('Helvetica 15 bold'))


    my_canvas.create_rectangle(50, 250, 250, 450, tags=rooms[2].name, fill="cyan")
    rooms[2].x = 50
    rooms[2].y = 250
    my_canvas.create_text(150,300, text=rooms[2].name, tags=rooms[2].name + "label", fill="black", font=('Helvetica 15 bold'))
    my_canvas.create_text(150,370, text=str(rooms[2].temperature), tags=rooms[2].name + "temp", fill="red", font=('Helvetica 15 bold'))

    my_canvas.create_rectangle(250, 250, 450, 450, tags=rooms[3].name, fill="cyan")
    rooms[3].x = 250
    rooms[3].y = 250
    my_canvas.create_text(350,300, text=rooms[3].name, tags=rooms[3].name + "label", fill="black", font=('Helvetica 15 bold'))
    my_canvas.create_text(350,370, text=str(rooms[3].temperature), tags=rooms[3].name + "temp", fill="red", font=('Helvetica 15 bold'))


    def input(room):

        sys_init(room)
        my_canvas.delete(room.name)
        if room.light == 1:
            my_canvas.create_rectangle(room.x, room.y, room.x + 200, room.y + 200, tags=room.name, fill="yellow")
        else:
            my_canvas.create_rectangle(room.x, room.y, room.x + 200, room.y + 200, tags=room.name, fill="cyan")
        tempX = room.x + 100
        tempY = room.y + 50
        my_canvas.delete(room.name + "label")
        my_canvas.create_text(tempX, tempY, text=room.name, tags=room.name + "label", fill="black", font=('Helvetica 15 bold'))
        my_canvas.delete(room.name + "temp")
        my_canvas.create_text(tempX, tempY + 70, text=str(room.temperature), tags=room.name +"temp", fill="red", font=('Helvetica 15 bold'))

    a = Button(my_window, text=rooms[0].name, command=lambda: input(rooms[0]))
    b = Button(my_window, text=rooms[1].name, command=lambda: input(rooms[1]))
    c = Button(my_window, text=rooms[2].name, command=lambda: input(rooms[2]))
    d = Button(my_window, text=rooms[3].name, command=lambda: input(rooms[3]))
    a.pack()
    b.pack()
    c.pack()
    d.pack()

    my_canvas.pack()   
    my_window.mainloop()

graphics(home)
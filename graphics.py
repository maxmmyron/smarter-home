from tkinter import *

lights = 1
temperature = 30
sitting_room_heating = 0
sitting_room_ac = 0

my_window = Tk()
my_window.title("Canvas")
my_window.geometry("500x500")


my_canvas = Canvas(my_window, width=500, height=500, bg="white")
my_canvas.pack(pady=50)

#sitting room lights
if lights == 1:
    #my_canvas.create_rectangle(x1, y1, x2, y2, fill="color") 
    my_canvas.create_rectangle(100, 100, 300, 300, fill="yellow")
else:
    my_canvas.create_rectangle(100, 100, 300, 300, fill="cyan")

#sitting room lable
my_canvas.create_text(200,150, text="Sitting Room", fill="black", font=('Helvetica 15 bold'))
if sitting_room_ac == 1 and sitting_room_heating == 1:
    my_canvas.create_text(200,220, text=str(temperature)+" Degrees \nWarning A/C \n+ Heating are\non", fill="Purple", font=('Helvetica 15 bold'))
elif sitting_room_ac == 1 and sitting_room_heating == 0:
    my_canvas.create_text(200,220, text=str(temperature)+" Degrees", fill="blue", font=('Helvetica 15 bold'))
elif sitting_room_ac == 0 and sitting_room_heating == 1:
    my_canvas.create_text(200,220, text=str(temperature)+" Degrees", fill="red", font=('Helvetica 15 bold'))
else:
    my_canvas.create_text(200,220, text=str(temperature)+" Degrees", fill="black", font=('Helvetica 15 bold'))


my_window.mainloop()
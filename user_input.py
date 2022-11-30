import copy
import tkinter as tk


def construct_user_state(tk_root, initial_state):
    state = copy.deepcopy(initial_state)

    # init popup window
    popup = tk.Toplevel(tk_root)
    popup.title("User Input")
    popup.geometry("600x500")

    # construct widgets

    for room in state.rooms:
        room_button = tk.Button(popup, text=room.name,
                                command=lambda: _construct_user_room_state(popup, room))
        room_button.pack()

    finish_button = tk.Button(popup, text="Finish", command=popup.destroy)
    finish_button.pack()

    # returns state after mainloop finishes (on popup destroy)
    return state


def _construct_user_room_state(tk_root, room):
    temp = room.temperature
    light = room.light

    popup = tk.Toplevel(tk_root)
    popup.title("Set " + room.name + " State")
    popup.geometry("600x500")

    # construct widgets
    left_frame = tk.Frame(popup)
    left_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=20, pady=20)

    right_frame = tk.Frame(popup)
    right_frame.pack(side=tk.RIGHT, fill="both", expand=True, padx=20, pady=20)

    tk.Label(left_frame, text="Temperature").pack()

    tk.Button(
        left_frame, text="+", command=lambda: set_temp(1)).pack()

    tk.Button(
        left_frame, text="-", command=lambda: set_temp(-1)).pack()

    tk.Label(
        left_frame, text="Current Temp: " + str(room.temperature)).pack()

    temperature_target_label = tk.Label(
        left_frame, text="Target Temp: " + str(temp))
    temperature_target_label.pack()

    def set_temp(flip):
        nonlocal temp
        temp = float("{:.2f}".format(temp + flip*room.temp_step))
        temperature_target_label.config(text="Target Temp: " + str(temp))

    tk.Label(right_frame, text="Light").pack()

    tk.Button(
        right_frame, text="On", command=lambda: set_light(True)).pack()

    tk.Button(
        right_frame, text="Off", command=lambda: set_light(False)).pack()

    tk.Label(
        right_frame, text="Current Light: " + str(room.light)).pack()

    light_target_label = tk.Label(
        right_frame, text="Target Light: " + str(light))
    light_target_label.pack()

    def set_light(b):
        nonlocal light
        light = b
        light_target_label.config(text="Target Light: " + str(light))

    def on_destroy():
        room.temperature = temp
        room.light = light
        popup.destroy()

    finish_button = tk.Button(popup, text="Finish", command=on_destroy)
    finish_button.pack()

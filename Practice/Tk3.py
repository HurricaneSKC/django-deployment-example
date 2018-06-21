from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# styling widgets

def open_msg_box():
    messagebox.showwarning(
        "Event Triggered"
        "Button Clicked"
    )


root = Tk()

# set size of window width+height+xoffset+yoffset
root.geometry("400x400+300+300")

# is it resizeable .... in this case no
root.resizable(width=False, height=False)

# simple frame to house widgets
frame = Frame(root)

# styling options using ttk
style = ttk.Style()

# style the button ...
style.configure("TButton",
                foreground="midnight blue",
                font="Time 20 bold italic",
                padding=20)

# print style themes
print(ttk.Style().theme_names())


print(style.lookup("TButton", "font"))
print(style.lookup("TButton", "foreground"))
print(style.lookup("TButton", "padding"))

ttk.Style().theme_use('classic')

# create button - tied to frame
theButton = ttk.Button(frame,
                       text="Important Button",
                       command=open_msg_box)

theButton['state'] = 'disabled'
theButton['state'] = 'normal'

theButton.pack()

frame.pack()

root.mainloop()
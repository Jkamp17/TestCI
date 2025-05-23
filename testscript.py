# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to Test GUI")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding a label to the root window
lbl = Label(root, text = "Test script")
lbl.grid()

# function to display text when
# button is clicked
def clicked():
    lbl.configure(text = "Click Confirmed")

# button widget with red color text
# inside
btn = Button(root, text = "Button" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)

# Execute Tkinter
root.mainloop()

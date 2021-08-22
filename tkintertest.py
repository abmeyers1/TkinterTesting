from tkinter import *

# First create Root widget. Window for use
root = Tk()

# to create things in kinter, two steps:
# 1) Create it
myLabel = Label(root, text='Hello, World!')
# 2) put it on screen, "pack it" on screen, unsophisticated & simple method
myLabel.pack()


# Create event Loop:
# when running a program, it's always looping. when mouse move,input,key input, notices difference in loop
root.mainloop()


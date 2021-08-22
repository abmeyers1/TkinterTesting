from tkinter import *

# First create Root widget. Window for use
root = Tk()

# to create things in kinter, two steps:
# 1) Create it
myLabel1 = Label(root, text='Hello, World!')
myLabel2 = Label(root, text='I\'m Alex M.')
myLabel3 = Label(root, text='Welcome to my thing')
space = Label(root, text= ' m ')
# 2) put it on screen, Use .grid(row=?, column=?) to structure placement
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=1, column=16)

# OR! For expedicency, can grid a label when creating:
myLabel4 = Label(root, text='...wow I think this one might work...').grid(row=2,column=1)


# Create event Loop:
# when running a program, it's always looping. when mouse move,input,key input, notices difference in loop
root.mainloop()


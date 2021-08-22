from tkinter import *
import random

# First create Root widget. Window for use
root = Tk()
colors =['red','blue','green','yellow']
# Make a function for the button:
def click():
    color = random.choice(colors)
    back = str(random.randint(0,999999))
    while len(back) < 6:
        back = '0'+ back
    backcolor = '#'+ back
    myLabel = Label(root, text='look, you\'ve done it I\'m very proud of you', fg=color, bg=backcolor)
    myLabel.pack()

#Creating a button:
# (location, what text?, state = Disabled to grey out)
# Padx = make button wider, Pady = make taller. Text remains center
#command = name of function to execute. Don't add () in this, or it'll call when creating
# fg = 'color' to change text color, can use hexcodes if you want
# bf = 'color' to change backcolor
myButton = Button(root, text='Click this button!', command=click, fg='red', bg='yellow')
myButton.pack()



# Create event Loop:
# when running a program, it's always looping. when mouse move,input,key input, notices difference in loop
root.mainloop()

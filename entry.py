from tkinter import *
import random

# First create Root widget. Window for use
root = Tk()

# Create Entry widget:
# Width, fg/bg
# borderwidth
e = Entry(root, width=50, bg='black', fg='yellow', borderwidth=10)
e.pack()

# insert to save default text
e.insert(0, 'enter your name please')

# How to get info from your entry:
e.get()





# Make a function for the button:
colors =['red','blue','green','yellow']
def click():
    color = random.choice(colors)
    back = str(random.randint(0,999999))
    while len(back) < 6:
        back = '0'+ back
    backcolor = '#'+ back
    myLabel = Label(root, text="Hello " + e.get(), fg=color, bg=backcolor)
    myLabel.pack()

#Creating a button:
# (location, what text?, state = Disabled to grey out)
# Padx = make button wider, Pady = make taller. Text remains center
#command = name of function to execute. Don't add () in this, or it'll call when creating
# fg = 'color' to change text color, can use hexcodes if you want
# bf = 'color' to change backcolor
myButton = Button(root, text='Enter your name!', command=click, fg='red', bg='yellow')
myButton.pack()



# Create event Loop:
# when running a program, it's always looping. when mouse move,input,key input, notices difference in loop
root.mainloop()

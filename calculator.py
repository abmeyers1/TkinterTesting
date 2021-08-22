from tkinter import *

root = Tk()
root.title('Simple Calculator"')

e = Entry(root, width=35, borderwidth=5)
# Columnspan: how many cols wide
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



# functions for buttons:
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_add():
    first_number = e.get()
    # Create global number to be used outside of function
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0,END)

def button_subtract():
    first_number = e.get()
    # Create global number to be used outside of function
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)

def button_mult():
    first_number = e.get()
    # Create global number to be used outside of function
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    # Create global number to be used outside of function
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)

def button_equals():
    # Saves current entered value
    second_number = e.get()
    # Clears screen
    e.delete(0,END)
    # Checks current Math status, updates result
    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    if math == 'division':
        e.insert(0, f_num / int(second_number))

def button_clear():
    e.delete(0, END)

# Define  buttons
clickcolor = "light blue"
button_1 = Button(root,text='1', padx=40, pady=20, activebackground =clickcolor, command=lambda: button_click(1))
button_2 = Button(root,text='2', padx=40, pady=20,activebackground =clickcolor, command=lambda: button_click(2))
button_3 = Button(root,text='3', padx=40, pady=20, activebackground =clickcolor,command=lambda: button_click(3))
button_4 = Button(root,text='4', padx=40, pady=20,activebackground =clickcolor, command=lambda: button_click(4))
button_5 = Button(root,text='5', padx=40, pady=20, activebackground =clickcolor,command=lambda: button_click(5))
button_6 = Button(root,text='6', padx=40, pady=20, activebackground =clickcolor,command=lambda: button_click(6))
button_7 = Button(root,text='7', padx=40, pady=20, activebackground =clickcolor,command=lambda: button_click(7))
button_8 = Button(root,text='8', padx=40, pady=20, activebackground =clickcolor,command=lambda: button_click(8))
button_9 = Button(root,text='9', padx=40, pady=20, activebackground =clickcolor,command=lambda: button_click(9))
button_0 = Button(root,text='0', padx=40, pady=20, activebackground =clickcolor,command=lambda: button_click(0))

button_plus= Button(root,text='+', padx=39, pady=20, command=button_add)
button_minus = Button(root,text='-', padx=40, pady=20, command=button_subtract)
button_times = Button(root,text='*', padx=39, pady=20, command=button_mult)
button_div = Button(root,text='/', padx=41, pady=20, command=button_div)

button_equal= Button(root,text='=', padx=87, pady=20, command= button_equals)
button_clear = Button(root,text='Clear', padx=77, pady=20, command=button_clear)


# Put number buttons on grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2 , column=1)
button_6.grid(row=2 , column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

# Put functions on grid
button_clear.grid(row=4,column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_equal.grid(row=5,column=1, columnspan=2)

button_minus.grid(row=6, column=0)
button_times.grid(row=6, column=1)
button_div.grid(row=6, column=2)


root.mainloop()
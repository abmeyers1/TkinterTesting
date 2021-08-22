from tkinter import *

root =Tk()
root.title('here\'s the next part...')
# Adding icons: using ICO files, 16x16, 32x32 etc files
root.iconbitmap("c:/testicon.ico")

button_quit = Button(root, text='Exit program', command=root.quit())
button_quit.pack()


print('ok?')









root.mainloop()
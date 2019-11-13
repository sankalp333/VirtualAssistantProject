from Tkinter import *

root = Tk()

def new_winF() : # New Window Definition
	newwin = Toplevel(root)
	display = Label(newwin,text="Humm, see a new window!")
	display.pack()

button1 = Button(root, text = "Open a new window", command = new_winF)  # Command Linked
button1.pack()

root.mainloop()

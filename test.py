from tkinter import *

root = Tk()

def comand():
	print('Hello')

def comand2():
	but1.invoke()

but1 = Button(root, command=comand)
but1.pack()

but2 = Button(root, command=comand2)
but2.pack()
root.mainloop()
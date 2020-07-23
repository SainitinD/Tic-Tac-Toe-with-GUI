import tkinter as tk
from PIL import ImageTk, Image


class TicTacToe(tk.Tk()):

	BUTTON_H = 100
	BUTTON_W = 100

	BUTTON_BG = '#4E4540'
	BUTTON_ACTIVE_BG = '#403834'

	null_img = Image.open('null.png')
	null_img = ImageTk.PhotoImage(null_img.resize((100,100), Image.ANTIALIAS))

	X_img = Image.open('X2.png')
	X_icon = ImageTk.PhotoImage(X_img.resize((15, 12), Image.ANTIALIAS))
	X_img = ImageTk.PhotoImage(X_img.resize((100, 80), Image.ANTIALIAS))

	O_img = Image.open('O2.png')
	O_icon = ImageTk.PhotoImage(O_img.resize((14, 14), Image.ANTIALIAS))
	O_img = ImageTk.PhotoImage(O_img.resize((90, 90), Image.ANTIALIAS))

	def __init__(self, *args, **kwargs):
		tk.Tk().__init__(self, *args, **kwargs)
		self.title('Tic Tac Toe')
		self.configure(bg='#4E4540')

		self.button1 = tk.Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button1, 1))
		self.button2 = tk.Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button2, 2))
		self.button3 = tk.Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button3, 3))

		self.button4 = tk.Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button4, 4))
		self.button5 = tk.Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button5, 5))
		self.button6 = tk.Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button6, 6))

		self.button7 = tk.Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button7, 7))
		self.button8 = tk.Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button8, 8))
		self.button9 = tk.Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button9, 9))

	def place_buttons(self):
		self.button1.grid(row=1,column=0)
		self.button2.grid(row=1,column=1)
		self.button3.grid(row=1,column=2)

		self.button4.grid(row=2,column=0)
		self.button5.grid(row=2,column=1)
		self.button6.grid(row=2,column=2)

		self.button7.grid(row=3,column=0)
		self.button8.grid(row=3,column=1)
		self.button9.grid(row=3,column=2)


tictactoe = TicTacToe()
tictactoe.mainloop()



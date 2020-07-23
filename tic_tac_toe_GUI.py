from tkinter import *
from PIL import ImageTk, Image
#


root = Tk()
root.title('Tic Tac Toe')
root.configure(bg='#4E4540')

BUTTON_H = 100
BUTTON_W = 100

BUTTON_BG = '#4E4540'
BUTTON_ACTIVE_BG = '#403834'

null_img = Image.open('null.png')
null_img = ImageTk.PhotoImage(null_img.resize((100,100), Image.ANTIALIAS))

X_img = Image.open('X2.png')
X_img = ImageTk.PhotoImage(X_img.resize((100, 80), Image.ANTIALIAS))

O_img = Image.open('O2.png')
O_img = ImageTk.PhotoImage(O_img.resize((90, 90), Image.ANTIALIAS))

# Global list to hold values of the tic-tac-toe board. Each three positions represent a row on the board
board = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']

# A counter to keep track of turns
turn = 0

# A list of booleans to keep track of button pressed
isClicked_List = [False, False, False, False, False, False, False, False, False]

def button_clicked(button, button_idx):
	''' Function to change images on buttons when clicked '''
	global turn
	if turn % 2 == 0:
		if isClicked_List[button_idx-1] == False:
			button.config(image=X_img)
			turn += 1
			isClicked_List[button_idx-1] = True
			print(turn)
	else:
		if isClicked_List[button_idx-1] == False:
			print(button.cget('image') == str(null_img))
			button.config(image=O_img)
			turn += 1
			isClicked_List[button_idx-1] = True
			print(button.cget('image') == str(null_img))

#Create my tic-tac-toe gui grid
'''

[1 2 3]
[4 5 6]
[7 8 9]

'''

# Creating the buttons for the board
Player1_Label = Label(root, text='Player 1: X')
Player2_Label = Label(root, text='Player 2: O')

button1 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button1, 1))
button2 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button2, 2))
button3 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button3, 3))

button4 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button4, 4))
button5 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button5, 5))
button6 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button6, 6))

button7 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button7, 7))
button8 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button8, 8))
button9 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button9, 9))


# Place the buttons on the board
Player1_Label.grid(row=0, column=0, ipadx=23)
Player2_Label.grid(row=0, column=1, ipadx=23)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

root.mainloop()









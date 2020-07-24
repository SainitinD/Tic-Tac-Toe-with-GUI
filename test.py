from tkinter import *
from PIL import ImageTk, Image


root = Tk()
BUTTON_H = 100
BUTTON_W = 100
BUTTON_BG = '#4E4540'
BUTTON_ACTIVE_BG = '#403834'

# Import an empty image
null_img = Image.open('assests/null.png')
null_img = ImageTk.PhotoImage(null_img.resize((100,100), Image.ANTIALIAS))

# Import image and icon for X
X_img = Image.open('assests/X2.png')
X_icon = ImageTk.PhotoImage(X_img.resize((15, 12), Image.ANTIALIAS))
X_img = ImageTk.PhotoImage(X_img.resize((95, 80), Image.ANTIALIAS))

# Import horizontally striked X
X_hor = Image.open('assests/X2_hor.png')
X_hor = ImageTk.PhotoImage(X_hor.resize((95, 80), Image.ANTIALIAS))

# Import vertically striked X
X_vert = Image.open('assests/X2_vert.png')
X_vert = ImageTk.PhotoImage(X_vert.resize((95, 80), Image.ANTIALIAS))

# Import diagonally strikedX
X_diag = Image.open('assests/X2_diag.png')
X_diag = ImageTk.PhotoImage(X_diag.resize((95, 80), Image.ANTIALIAS))

# Import another diagonally striked X
X_diag2 = Image.open('assests/X2_diag2.png')
X_diag2 = ImageTk.PhotoImage(X_diag2.resize((95, 80), Image.ANTIALIAS))

# Import image and icon for O
O_img = Image.open('assests/O2.png')
O_icon = ImageTk.PhotoImage(O_img.resize((14, 14), Image.ANTIALIAS))
O_img = ImageTk.PhotoImage(O_img.resize((90, 90), Image.ANTIALIAS))

# Import horizontally striked O
O_hor = Image.open('assests/O2_hor2.png')
O_hor = ImageTk.PhotoImage(O_hor.resize((90, 90), Image.ANTIALIAS))

# Import vertically striked O
O_vert = Image.open('assests/O2_vert2.png')
O_vert = ImageTk.PhotoImage(O_vert.resize((90, 90), Image.ANTIALIAS))

# Import diagonally striked O
O_diag = Image.open('assests/O2_diag.png')
O_diag = ImageTk.PhotoImage(O_diag.resize((90, 90), Image.ANTIALIAS))

# Import another diagonally striked O
O_diag2 = Image.open('assests/O2_diag2.png')
O_diag2 = ImageTk.PhotoImage(O_diag2.resize((90, 90), Image.ANTIALIAS))


top_frame = Frame(root, relief='groove')
top_frame.grid(row=0, pady=5)

Score_Label = Label(top_frame, bg=BUTTON_BG, text='( 0 - 0 )', foreground='#FFFFFF')
Player1_Label = Button(top_frame, bg=BUTTON_BG, image=X_icon, activebackground=BUTTON_BG, relief='flat')
Player2_Label = Button(top_frame, bg=BUTTON_BG, image=O_icon, activebackground=BUTTON_BG, relief='flat')

Score_Label.grid(row=0,column=1, ipadx=32)
Player1_Label.grid(row=0, column=0, ipadx=23, pady=1)
Player2_Label.grid(row=0, column=2, ipadx=23, pady=1)

root.mainloop()



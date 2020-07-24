from tkinter import *
from PIL import ImageTk, Image
import random
import time

root = Tk()
root.title('Tic Tac Toe')
root.configure(bg='#4E4540')

# Global list to hold values of the tic-tac-toe board. Each three positions represent a row on the board
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# A counter to keep track of turns
turn = 0

# A counter to keep track of player's scores
x_score = 0
o_score = 0

# A variable to keep track of player mode. (1 = Player vs Player, 2 = Player vs CPU)
player_mode = 2

# Set all button's inner properties
BUTTON_H = 100
BUTTON_W = 100
BUTTON_BG = '#4E4540'
BUTTON_ACTIVE_BG = '#403834'

# Import an empty image
null_img = Image.open('assests/null/null.png')
null_img = ImageTk.PhotoImage(null_img.resize((100,100), Image.ANTIALIAS))

# Import image and icon for X
X_img = Image.open('assests/X_Assets/X2.png')
X_icon = ImageTk.PhotoImage(X_img.resize((15, 12), Image.ANTIALIAS))
X_img = ImageTk.PhotoImage(X_img.resize((95, 80), Image.ANTIALIAS))

# Import horizontally striked X
X_hor = Image.open('assests/X_Assets/X2_hor.png')
X_hor = ImageTk.PhotoImage(X_hor.resize((95, 80), Image.ANTIALIAS))

# Import vertically striked X
X_vert = Image.open('assests/X_Assets/X2_vert.png')
X_vert = ImageTk.PhotoImage(X_vert.resize((95, 80), Image.ANTIALIAS))

# Import diagonally strikedX
X_diag = Image.open('assests/X_Assets/X2_diag.png')
X_diag = ImageTk.PhotoImage(X_diag.resize((95, 80), Image.ANTIALIAS))

# Import another diagonally striked X
X_diag2 = Image.open('assests/X_Assets/X2_diag2.png')
X_diag2 = ImageTk.PhotoImage(X_diag2.resize((95, 80), Image.ANTIALIAS))

# Import image and icon for O
O_img = Image.open('assests/O_Assets/O2.png')
O_icon = ImageTk.PhotoImage(O_img.resize((14, 14), Image.ANTIALIAS))
O_img = ImageTk.PhotoImage(O_img.resize((90, 90), Image.ANTIALIAS))

# Import horizontally striked O
O_hor = Image.open('assests/O_Assets/O2_hor2.png')
O_hor = ImageTk.PhotoImage(O_hor.resize((90, 90), Image.ANTIALIAS))

# Import vertically striked O
O_vert = Image.open('assests/O_Assets/O2_vert2.png')
O_vert = ImageTk.PhotoImage(O_vert.resize((90, 90), Image.ANTIALIAS))

# Import diagonally striked O
O_diag = Image.open('assests/O_Assets/O2_diag.png')
O_diag = ImageTk.PhotoImage(O_diag.resize((90, 90), Image.ANTIALIAS))

# Import another diagonally striked O
O_diag2 = Image.open('assests/O_Assets/O2_diag2.png')
O_diag2 = ImageTk.PhotoImage(O_diag2.resize((90, 90), Image.ANTIALIAS))


def player_highlight():
    """
    Responsible for highlighting the label for the player with their turn
    """

    global turn
    if turn % 2 == 0:
        Player2_Label.configure(relief='flat')
        Player1_Label.configure(relief='groove')
    else:
        Player1_Label.configure(relief='flat')
        Player2_Label.configure(relief='groove')


def button_clicked(button, button_idx):
    """
    Function to change images on buttons when clicked
    """
    cache = 0
    global turn
    global player_mode

    if turn % 2 == 0:
        if board[button_idx-1] == 0:
            button.config(image=X_img)
            board[button_idx-1] = 1
            turn += 1
            player_highlight()
            if player_mode == 2:
                pc_play()
    else:
        if player_mode == 1:
            if board[button_idx-1] == 0:
                button.config(image=O_img)
                board[button_idx-1] = 2
                turn += 1
    checkgame()
    player_highlight()

def pc_play():
    """
    Function that chooses random spots to place O for pc 
    """
    global turn
    while True:
        # If all spots on board are filled up then get out of this loop

        if turn >= 9:
            break

        # choose a random position and if that position on board is empty, then place a 'O' there.
        i = random.randint(0, 8)
        if board[i] == 0:
            #root.after(400)
            button_list[i].config(image=O_img)
            board[i] = 2
            turn += 1

            break
    
def check_board(player):
    """ Checks if X or O won in any way.

    The function checks horizontally, vertically and diagnoally.
    For a certain row,column or diagnal it returns True if that slice has no empty values and no opposite sign.  

    Parameters
    ----------
    player (int): indicates the player. (1 for "X" and 2 for "O")

    Returns
    -------
    bool:
        (True/False) if the inputed player has won. 
    """
    if player == 1:
        sign = 2
        # Checks if X won horizontally
        if sign not in board[0:3] and 0 not in board[0:3]:
            set_sprites_over(1, 123)
            return True
        if sign not in board[3:6] and 0 not in board[3:6]:
            set_sprites_over(1, 456)
            return True
        if sign not in board[6:9] and 0 not in board[6:9]:
            set_sprites_over(1, 789)
            return True

        # Checks if X won vertically
        if sign not in board[0:7:3] and 0 not in board[0:7:3]:
            set_sprites_over(1, 147)
            return True
        if sign not in board[1:8:3] and 0 not in board[1:8:3]:
            set_sprites_over(1, 258)
            return True
        if sign not in board[2:9:3] and 0 not in board[2:9:3]:
            set_sprites_over(1, 369)
            return True

        # Checks if X won diagonally
        if sign not in board[0:9:4] and 0 not in board[0:9:4]:
            set_sprites_over(1, 159)
            return True
        if sign not in board[2:7:2] and 0 not in board[2:7:2]:
            set_sprites_over(1, 357)
            return True

        # Return False if X is not winning
        return False
    else:
        sign = 1

        # Checks if O won horizontally
        if sign not in board[0:3] and 0 not in board[0:3]:
            set_sprites_over(2, 123)
            return True
        if sign not in board[3:6] and 0 not in board[3:6]:
            set_sprites_over(2, 456)
            return True
        if sign not in board[6:9] and 0 not in board[6:9]:
            set_sprites_over(2, 789)
            return True

        # Checks if O won vertically
        if sign not in board[0:7:3] and 0 not in board[0:7:3]:
            set_sprites_over(2, 147)
            return True
        if sign not in board[1:8:3] and 0 not in board[1:8:3]:
            set_sprites_over(2, 258)
            return True
        if sign not in board[2:9:3] and 0 not in board[2:9:3]:
            set_sprites_over(2, 369)
            return True

        # Checks if O won diagonally
        if sign not in board[0:9:4] and 0 not in board[0:9:4]:
            set_sprites_over(2, 159)
            return True
        if sign not in board[2:7:2] and 0 not in board[2:7:2]:
            set_sprites_over(2, 357)
            return True

        # Return False if O is not winning
        return False

def set_sprites_over(player, orientation):
    if player == 1:
        if orientation == 123:
            button1.config(image=X_hor)
            button2.config(image=X_hor)
            button3.config(image=X_hor)
        elif orientation == 456:
            button4.config(image=X_hor)
            button5.config(image=X_hor)
            button6.config(image=X_hor)
        elif orientation == 789:
            button7.config(image=X_hor)
            button8.config(image=X_hor)
            button9.config(image=X_hor)
        elif orientation == 147:
            button1.config(image=X_vert)
            button4.config(image=X_vert)
            button7.config(image=X_vert)
        elif orientation == 258:
            button2.config(image=X_vert)
            button5.config(image=X_vert)
            button8.config(image=X_vert)
        elif orientation == 369:
            button3.config(image=X_vert)
            button6.config(image=X_vert)
            button9.config(image=X_vert)
        elif orientation == 159:
            button1.config(image=X_diag)
            button5.config(image=X_diag)
            button9.config(image=X_diag)
        elif orientation == 357:
            button3.config(image=X_diag2)
            button5.config(image=X_diag2)
            button7.config(image=X_diag2)
    else:
        if orientation == 123:
            button1.config(image=O_hor)
            button2.config(image=O_hor)
            button3.config(image=O_hor)
        elif orientation == 456:
            button4.config(image=O_hor)
            button5.config(image=O_hor)
            button6.config(image=O_hor)
        elif orientation == 789:
            button7.config(image=O_hor)
            button8.config(image=O_hor)
            button9.config(image=O_hor)
        elif orientation == 147:
            button1.config(image=O_vert)
            button4.config(image=O_vert)
            button7.config(image=O_vert)
        elif orientation == 258:
            button2.config(image=O_vert)
            button5.config(image=O_vert)
            button8.config(image=O_vert)
        elif orientation == 369:
            button3.config(image=O_vert)
            button6.config(image=O_vert)
            button9.config(image=O_vert)
        elif orientation == 159:
            button1.config(image=O_diag)
            button5.config(image=O_diag)
            button9.config(image=O_diag)
        elif orientation == 357:
            button3.config(image=O_diag2)
            button5.config(image=O_diag2)
            button7.config(image=O_diag2)




def checkgame():
    """
    Called every time a move is placed. Checks if either X or O won in any way. 
    """
    global turn
    global x_score
    global o_score
    if turn > 4:
        is_game_over_x = check_board(1)
        if is_game_over_x is True:
            x_score += 1
            Score_Label.configure(text='YOU WON', foreground='#32CD32')
            Score_Label.grid(row=0,column=1, ipadx=12)
            button_disabled()

        # Check if PC has won
    if turn > 5:
        is_game_over_o = check_board(2)
        if is_game_over_o is True:
            o_score += 1
            Score_Label.configure(text='YOU LOST', foreground='#DC143C')
            Score_Label.grid(row=0,column=1, ipadx=12)
            button_disabled()

        # Prints out tie if all the positions on board are filled and player1 and player2 haven't won.
        # As total positions on board are 9, when turn is 9 and no one won the game, end the game and print 'tie'
        if turn >= 9:
            is_game_over_x = check_board(1)
            is_game_over_o = check_board(2)
            if is_game_over_x:
                Score_Label.configure(text='YOU WON', foreground='#32CD32')
                Score_Label.grid(row=0,column=1, ipadx=12)
                button_disabled()
            elif is_game_over_o:
                Score_Label.configure(text='YOU LOST', foreground='#DC143C')
                Score_Label.grid(row=0,column=1, ipadx=12)
                button_disabled()
            else:
                Score_Label.configure(text='YOU TIED', foreground='#FFFF99')
                Score_Label.grid(row=0,column=1, ipadx=12)
                button_disabled()


def reset_board():
    """
    Restarts the game by resetting the board, turns, and buttons. Sets the score if any.  
    """
    global board
    global turn
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 0

    button1.configure(image=null_img)
    button2.configure(image=null_img)
    button3.configure(image=null_img)

    button4.configure(image=null_img)
    button5.configure(image=null_img)
    button6.configure(image=null_img)

    button7.configure(image=null_img)
    button8.configure(image=null_img)
    button9.configure(image=null_img)

    Score_Label.configure(text='( 0 - 0 )', foreground='#FFFFFF')
    Score_Label.grid(row=0,column=1, ipadx=32)

    player_highlight()
    button_normal()
    update_score()

def update_score():
    """ Used when retry is clicked. Updates the score. """
    score_text = '( ' + str(x_score) + ' - ' + str(o_score) + ' )'
    Score_Label.configure(text=score_text)

def button_disabled():
    """
    Sets the state of buttons in the game to disabled
    """
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def button_normal():
    """
    Sets the state of buttons in the game to normal
    """
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)


def change_player_mode():
    """ 
    Changes player mode when the player mode button is clicked.
    When Player mode is changed, it resets the text on button and sets both x and o score to 0.
    """
    global player_mode

    # Checks if player mode is 'Player vs Player'
    if player_mode == 1:
        p_mode.configure(text='Player vs CPU')
        player_mode = 2
        reset_score()
        reset_board()

    else:
        p_mode.configure(text='Player vs Player')
        player_mode = 1
        reset_score()
        reset_board()


def reset_score():
    """
    Resets the score for players. Intended to be called whenever the changes the game_mode
    """
    global x_score
    global o_score
    x_score = 0
    o_score = 0


# Creating the labels for player1,player2 and Score
Score_Label = Label(root, bg=BUTTON_BG, text='( 0 - 0 )', foreground='#FFFFFF')
Player1_Label = Button(root, bg=BUTTON_BG, image=X_icon, activebackground=BUTTON_BG, relief='flat')
Player2_Label = Button(root, bg=BUTTON_BG, image=O_icon, activebackground=BUTTON_BG, relief='flat')

'''
Create the buttons for the tic-tac-toe gui grid.
Below is the layout of the named buttons. 

[1 2 3]
[4 5 6]
[7 8 9]

'''
button1 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button1, 1))
button2 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button2, 2))
button3 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button3, 3))

button4 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button4, 4))
button5 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button5, 5))
button6 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button6, 6))

button7 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button7, 7))
button8 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button8, 8))
button9 = Button(root, height=BUTTON_H, width=BUTTON_W, bg=BUTTON_BG, activebackground=BUTTON_ACTIVE_BG, image=null_img, cursor="circle", command= lambda: button_clicked(button9, 9))

# Create the retry functions
retry_button = Button(root, bg=BUTTON_BG, text='RETRY', foreground='#FFFFFF', command=reset_board)

# Create a player mode function
p_mode = Button(root, bg=BUTTON_BG, text='Player vs CPU', foreground='#FFFFFF', command=change_player_mode)

# Place the Labels on the board
Score_Label.grid(row=0,column=1, ipadx=32)
Player1_Label.grid(row=0, column=0, ipadx=23)
Player2_Label.grid(row=0, column=2, ipadx=23)

# Place the buttons on the board
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

button_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

# Place the Michallancheous buttons on screen
retry_button.grid(row=4, column=1, ipadx=32, pady=3)

# Place the player Mode button on screen
p_mode.grid(row=4, column=0)

# Indicates that X goes first
player_highlight()

root.mainloop()
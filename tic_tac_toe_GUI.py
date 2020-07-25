import tkinter as tk
from PIL import ImageTk, Image
import pygame
import random

class TicTacToe(tk.Frame):

    # Set all button's inner properties
    BUTTON_H = 100
    BUTTON_W = 100
    BUTTON_BG = '#4E4540'
    BUTTON_ACTIVE_BG = '#403834'

    def __init__(self, root, image_tuple):
        super().__init__(root)

        self.null_img, self.X_icon, self.X_img, self.X_hor, self.X_vert, self.X_diag, self.X_diag2, self.O_icon, self.O_img, self.O_hor, self.O_vert, self.O_diag, self.O_diag2 = image_tuple

        # Global list to hold values of the tic-tac-toe board. Each three positions represent a row on the board
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # A counter to keep track of turns
        self.turn = 0

        # A counter to keep track of player's scores
        self.x_score = 0
        self.o_score = 0

        # A bool to keep track if any player wins. 
        self.is_game_over_x = False
        self.is_game_over_o = False

        # A variable to keep track of player mode. ('pvp' = Player vs Player, 'pvc' = Player vs CPU)
        self.player_mode = 'pvc'

        # Creating the labels for player1,player2 and Score
        self.Score_Label = tk.Label(root, bg=self.BUTTON_BG, text=' 0 - 0 ', foreground='#FFFFFF')
        self.Player1_Label = tk.Button(root, bg=self.BUTTON_BG, image= self.X_icon, activebackground=self.BUTTON_BG, relief='flat')
        self.Player2_Label = tk.Button(root, bg=self.BUTTON_BG, image=self.O_icon, activebackground=self.BUTTON_BG, relief='flat')

        self.button1 = tk.Button(root, height=self.BUTTON_H, width=self.BUTTON_W, bg=self.BUTTON_BG, activebackground=self.BUTTON_ACTIVE_BG, image=self.null_img, cursor="circle", command= lambda: self.button_clicked(self.button1, 1))
        self.button2 = tk.Button(root, height=self.BUTTON_H, width=self.BUTTON_W, bg=self.BUTTON_BG, activebackground=self.BUTTON_ACTIVE_BG, image=self.null_img, cursor="circle", command= lambda: self.button_clicked(self.button2, 2))
        self.button3 = tk.Button(root, height=self.BUTTON_H, width=self.BUTTON_W, bg=self.BUTTON_BG, activebackground=self.BUTTON_ACTIVE_BG, image=self.null_img, cursor="circle", command= lambda: self.button_clicked(self.button3, 3))

        self.button4 = tk.Button(root, height=self.BUTTON_H, width=self.BUTTON_W, bg=self.BUTTON_BG, activebackground=self.BUTTON_ACTIVE_BG, image=self.null_img, cursor="circle", command= lambda: self.button_clicked(self.button4, 4))
        self.button5 = tk.Button(root, height=self.BUTTON_H, width=self.BUTTON_W, bg=self.BUTTON_BG, activebackground=self.BUTTON_ACTIVE_BG, image=self.null_img, cursor="circle", command= lambda: self.button_clicked(self.button5, 5))
        self.button6 = tk.Button(root, height=self.BUTTON_H, width=self.BUTTON_W, bg=self.BUTTON_BG, activebackground=self.BUTTON_ACTIVE_BG, image=self.null_img, cursor="circle", command= lambda: self.button_clicked(self.button6, 6))

        self.button7 = tk.Button(root, height=self.BUTTON_H, width=self.BUTTON_W, bg=self.BUTTON_BG, activebackground=self.BUTTON_ACTIVE_BG, image=self.null_img, cursor="circle", command= lambda: self.button_clicked(self.button7, 7))
        self.button8 = tk.Button(root, height=self.BUTTON_H, width=self.BUTTON_W, bg=self.BUTTON_BG, activebackground=self.BUTTON_ACTIVE_BG, image=self.null_img, cursor="circle", command= lambda: self.button_clicked(self.button8, 8))
        self.button9 = tk.Button(root, height=self.BUTTON_H, width=self.BUTTON_W, bg=self.BUTTON_BG, activebackground=self.BUTTON_ACTIVE_BG, image=self.null_img, cursor="circle", command= lambda: self.button_clicked(self.button9, 9))

        # Create a Button_List for the cpu player to use
        self.button_list = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9]

        # Create a reference dictionary for X and O image assets. 
        self.x_img_dict = {123: self.X_hor, 456:self.X_hor, 789:self.X_hor, 147:self.X_vert, 258: self.X_vert, 369: self.X_vert, 159: self.X_diag, 357: self.X_diag2}
        self.o_img_dict = {123: self.O_hor, 456:self.O_hor, 789:self.O_hor, 147:self.O_vert, 258: self.O_vert, 369: self.O_vert, 159: self.O_diag, 357: self.O_diag2}
        
        # Create the retry functions
        self.retry_button = tk.Button(root, bg=self.BUTTON_BG, text='RETRY', foreground='#FFFFFF', command=self.reset_board)

        # Create a player mode function
        self.p_mode = tk.Button(root, bg=self.BUTTON_BG, text='Player vs CPU', foreground='#FFFFFF', command=self.change_player_mode)
        
        # Initaliazie pygame to play button sound
        pygame.init()

        # Place the widgets on the board
        self.place_widgets()

        # Indicate its X's turn first
        self.player_highlight()

    def place_widgets(self):
        """ Used to place the widgets onto the board """
        # Place the Labels on the board
        self.Score_Label.grid(row=0,column=1, ipadx=32)
        self.Player1_Label.grid(row=0, column=0, ipadx=23)
        self.Player2_Label.grid(row=0, column=2, ipadx=23)

        # Place the buttons on the board
        self.button1.grid(row=1,column=0)
        self.button2.grid(row=1,column=1)
        self.button3.grid(row=1,column=2)

        self.button4.grid(row=2,column=0)
        self.button5.grid(row=2,column=1)
        self.button6.grid(row=2,column=2)

        self.button7.grid(row=3,column=0)
        self.button8.grid(row=3,column=1)
        self.button9.grid(row=3,column=2)

        # Place the retry button on screen
        self.retry_button.grid(row=4, column=1, ipadx=28, pady=3)

        # Place the player mode button on screen
        self.p_mode.grid(row=4, column=0)

    def button_clicked(self, button, button_idx):
        """ Place the move of the current player onto the button.
        
        if game mode is 'pvc', call :meth: play_cpu to place a move for cpu .

        :param button: The button object attribute
        :ptype: tk.Button

        :param (int) button_idx: The no.of button object clicked.
            Used to reference the button's place in the board attribute. 
        """
        if self.turn % 2 == 0:
            if self.board[button_idx-1] == 0:
                self.place_move_x(button, button_idx-1)
                gameOver = self.check_x_won()
                if self.player_mode == 'pvc' and gameOver is None:
                    self.play_cpu()
        else:
            if self.player_mode == 'pvp':
                if self.board[button_idx-1] == 0:
                    self.place_move_o(button, button_idx-1)

        self.check_game()
        self.player_highlight()

    def place_move_x(self, button, button_idx):
        """ Places a move for player 'X' 
        :param button: The button object that the player choose to place X. 
        :ptype: Tk.Button

        :param button_idx: The index of button in the board attribute
        """
        self.button_sound()
        button.config(image=self.X_img)
        self.board[button_idx] = 1
        self.turn += 1
        self.player_highlight()

    def place_move_o(self, button, button_idx):
        """ Places a move for player 'O'.
        Intended to be called when the game mode is 'pvp'
        
        :param button: The button object that the player choose to place X. 
        :ptype: Tk.Button

        :param button_idx: The index of button in the board attribute
        """
        self.button_sound()
        button.config(image=self.O_img)
        self.board[button_idx] = -1
        self.turn += 1

    def play_cpu(self):
        """ Function that chooses random spots to place 'O' for pc. """
        
        # Play button sound
        self.button_sound()

        while True:

            # If turns is 9, then all the places on the board are filled. Hence Cpu doesn't get a turn. 
            if self.turn >= 9:
                break

            # Choose a random position and if that position on board is empty, then place a 'O' there.
            i = random.randint(0, 8)
            if self.board[i] == 0:
                #root.after(400)
                self.button_list[i].config(image=self.O_img)
                self.board[i] = -1
                self.turn += 1

                break

    def reset_score(self):
        """ Resets the score for players.
        Will be called whenever the player changes the game-mode.
        """
        self.x_score = 0
        self.o_score = 0

    def change_button_state(self, button_state='normal'):
        """ Changes the state of buttons in the game to normal or disabled.
        Intended to be used internally.

        :param (str) button_state: Button state for all the buttons on the board.
            Accepts two valid answers: 'disabled' or 'normal'
        """
        self.button1.configure(state=button_state)
        self.button2.configure(state=button_state)
        self.button3.configure(state=button_state)
        self.button4.configure(state=button_state)
        self.button5.configure(state=button_state)
        self.button6.configure(state=button_state)
        self.button7.configure(state=button_state)
        self.button8.configure(state=button_state)
        self.button9.configure(state=button_state)

    def change_player_mode(self):
        """ Changes player mode when the player mode button is clicked.
        When Player mode is changed, it resets the text on button and sets both x and o score to 0.
        """

        # Checks if player mode is 'Player vs Player'
        if self.player_mode == 'pvp':
            self.p_mode.configure(text='Player vs CPU')
            self.player_mode = 'pvc'
            self.reset_score()
            self.reset_board()

        else:
            self.p_mode.configure(text='Player vs Player')
            self.player_mode = 'pvp'
            self.reset_score()
            self.reset_board()

    def update_score(self):
        """ Used when retry is clicked. Updates the self.Score_Label with the updated
        self.x_score and self.o_score. 
        """
        score_text = ' ' + str(self.x_score) + ' - ' + str(self.o_score) + ' '
        self.Score_Label.configure(text=score_text, foreground='#FFFFFF')

    def reset_board(self):
        """ Invoked when the player resets the board by clicking 'retry'. Acheives it by emptying the board attribute to a list of 0's, resetting the turn attribute to 0. 
        It also changes the images on all buttons to an empty 'null.png' image. Then it resets the score .
        """
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.turn = 0

        self.change_button_img_to_null()

        #self.Score_Label.grid(row=0,column=1, ipadx=32)

        self.player_highlight()
        self.change_button_state('normal')
        self.update_score()

    def change_button_img_to_null(self, null_img=None):
        """ Used to change the button image to default empty 'null.png' Image. """
        null_img = self.null_img
        self.button1.configure(image=null_img)
        self.button2.configure(image=null_img)
        self.button3.configure(image=null_img)

        self.button4.configure(image=null_img)
        self.button5.configure(image=null_img)
        self.button6.configure(image=null_img)

        self.button7.configure(image=null_img)
        self.button8.configure(image=null_img)
        self.button9.configure(image=null_img)

    def game_x_won(self, msg='YOU WON', fr='#32CD32'):
        """ Called when the game detects the Player or 'X' has won the game.

        :param (str) msg: The Message to display when the player or 'X' wins.
            Changes the Score_Label attribute to display message. Default is 'YOU WON'.

        :param (str) fr: The foreground color of the message. Default is Green color.
        """
        self.x_score += 1
        self.Score_Label.configure(text=msg, foreground=fr)
        self.Score_Label.grid(row=0,column=1, ipadx=12)
        self.change_button_state('disabled')

    def game_o_won(self, msg='YOU LOST', fr='#DC143C'):
        """ Called when the game detects the CPU or 'O' has won the game.

        :param (str) msg: The Message to display when the CPU or 'O' wins.
            Changes the Score_Label attribute to display message. Default is 'YOU LOST'.

        :param (str) fr: The foreground color of the message. Default is Red color.
        """
        self.o_score += 1
        self.Score_Label.configure(text=msg, foreground=fr)
        self.Score_Label.grid(row=0,column=1, ipadx=12)
        self.change_button_state('disabled')

    def game_tie(self, msg='YOU TIED', fr='#FFFF99'):
        """ Called when the game detects the player has tied with the CPU.

        :param (str) msg: The Message to display when the CPU or 'O' wins.
            Changes the Score_Label attribute to display message. Default is 'YOU LOST'.

        :param (str) fr: The foreground color of the message. Default is Red color.
        """
        self.Score_Label.configure(text=msg, foreground=fr)
        self.Score_Label.grid(row=0,column=1, ipadx=12)
        self.change_button_state('disabled')

    def check_game(self):
        """ Called every time a move is placed. Checks if either X or O won in any way or tied.
            Then updates the game state by calling the appropriate method. """
        gameOver = None
        if self.turn > 4:
            gameOver = self.check_x_won()
            if gameOver is True:
                self.game_x_won()
                return

        gameOver = None
        if self.turn > 5:
            gameOver = self.check_o_won()
            if gameOver is True:
                self.game_o_won()
                return

        if self.turn >= 9:
            self.game_tie()
            return

    def check_x_won(self, opp_sign = -1, empty_sign_num = 0):
        """ Checks if 'X' or player won in any of the horizontal, vertical and diagonal rows.
        Does the checks if seeing if any of the winning rows has no 'O's and no empty spots. 

        :returns: True or None 
        :rtype: bool or None
        """ 
        # Checks if X won horizontally
        if opp_sign not in self.board[0:3] and empty_sign_num not in self.board[0:3]:
            self.change_button_img_to_x(123)
            return True
        elif opp_sign not in self.board[3:6] and empty_sign_num not in self.board[3:6]:
            self.change_button_img_to_x(456)
            return True
        elif opp_sign not in self.board[6:9] and empty_sign_num not in self.board[6:9]:
            self.change_button_img_to_x(789)
            return True

        # Checks if X won vertically
        elif opp_sign not in self.board[0:7:3] and empty_sign_num not in self.board[0:7:3]:
            self.change_button_img_to_x(147)
            return True
        elif opp_sign not in self.board[1:8:3] and empty_sign_num not in self.board[1:8:3]:
            self.change_button_img_to_x(258)
            return True
        elif opp_sign not in self.board[2:9:3] and empty_sign_num not in self.board[2:9:3]:
            self.change_button_img_to_x(369)
            return True

        # Checks if X won diagonally
        elif opp_sign not in self.board[0:9:4] and empty_sign_num not in self.board[0:9:4]:
            self.change_button_img_to_x(159)
            return True
        elif opp_sign not in self.board[2:7:2] and empty_sign_num not in self.board[2:7:2]:
            self.change_button_img_to_x(357)
            return True

        # if X didn't win yet, return None 
        else:
            return None

    def check_o_won(self, opp_sign_num = 1, empty_sign_num = 0):
        """ Checks if 'O' or CPU/P2 won in any of the horizontal, vertical and diagonal rows.
        Does the checks if seeing if any of the winning rows has no 'X's and no empty spots. 

        :returns: True or None 
        :rtype: bool or None
        """ 
        if opp_sign_num not in self.board[0:3] and empty_sign_num not in self.board[0:3]:
            self.change_button_img_to_o(123)
            return True
        elif opp_sign_num not in self.board[3:6] and empty_sign_num not in self.board[3:6]:
            self.change_button_img_to_o(456)
            return True
        elif opp_sign_num not in self.board[6:9] and empty_sign_num not in self.board[6:9]:
            self.change_button_img_to_o(789)
            return True

        # Checks if O won vertically
        elif opp_sign_num not in self.board[0:7:3] and empty_sign_num not in self.board[0:7:3]:
            self.change_button_img_to_o(147)
            return True
        elif opp_sign_num not in self.board[1:8:3] and empty_sign_num not in self.board[1:8:3]:
            self.change_button_img_to_o(258)
            return True
        elif opp_sign_num not in self.board[2:9:3] and empty_sign_num not in self.board[2:9:3]:
            self.change_button_img_to_o(369)
            return True

        # Checks if O won diagonally
        elif opp_sign_num not in self.board[0:9:4] and empty_sign_num not in self.board[0:9:4]:
            self.change_button_img_to_o(159)
            return True
        elif opp_sign_num not in self.board[2:7:2] and empty_sign_num not in self.board[2:7:2]:
            self.change_button_img_to_o(357)
            return True
        
        # if O didn't win yet, return None
        else:
            return None

    def change_button_img_to_x(self, row_seq):
        """ Changes all the images in a row into the related striked X image. 
        Utilized when X has successfully put 3 in some winnable row. 

        :param (int) row_seq: The indices of the 3 places P1 has put X to win the game. Eg: row_seq=123 if X won in the first row.
            See below for row_seq reference
            
        1 2 3
        4 5 6
        7 8 9
        """
        change_img = self.x_img_dict[row_seq]
        idx_list = [int(i)-1 for i in str(row_seq)]
        for button_idx in idx_list:
            self.button_list[button_idx].config(image=change_img)

    def change_button_img_to_o(self, row_seq):
        """ Changes all the images in a row into the related striked O image. 
            Utilized when O has successfully put 3 in some winnable row. 

        :param (int) row_seq: The indices of the 3 places P2/CPU has put O to win the game. Eg: row_seq=123 if O won in the first row.
            See below for row_seq reference
            
        1 2 3
        4 5 6
        7 8 9
        """
        change_img = self.o_img_dict[row_seq]
        idx_list = [int(i)-1 for i in str(row_seq)]
        for button_idx in idx_list:
            self.button_list[button_idx].config(image=change_img)

    def button_sound(self):
        """ Utilizes the pygame module to play button sound.
            This method is called whenever a button has been clicked and a valid move has been selected. 
        """
        sound = pygame.mixer.Sound('assests/sounds/Button_Sound.wav')
        sound.play()

    def player_highlight(self):
        """ Puts a Square around the icon of the player who has to go next.
            The icon of the play is indicated in the top row.
        """
        if self.turn % 2 == 0:
            self.Player2_Label.configure(relief='flat')
            self.Player1_Label.configure(relief='groove')
        else:
            self.Player1_Label.configure(relief='flat')
            self.Player2_Label.configure(relief='groove')

def gather_images():
    """ External function used to gather images from the folder. """
    # Import an empty image
    null_img = Image.open('assests/null/null.png')
    null_img = ImageTk.PhotoImage(null_img.resize((100,100), Image.ANTIALIAS))

    # Import image and icon for X
    X_img = Image.open('assests/X_Assets/X.png')
    X_icon = ImageTk.PhotoImage(X_img.resize((15, 12), Image.ANTIALIAS))
    X_img = ImageTk.PhotoImage(X_img.resize((95, 80), Image.ANTIALIAS))

    # Import horizontally striked X
    X_hor = Image.open('assests/X_Assets/X_hor.png')
    X_hor = ImageTk.PhotoImage(X_hor.resize((95, 80), Image.ANTIALIAS))

    # Import vertically striked X
    X_vert = Image.open('assests/X_Assets/X_vert.png')
    X_vert = ImageTk.PhotoImage(X_vert.resize((95, 80), Image.ANTIALIAS))

    # Import diagonally strikedX
    X_diag = Image.open('assests/X_Assets/X_diag.png')
    X_diag = ImageTk.PhotoImage(X_diag.resize((95, 80), Image.ANTIALIAS))

    # Import another diagonally striked X
    X_diag2 = Image.open('assests/X_Assets/X_diag2.png')
    X_diag2 = ImageTk.PhotoImage(X_diag2.resize((95, 80), Image.ANTIALIAS))

    # Import image and icon for O
    O_img = Image.open('assests/O_Assets/O.png')
    O_icon = ImageTk.PhotoImage(O_img.resize((14, 14), Image.ANTIALIAS))
    O_img = ImageTk.PhotoImage(O_img.resize((90, 90), Image.ANTIALIAS))

    # Import horizontally striked O
    O_hor = Image.open('assests/O_Assets/O_hor2.png')
    O_hor = ImageTk.PhotoImage(O_hor.resize((90, 90), Image.ANTIALIAS))

    # Import vertically striked O
    O_vert = Image.open('assests/O_Assets/O_vert2.png')
    O_vert = ImageTk.PhotoImage(O_vert.resize((90, 90), Image.ANTIALIAS))

    # Import diagonally striked O
    O_diag = Image.open('assests/O_Assets/O_diag.png')
    O_diag = ImageTk.PhotoImage(O_diag.resize((90, 90), Image.ANTIALIAS))

    # Import another diagonally striked O
    O_diag2 = Image.open('assests/O_Assets/O_diag2.png')
    O_diag2 = ImageTk.PhotoImage(O_diag2.resize((90, 90), Image.ANTIALIAS))

    return (null_img, X_icon, X_img, X_hor, X_vert, X_diag, X_diag2, O_icon, O_img, O_hor, O_vert, O_diag, O_diag2)


# Run the program when file is run
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tic Tac Toe')
    root.configure(bg='#4E4540')
    root.resizable(width=False, height=False)
    image_tuple = gather_images()
    tictactoe = TicTacToe(root=root, image_tuple=image_tuple)
    tictactoe.mainloop()
from IPython.display import clear_output

def display_board(board):
    
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])
    clear_output()

def player_input():
    
    print("Do you want 'X' or 'O' as your marker ?")
    player1 = str(input())
    while True:        
        if (player1 != 'X') and (player1 !='O'):
            print("Kindly enter a valid input for maker.")
            player1 = str(input())
        else:
            break
    print("Player 1 have selected {} as your maker.".format(player1))

def place_marker(board, marker, position):    
    board[position] = marker


def win_check(board, mark):
    if (
        
        (mark == board[7] and board[8] and board[9]) or 
        (mark == board[4] and board[5] and board[6]) or
        (mark == board[1] and board[2] and board[3]) or

        (mark == board[7] and board[4] and board[1]) or 
        (mark == board[8] and board[5] and board[2]) or
        (mark == board[9] and board[6] and board[3]) or

        (mark == board[7] and board[5] and board[3]) or 
        (mark == board[1] and board[5] and board[9])

        ):
        return True

import random

def choose_first():
    val = random.randint(0,1)
    if val == 0:
        print("Player1 will make the first move")
    else:
        print("Player2 will make the first move")


def space_check(board,position):
    if board[position] == "":
        return True

def full_board_check(board):
    for item in board:
        if (item == ""):
            return False
        else:
            return True

def player_choice(board):
    position = int(input("Kindly enter the number for next move"))
    if space_check(board,position) == True:
        return position

def replay():
    
    play_again = str(input("Are you ready to play the game again ? Enter Yes or No"))
    if play_again == "Yes":
        return True
    elif play_again == "No":
        return False

print('Welcome to Tic Tac Toe!')

while True:
    

    while game_on:
        Player 1 Turn
        
        
        Player2's turn.
            
            pass

    if not replay():
        break
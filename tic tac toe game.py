from random import random
from ipython.display import clear_output

# This will show you a bard as a list of 3*3
def display_board(board):

    clear_output()         # This will clear the history of board.

    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

# Testing the Board
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

# Marker assignment of players X and O
def player_input():
    '''
    OUTPUT = (player 1 marker, Player 2 marker )
    '''
    marker = ""
    while marker != 'X' and marker != 'O':    # 2nd way  while not (marker == 'X' or marker == 'O':)
        marker = input('Player1: Choose X or O: ').upper()
    if marker == 'X':
        reutrn('X','O')
    else:
        return ('O','X')
    

#This will assign positon of marker in board
def place_marker(board,marker,position):
    board[position] = marker


#This will check which mark is won 
def win_check(board,mark):
    #To check in row if there's samw marker in a row thwn 
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #For bottom row
            (board[4] == mark and board[5] == mark and board[6] == mark) or #For middle row 
            (board[7] == mark and board[8] == mark and board[9] == mark) or #For bottom row
            (board[1] == mark and board[4] == mark and board[7] == mark) or #for 1st coloumn
            (board[2] == mark and board[5] == mark and board[8] == mark) or #For middle coloumn
            (board[3] == mark and board[6] == mark and board[9] == mark) or #For third coloumn
            (board[1] == mark and board[5] == mark and board[9] == mark) or #For diagonally
            (board[3] == mark and baord[5] == mark and boord[7] == mark))   #For diagonally


#This will Toss who will move first Player 1 or Player 2
import random
def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    

#This will check the free space in the board (Boolean indicator)

def space_check(board,position):
    return board[position] == ' '

#This will check the board is full or not (Boolean indicator)
def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False                                                       #Board has free space if we get false
    return True                                                                #Board is full is we get True



#This will ask Player to assign mark to baord position in range and return the position for future use
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
    return position

#This will ask them to play again or not
def replay():
    choice = input("Play again?  Enter Yes or No")
    return choice == 'Yes'

#Final or Main Game code 
print('Welcome to TIC TAC TOE')

while True:
    #This will Play the game

    ##Things to be set (baord,first player,chooosing marker X,O)
    the_board = [' ']*10
    player1_marker,player2_marker = plauyer_input()

    turn = choose_first()
    print(turn+ ' Congrats you are first')

    play_game = input('Ready to Battle? Y or N')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

     ## GAME PLAY
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)                                  #It will show the board to choose the position to Player
            position = player_choice(the_board)                       #Allows to Player to choose the position
            place_marker(the_board,player1_marker,position)           #It will palce the marker as per input of Player
            if win_check(the_board,player1_marker):                   #This will check if they wom or not
                display_board(the_board)
                print('Boommm! Player1 has Won!!!!')
                game_on = False
            else:                                                     #This will check is the game is tie or not
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Dmannn This is TIEEE!!!!')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)                                  #It will show the board to choose the position to Player
            position = player_choice(the_board)                       #Allows to Player to choose the position
            place_marker(the_board,player2_marker,position)           #It will palce the marker as per input of Player
            if win_check(the_board,player2_marker):                   #This will check if they wom or not
                display_board(the_board)
                print('Boommm! Player2 has Won!!!!')
                game_on = False
            else:                                                     #This will check is the game is tie or not
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Dmannn This is TIEEE!!!!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():                                                   #This will end the game (while loop basically)
        break


                     
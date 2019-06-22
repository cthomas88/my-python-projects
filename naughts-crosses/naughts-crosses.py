import random
# create the board

def display_board(board):
    print('\n'*50)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    

starting_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
display_board(starting_board)

# Define game players names

player1_name = input('What is your name player 1? ')
player2_name = input('What is your name player 2? ')

# Players choose their playing piece

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input(f'{player1_name} please choose either X or O: ').upper()
    
    player1 = marker
    if player1 == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
    return (player1, player2)

player1, player2 = player_input()

# First or second

def first_or_second():
    choice1 = input(f'{player1_name}, would you like to go first or second? ')
    if choice1.lower() == 'first':
        print(f'''{player1_name}, you have chosen to use {player1} 
        and have chosen to go first''')
    else:
        print (f'''{player1_name}, you have chosen to use {player1} 
        and have chosen to go second''')

def place_marker(board, marker, position):

    board[position] = marker

def check_winner(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark) or
    (board[7] == board[5] == board[3] == mark))

# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


    
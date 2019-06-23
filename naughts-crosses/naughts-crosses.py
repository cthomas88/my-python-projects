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
    
# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
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

    p1choice = input(f'{player1_name} choose heads or tails: ')
     
    flip = random.randint(1, 2)

    if flip == 1 and p1choice.lower() == 'heads':
        print (f'{player1_name} the coin has landed on heads, you go first!')
    else:
        print (f'{player1_name} the coin has landed on tails, {player2_name} you go first!')

# Choose where to place your first move

def place_marker(board, marker, position):

    board[position] = marker

# Check whether anyone has won the game

def check_winner(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark) or
    (board[7] == board[5] == board[3] == mark))

# Check whether a space is free

def space_check (board, position):

    return board[position] == '1' or
    board[position] == '2' or
    board[position] == '3' or
    board[position] == '4' or
    board[position] == '5' or
    board[position] == '6' or
    board[position] == '7' or
    board[position] == '8' or
    board[position] == '9'


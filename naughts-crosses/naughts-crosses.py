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

first_or_second()

def place_marker(board, marker, position):

    board[position] = marker

def check_winner(board, mark):
    return ((mark == board[1] and mark == board[2] and mark == board[3]) or
    (mark == board[4] and mark == board[5] and mark == board[6]) or
    (mark == board[7] and mark == board[8] and mark == board[9]) or
    (mark == board[7] and mark == board[4] and mark == board[1]) or
    (mark == board[8] and mark == board[5] and mark == board[2]) or
    (mark == board[9] and mark == board[6] and mark == board[3]) or
    (mark == board[9] and mark == board[5] and mark == board[1]) or
    (mark == board[7] and mark == board[5] and mark == board[3]))

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


    
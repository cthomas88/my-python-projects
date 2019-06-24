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

# First or second

def first_or_second():

    p1choice = input(f'{player1_name} choose heads or tails: ')
     
    flip = random.randint(1, 2)

    if flip == 1 and p1choice.lower() == 'heads':
        return (player1_name + " the coin landed on heads, you're up frist!")
    else:
        return (player2_name + " the coin landed on tails, you're up first!")

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

    return ((board[position] == '1') or
    (board[position] == '2') or
    (board[position] == '3') or
    (board[position] == '4') or
    (board[position] == '5') or
    (board[position] == '6') or
    (board[position] == '7') or
    (board[position] == '8') or
    (board[position] == '9'))

    return True

# Check if board is full

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True

# Player chooses a position

def player_choice(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        position = int(input('Please enter a position to place your piece (1-9): '))
    
    return position

def replay():

    replay_y_n = input('GAME OVER!! Would you like to play again? Yes or No: ')

    return replay_y_n.lower[0] == 'y'

# While loop that keeps the game running

print ('WELCOME TO NAUGHTS AND CROSSES!!')

while True:
    # Play the game

    ## Set everything up (board, name, who's first, marker choice)

    the_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    player1, player2 = player_input()

    turn = first_or_second()
    print (turn)

    play_game = input('Are you ready to start the game? ')

    if play_game.lower = 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == player1_name:

            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1, position)
            # Check if they won
            if check_winner(the_board, player1):
                display_board(the_board)
                print (f'{player1_name} congratulations, you have won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print ('This game is a tie!')
                    game_on = False
                else:
                    turn = player2_name
            

            # If no tie and no win next player's turn


        ### First player turn

        else:

            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2, position)
            # Check if they won
            if check_winner(the_board, player2):
                display_board(the_board)
                print (f'{player2_name} congratulations, you have won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print ('This game is a tie!')
                    game_on = False
                else:
                    turn = player1_name

    if not replay():
        break
# Break out of the while loop while on replay()


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

player1_name = input('\nWhat is your name player 1? ')
player2_name = input('\nWhat is your name player 2? ')

# Players choose their playing piece


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input(f'\n{player1_name} please choose either X or O: ').upper()
    
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
    return (player1, player2)

# First or second


def first_or_second():

    p1choice = input(f'\n{player1_name} choose heads or tails: ')
    print('\n')
     
    flip = random.randint(1, 2)

    if flip == 1 and p1choice.lower() == 'heads':
        return (player1_name + " the coin landed on heads, you're up frist!")
    elif flip == 1 and p1choice.lower() == 'tails':
        return (player1_name + f" the coin landed on heads, {player2_name}, you're up first!")
    elif flip == 2 and p1choice.lower() == 'heads':
        return (player1_name + f" the coin landed on tails, {player2_name}, you're up first!")
    elif flip == 2 and p1choice.lower() == 'tails':
        return (player1_name + " the coin landed on tails, you're up first!")

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


def space_check(board, position):

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

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('\nPlease enter a position to place your piece (1-9): '))

    return position


def replay():

    yes_or_no = input('\nGAME OVER!! Would you like to play again? Yes or No: ').lower()

    if yes_or_no[0] == 'y':
        return True

# While loop that keeps the game running

print('\nWELCOME TO NAUGHTS AND CROSSES!!')

while True:
    # Play the game

    # Set everything up (board, name, who's first, marker choice)

    the_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    turn = first_or_second()
    
    player1, player2 = player_input()

    print(turn)

    play_game = input(f'\n{player1_name} and {player2_name} are you ready to start the game? ')

    if play_game.lower() == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == player1_name + " the coin landed on heads, you're up frist!" or turn == player1_name + " the coin landed on tails, you're up first!":

            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1, position)
            # Check if they won
            if check_winner(the_board, player1):
                display_board(the_board)
                print(f'\n{player1_name} congratulations, you have won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('\nThis game is a tie!')
                    game_on = False
                else:
                    turn = player1_name + f" the coin landed on heads, {player2_name}, you're up first!"

            # If no tie and no win next player's turn

        # First player turn

        elif turn == player1_name + f" the coin landed on heads, {player2_name}, you're up first!" or turn == player1_name + f" the coin landed on tails, {player2_name}, you're up first!":

            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2, position)
            # Check if they won
            if check_winner(the_board, player2):
                display_board(the_board)
                print(f'\n{player2_name} congratulations, you have won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('\nThis game is a tie!')
                    game_on = False
                else:
                    turn = player1_name + " the coin landed on heads, you're up frist!"

    if not replay():
        print(f'\nThanks for playing {player1_name} and {player2_name}, see you next time!')
        break
# Break out of the while loop while on replay()
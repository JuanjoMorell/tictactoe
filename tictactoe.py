# Variables
board = [' ' for x in range(10)]


# Funciones Principales
def insert_letter(letter, pos):
    board[pos] = letter


def space_free(pos):
    return board[pos] == ' '


def print_board():
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def is_winner(bo, le):
    if bo[7] == le and bo[8] == le and bo[9] == le:
        return 1
    elif bo[4] == le and bo[5] == le and bo[6] == le:
        return 1
    elif bo[1] == le and bo[2] == le and bo[3] == le:
        return 1
    elif bo[1] == le and bo[4] == le and bo[7] == le:
        return 1
    elif bo[2] == le and bo[5] == le and bo[8] == le:
        return 1
    elif bo[3] == le and bo[6] == le and bo[9] == le:
        return 1
    elif bo[1] == le and bo[5] == le and bo[9] == le:
        return 1
    elif bo[3] == le and bo[5] == le and bo[6] == le:
        return 1
    else:
        return 0


def player_move():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if 0 < move < 10:
                if space_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range')
        except:
            print('Please type a number!')


def comp_move():
    pass


def select_random(bo):
    pass


def is_board_full(bo):
    if bo.count(' ') > 1:
        return True
    else:
        return False


def main():
    print('Welcome to Tic Tac Toe!')
    print_board()

    while not (is_board_full(board)):
        if not (is_winner(board, 'O')):
            player_move()
            print_board()
        else:
            print('Sorry, O\'s won this time!')
            break

        if not (is_winner(board, 'X')):
            comp_move()
            print_board()
        else:
            print('X\'s won this time! Good Job!')
            break

    if is_board_full(board):
        print('Tie Game!')


main()

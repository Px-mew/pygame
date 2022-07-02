"""Крестики-нолики"""

import random

def draw_board(board):
    """Выводит на экран игровое поле."""
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def input_player_letter():
    """Выбор буквы игрока."""
    letter = ''
    while letter not in ('Х', 'О', 'X', 'O', '0'):
        print('Вы выбираете Х или О?')
        letter = input().upper()
    if letter in ('Х', 'X'):
        return ['Х', 'О']
    return ['О', 'Х']

def who_goes_first():
    """Случайный выбор кто ходит первым."""
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    return 'Человек'

def make_move(board, letter, move):
    """Сделать ход."""
    board[move] = letter

def is_winner(bo, le):
    """Возвращает True, если игрок выиграл."""
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def get_board_copy(board):
    """Создает копию игрового поля и возвращает его."""
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy

def is_space_free(board, move):
    """Возвращает True, если сделан ход в свободную клетку."""
    return board[move] == ' '

def get_player_move(board):
    """Разрешение игроку сделать ход."""
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('Ваш следующий ход? (1-9)')
        move = input()
    return int(move)

def choose_random_move_from_list(board, moves_list):
    """Возвращает допустимые ходы."""
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    return None

def get_computer_move(board, computer_letter):
    """Учитывая заполнение игрового поля и букву компьютера, определяет допустимый ход и возвращает его."""
    if computer_letter == 'Х':
        player_letter = 'О'
    else:
        player_letter = 'Х'

    # Проверка — победит ли компьютер, сделав следующий ход.
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, computer_letter, i)
            if is_winner(board_copy, computer_letter):
                return i

    # Проверка — победит ли игрок, сделав следующий ход, и блокировка этого хода.   
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
            if is_winner(board_copy, player_letter):
                return i

    # Занять один из углов, если есть свободные.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Занять центр, если он свободен.
    if is_space_free(board, 5):
        return 5

    # Xод по одной стороне.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    """Возвращает True, если клетка на игровом поле занята. В противном случае, возвращает False."""
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('Игра "Крестики-нолики"')

while True:
    # Обновление игрового поля
    board = [' '] * 10
    playerLetter, computerLetter = input_player_letter()
    turn = who_goes_first()
    print('' + turn + ' ходит первым.')
    game_is_playing = True
    while game_is_playing:
        if turn == 'Человек':
            # Ход игрока.
            draw_board(board)
            move = get_player_move(board)
            make_move(board, playerLetter, move)

            if is_winner(board, playerLetter):
                draw_board(board)
                print('Ура! Вы выиграли!')
                game_is_playing = False
            elif is_board_full(board):
                draw_board(board)
                print('Ничья!')
                break
            else:
                turn = 'Компьютер'

        else:
            # Ход компьютера.
            move = get_computer_move(board, computerLetter)
            make_move(board, computerLetter, move)
            if is_winner(board, computerLetter):
                draw_board(board)
                print('Компьютер победил! Вы проиграли.')
                game_is_playing = False
            elif is_board_full(board):
                draw_board(board)
                print('Ничья!')
                break
            else:
                turn = 'Человек'

    print('Сыграем еще раз? (да или нет)')
    if not input().lower().startswith('l') and not input().lower().startswith('l'):
        break

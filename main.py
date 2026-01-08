# # Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game.
# print("""
# __________                    __________                          __________
# MMMMMMMMMM 68b                MMMMMMMMMM                          MMMMMMMMMM
# /   MM   / Y89                /   MM   /                          /   MM   /
#     MM     ___   ____             MM        ___      ____             MM       _____     ____
#     MM     `MM  6MMMMb.           MM      6MMMMb    6MMMMb.           MM      6MMMMMb   6MMMMb
#     MM      MM 6M'   Mb           MM     8M'  `Mb  6M'   Mb           MM     6M'   `Mb 6M'  `Mb
#     MM      MM MM    `'           MM         ,oMM  MM    `'           MM     MM     MM MM    MM
#     MM      MM MM                 MM     ,6MM9'MM  MM                 MM     MM     MM MMMMMMMM
#     MM      MM MM                 MM     MM'   MM  MM                 MM     MM     MM MM
#     MM      MM YM.   d9           MM     MM.  ,MM  YM.   d9           MM     YM.   ,M9 YM    d9
#    _MM_    _MM_ YMMMM9           _MM_    `YMMM9'Yb. YMMMM9           _MM_     YMMMMM9   YMMMM9
#
#
#
# """)
# print("""████████████████████████████████████████
# ████████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█████████
# █████▀▀░░░░░░░░░░░░░░░░░░░░░░░░░▀███████
# ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████
# ███▀░░░░░▄▄▄░░░░░░░░▄▄▀███▄▄░░░░░░░█████
# ██░░░░░░▀▀▀███▄▄░░░█▄▄█▀█▀▀▀▀░▀░▄▄░▀▀███
# █░░▄▄░▄▄░▄░░░█▀░░░░░░░░░░▀▄▄▄█▀▀▄░▀█░░▀█
# █░░░░▄░▀▀░░▄█▀░░░░░░▄▄░░░░░░░▄▄▀██▄░█░░█
# ██░░░██░░░▀▀█▄░░░▀▀▀▄▀░▄▄▄███▀░▄█░░░▀░▄█
# ██▄░██▀█▀▄▄▄▄▄█▄▄▄▄▄▀▀█▀░░▄███▀█▀░░░▄▄██
# ███░████▄█▄░░█░░▄█░░▄▄███▀▀▀█▄▀░░░░▄████
# ███░▀██████████████▀▀▀▀█░░░▄▀▀░░░░▄█████
# ███░░██▀█▀██▀█▀░░▀█░░░░█▄█▀░░░░░▄███████
# ███░░░░▀▀▀██▄██▄▄██▀▀▀▀▀░░░░░▄▄█████████
# ██▀░░░░░░░░░░░░░░░░░░░░░░▄▄▄████████████
# ██▄░░░░░░░░░░░░░░░░░░▄▄█████████████████
# ████▄░░░░░░░░░▄▄▄▄▄█████████████████████
# ████████████████████████████████████████""")

rash = [['   1   ', '   2   ', '   3   '],
        [' A ', '  ', ' | ', '  ', ' | ', '  '],
        [' B ', '  ', ' | ', '  ', ' | ', '  '],
        [' C ', '  ', ' | ', '  ', ' | ', '  ']]

# printing the tic tac toe game
def print_rash():
    print('\n')

    for fila in rash:
        for item in fila:
            print(item, end=' ')

        print('\n')

#load correct position
def posicao(pos):
    pos = pos + (pos - 1)
    return pos

# add position in array
def add_posi(player, local_y, local_x):
    rash[local_y][posicao(local_x)] = player


# Split the string in real positions in array
def split_site(site):
    local_y = 0
    local_x = 0
    model = ['A','B','C']
    for item in site:
        if item in model:
            for letter in model:
                if item == 'A':
                    local_y = 1
                elif item == 'B':
                    local_y = 2
                else:
                    local_y = 3
        else:
            local_x = int(item)

    return local_x, local_y

# ---------------------- Add player configurations
player_1 = input("Player 1 type out 'X' or 'O': ").upper()
player_2 = ''
if player_1 == 'X':
    print('player 2 you are "O" ')
    player_2 = 'O'
else:
    print('Player 2 you are "X" ')
    player_2 = 'X'
print_rash()

# start game
while True:
    site = input("Player 1 Type out one letter and a number: ").upper()

    locals = split_site(site)
    print(locals)

    add_posi(player=player_1, local_y= locals[1], local_x=locals[0])
    print_rash()

    site = input('Player 2 typed out one letter and a number').upper()

    locals = split_site(site)
    print(locals)

    add_posi(player=player_2, local_y=locals[1], local_x=locals[0])
    print_rash()
import os


def print_pole(pole):
    i = 0
    print("  0 1 2")
    for item in pole:
        print(i, end=' ')
        for jtem in item:
            print(jtem, end=' ')
        i += 1
        print()


def do_hod():
    i = ''
    j = ''
    while not i.isdigit() or not j.isdigit() or (int(i) < 0 or int(i) >= 3) or (int(j) < 0 or int(j) >= 3):
        print("ведите номера клеток")
        i = input()
        j = input()
    return [int(i), int(j)]


def try_to_game(position, pole, hod):
    if pole[position[0]][position[1]] == '-':
        if hod % 2 == 0:
            pole[position[0]][position[1]] = 'x'
        else:
            pole[position[0]][position[1]] = '0'
        return True
    else:
        return False


def game_end(pole):
    for i in range(3):
        if pole[i].count('x') == 3 or pole[i].count('0') == 3:
            return True
    if pole[0][0] == pole[1][1] == pole[2][2] == '0' or pole[0][0] == pole[1][1] == pole[2][2] == 'x':
        return True
    if pole[0][0] == pole[1][0] == pole[2][0] == '0' or pole[0][0] == pole[1][0] == pole[2][0] == 'x':
        return True
    if pole[1][0] == pole[1][1] == pole[1][2] == '0' or pole[1][0] == pole[1][1] == pole[1][2] == 'x':
        return True
    if pole[2][0] == pole[2][1] == pole[2][2] == '0' or pole[2][0] == pole[2][1] == pole[2][2] == 'x':
        return True
    if pole[0][2] == pole[1][1] == pole[2][0] == '0' or pole[0][2] == pole[1][1] == pole[2][0] == 'x':
        return True

    return False


criss_cross = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

count_hod = 0
print_pole(criss_cross)
GAME = True

while GAME:
    ij = do_hod()

    if try_to_game(ij, criss_cross, count_hod):
        os.system('cls')
        print_pole(criss_cross)
        count_hod += 1
    else:
        print("Это поле занято, введите новые значения")
        ij = do_hod()

    out_moves = count_hod == 9
    if game_end(criss_cross) or out_moves:
        GAME = False
        if out_moves:
            print("Ничья")
        elif count_hod % 2 != 0:
            print("Крестики победили")
        else:
            print("Нолики победили")


else:
    print("Спасибо за игру")

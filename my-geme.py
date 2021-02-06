game_place = [['   ', 7, ' | ', 8, ' | ', 9], ['  ', '――', ' ', '―― ', '――', ''], ['   ', 4, ' | ', 5, ' | ', 6],
              ['  ', '――', ' ', '―― ', '――', ''], ['   ',1, ' | ', 2, ' | ', 3]]

def print_place(place):
    for j in range(5):
        print(' '.join(map(str, place[j])))
    print('')



def play_cross():
    cross = int(input('Игрок1: Введите номер клетки для "X":  '))
    if not proverka_cross(cross):
        play_cross()
    print_place(game_place)

def play_zero():
    zero = int(input('Игрок2: Введите номер клетки для "0":  '))
    if not proverka_zero(zero):
        play_zero()
    print_place(game_place)

def proverka_cross(x):
    for i in range(5):
        for j in range(6):
            if game_place[i][j] == x:
                game_place[i][j] = "X"
                return True
    print('Некорректное значение')
    return False

def proverka_zero(x):
    for i in range(5):
        for j in range(6):
            if game_place[i][j] == x:
                game_place[i][j] = "0"
                return True
    print('Некорректное значение')
    return False

def search_win():
    for i in range(len(game_place)):
        if game_place[i][1] == game_place[i][3] == game_place[i][5]:
            print('Победа! Игра окончена!')
            return True
    for i in range(1, 6, 2):
        if game_place[0][i] == game_place[2][i] == game_place[4][i]:
            print('Победа! Игра окончена!')
            return True
    if game_place[0][1] == game_place[2][3] == game_place[4][5] or game_place[0][5] == game_place[2][3] == game_place[4][1]:
        print('Победа! Игра окончена!')
        return True




def game():
    print_place(game_place)
    count = 0
    while True:

        play_cross()
        count += 1
        if search_win():
            break
        if count == 9:
            print('Ничья, играйте заноово!')
            break
        play_zero()
        count += 1
        if search_win():
            break


game()
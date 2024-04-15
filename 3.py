import random

class NavalBattle:
    playing_field = [[0] * 10 for _ in range(10)]

    def __init__(self, symb):
        self.symb = symb

    def __str__(self):
        return f'{self.symb}'

    def __repr__(self):
        self.__str__()

    def shot(self, x, y):
        if NavalBattle.playing_field == [[0] * 10] * 10:
            print('игровое поле не заполнено')
        else:
            if NavalBattle.playing_field[y - 1][x - 1] == 1:
                NavalBattle.playing_field[y - 1][x - 1] = self.symb
                print('попал')
            elif NavalBattle.playing_field[y - 1][x - 1] == 0:
                NavalBattle.playing_field[y - 1][x - 1] = 'o'
                print('мимо')
            else:
                print('ошибка')

    @staticmethod
    def show():
        show = []
        for i in range(len(NavalBattle.playing_field)):
            show.append(NavalBattle.playing_field[i][:])  # копируем список из списка списков отдельно
        for i in range(len(show)):
            for j in range(len(show)):
                if show[i][j] in [0, 1]:
                    show[i][j] = '~'
        for i in show:
            print(*i)

    @staticmethod
    def new_game():
        NavalBattle.playing_field = [[0] * 10 for _ in range(10)]
        def beyond_borders(num_line, num_elem, len_ship):
            if num_line + len_ship > 9 and num_elem + len_ship > 9:
                return False


        def other_ships(num_line, num_elem, len_ship, dir):  # сталкиваемся с кем-то или нет
            def other_dir(num_line, num_elem, len_ship, dir):
                if dir == 1:
                    if num_line + len_ship > 9:
                        return False
                    for i in range(-1, len_ship + 1):
                        for j in range(-1, 2):
                            if (num_line + i < 0 or num_line + i > 9) or (num_elem + j < 0 or num_elem + j > 9):
                                continue
                            if NavalBattle.playing_field[num_line + i][num_elem + j] != 0:
                                return False
                    return dir
                if dir == 0:
                    if num_elem + len_ship > 9:
                        return False
                    for i in range(-1, len_ship + 1):
                        for j in range(-1, 2):
                            if num_elem + i < 0 or num_elem + i > 9 or num_line + j < 0 or num_line + j > 9:
                                continue
                            if NavalBattle.playing_field[num_line + j][num_elem + i] != 0:
                                return False
                    return dir

            if dir == 1:
                if num_line + len_ship > 9:
                    return False
                for i in range(-1, len_ship + 1):
                    for j in range(-1, 2):
                        if (num_line + i < 0 or num_line + i > 9) or (num_elem + j < 0 or num_elem + j > 9):
                            continue
                        if NavalBattle.playing_field[num_line + i][num_elem + j] != 0:
                            other_d = other_dir(num_line, num_elem, len_ship, 0)
                            return other_d
                return True
            if dir == 0:
                if num_elem + len_ship > 9:
                    return False
                for i in range(-1, len_ship + 1):
                    for j in range(-1, 2):
                        if num_elem + i < 0 or num_elem + i > 9 or num_line + j < 0 or num_line + j > 9:
                            continue
                        if NavalBattle.playing_field[num_line + j][num_elem + i] != 0:
                            other_d = other_dir(num_line, num_elem, len_ship, 1)
                            return other_d
                return True

        def placing_ship(num_line, num_elem, len_ship, dir, points):
            if dir == 1:
                for _ in range(len_ship):
                    NavalBattle.playing_field[num_line][num_elem] = 1
                    points.append([num_line, num_elem])
                    num_line += 1
                return NavalBattle.playing_field
            else:
                for _ in range(len_ship):
                    NavalBattle.playing_field[num_line][num_elem] = 1
                    num_elem += 1
                return NavalBattle.playing_field

        def cicle_sh(num_ships, len_ship):
            points = []
            while num_ships != 0:
                num_line = random.randint(0, 9)
                num_elem = random.randint(0, 9)
                if [num_line, num_elem] in points:
                    continue
                res_b_bord = beyond_borders(num_line, num_elem, len_ship)  # не выходит ли за границы поля
                if res_b_bord is False:  # если выходит за границы поля,
                    continue  # новая итерация, меняем точку и проверяем ее снова
                drct = random.randint(0, 1)  # выбираем рандомное направление вниз или вправо
                res_oth_sh = other_ships(num_line, num_elem, len_ship,
                                         drct)  # проверяем, будет ли сталкиваться в таком направлении с другими кораблями
                if res_oth_sh is True:  # если не сталкивается, то будем ставить корабль
                    possib = 1 # если направление не мен
                elif res_oth_sh is False:  # сталкивается в обоих направлениях, выбираем точку заново
                    possib = 0
                else:  # если вернули новое направление, в котором не сталкивается, в отличие от другого
                    possib = 1
                    drct = res_oth_sh
                if possib == 0:
                    continue  # сталкивается в обоих направлениях, выбираем точку заново
                else:
                    placing_ship(num_line, num_elem, len_ship, drct, points)  # ставим корабль, уменьшаем число кораблей
                    num_ships -= 1
            return NavalBattle.playing_field


        sh_1 = 4
        sh_2 = 3
        sh_3 = 2
        sh_4 = 1

        cicle_sh(sh_1, 1)
        cicle_sh(sh_2, 2)
        cicle_sh(sh_3, 3)
        cicle_sh(sh_4, 4)
        return NavalBattle.playing_field

player1 = NavalBattle('#')
player1.shot(6, 2)
NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 1, 0, 0, 0, 1],[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 1, 0],[1, 1, 1, 0, 0, 1, 0, 0, 1, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle.show()
player1.shot(1, 1)
player1.shot(1, 1)
NavalBattle.new_game()
print(NavalBattle.playing_field)
NavalBattle.show()


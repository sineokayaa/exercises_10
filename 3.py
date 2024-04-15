import random


class NavalBattle:
    '''
    This class represents the Naval Battle game.

    Attributes
    ----------
    - playing_field: list, A 10x10 grid representing the game playing field.
    - symb: str, Symbol for a player's move.

    Methods
    -------
    - __init__(self, symb): Initializes a NavalBattle object with a symbol.
    - __str__(self): Returns the symbol representation of the object.
    - __repr__(self): Returns the string representation of the object.
    - shot(self, x, y): Makes a shot on the playing field.
    - show(): Displays the current state of the playing field.
    - new_game(): Starts a new game by placing ships on the playing field.
    '''
    playing_field = [[0] * 10 for _ in range(10)]

    def __init__(self, symb):
        self.symb = symb

    def __str__(self):
        return f'{self.symb}'

    def __repr__(self):
        self.__str__()

    def shot(self, x, y):
        '''
        Makes a shot on the playing field.

        Parameters
        ----------
        - x: int, The x-coordinate of the shot.
        - y: int, The y-coordinate of the shot.
        '''

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
        '''
        Displays the current state of the playing field.
        '''
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
        '''
        Starts a new game by placing ships on the playing field.
        '''
        NavalBattle.playing_field = [[0] * 10 for _ in range(10)]

        def beyond_borders(num_line, num_elem, len_ship):
            '''
            Checks if placing a ship beyond the borders of the playing field.

            Parameters
            ----------
            - num_line: int, The row index.
            - num_elem: int, The column index.
            - len_ship: int, The length of the ship.

            Returns
            -------
            bool: True if the ship doesn't go beyond the borders, False otherwise.
            '''
            if num_line + len_ship > 9 and num_elem + len_ship > 9:
                return False

        def other_ships(num_line, num_elem, len_ship, dir):  # сталкиваемся с кем-то или нет
            '''
            Checks if placing a ship conflicts with other ships.

            Parameters
            ----------
            - num_line: int, The row index.
            - num_elem: int, The column index.
            - len_ship: int, The length of the ship.
            - dir: int, The direction of the ship (0 for horizontal, 1 for vertical).

            Returns
            -------
            bool: True if no conflicts with other ships, False otherwise.
            '''

            def other_dir(num_line, num_elem, len_ship, dir):
                '''
                Checks other direction for placing ship.

                Parameters
                ----------
                - num_line: int, The row index.
                - num_elem: int, The column index.
                - len_ship: int, The length of the ship.
                - dir: int, The direction of the ship (0 for horizontal, 1 for vertical).

                Returns
                -------
                bool or dir:True if no conflicts with other ships, False otherwise, dir if other direction is possible.
                '''
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
            '''
            Places a ship on the playing field.

            Parameters
            ----------
            - num_line: int, The row index.
            - num_elem: int, The column index.
            - len_ship: int, The length of the ship.
            - dir: int, The direction of the ship (0 for horizontal, 1 for vertical).
            - points: list, List of points occupied by ships.
            '''
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
            '''
            Places ships on the playing field.

            Parameters
            ----------
            - num_ships: int, The number of ships to be placed.
            - len_ship: int, The length of the ships.
            '''
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
                    possib = 1  # если направление не мен
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
NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle.show()
player1.shot(1, 1)
player1.shot(1, 1)
NavalBattle.new_game()
NavalBattle.show()
player1.shot(6, 2)

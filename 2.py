class NavalBattle:
    '''
    This class represents a naval battle game.

    Attributes
    -----------
    - playing_field: a list of lists representing the playing field.

    Attributes
    -----------
    - playing_field: list, A 10x10 grid representing the game playing field.
    - symb: str, Symbol for a player's move.

    Methods
    --------
    - shot(x, y): Mark the shot on the playing field as a hit or a miss.
    - show(): Display the current state of the playing field.
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
                Mark the shot on the playing field as a hit or a miss.

                Args:
                - x (int): the x-coordinate of the shot.
                - y (int): the y-coordinate of the shot.
                '''
        if NavalBattle.playing_field[y - 1][x - 1] == 1:
            NavalBattle.playing_field[y - 1][x - 1] = self.symb
            print('попал')
        else:
            NavalBattle.playing_field[y - 1][x - 1] = 'o'
            print('мимо')

    @staticmethod
    def show():
        '''
        Display the current state of the playing field.
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


NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                             [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
print(NavalBattle.playing_field)
player1 = NavalBattle('#')
player2 = NavalBattle('*')
NavalBattle.show()
player1.shot(6, 2)
player1.shot(6, 1)
player2.shot(6, 3)
player2.shot(6, 4)
player2.shot(6, 5)
player2.shot(3, 3)
player2.show()
player1.shot(1, 1)
NavalBattle.show()

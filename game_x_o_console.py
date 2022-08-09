lst = [str(i) for i in range (1, 10)]
dct = dict.fromkeys(lst)
lst_val = [key for key in dct.keys()]
print('Игровое поле:\n', lst_val[0], lst_val[1], lst_val[2], '\n', lst_val[3], lst_val[4], lst_val[5], '\n', lst_val[6], lst_val[7], lst_val[8])

class Game:

    def field_x(self):
        self.Fx = input('Ходят "крестики". Введите поле (1-9): ')
        if self.Fx in lst:
            if dct[self.Fx] is not None:
                print('Поле уже занято! Введите еще раз')
                self.field_x()
            dct[self.Fx] = 'X'
            print([dct['1'], dct['2'], dct['3']])
            print([dct['4'], dct['5'], dct['6']])
            print([dct['7'], dct['8'], dct['9']])
            self.win_check_x()
        else:
            print('Неверное поле! Введите еще раз')
            self.field_x()

    def field_o(self):
        self.Fo = input('Ходят "нолики". Введите поле (1-9): ')
        if self.Fo in lst:
            if dct[self.Fo] is not None:
                print('Поле уже занято! Введите еще раз')
                self.field_o()
            dct[self.Fo] = 'O'
            print([dct['1'], dct['2'], dct['3']])
            print([dct['4'], dct['5'], dct['6']])
            print([dct['7'], dct['8'], dct['9']])
            self.win_check_o()
        else:
            print('Неверное поле! Введите еще раз')
            self.field_o()

    def win_check_x(self):
        if dct['1'] == dct['2'] == dct['3'] == 'X' or \
                dct['4'] == dct['5'] == dct['6'] == 'X' or \
                dct['7'] == dct['8'] == dct['9'] == 'X' or \
                dct['1'] == dct['4'] == dct['7'] == 'X' or \
                dct['2'] == dct['5'] == dct['8'] == 'X' or \
                dct['3'] == dct['6'] == dct['9'] == 'X' or \
                dct['1'] == dct['5'] == dct['9'] == 'X' or \
                dct['3'] == dct['5'] == dct['7'] == 'X':
                print(f'Игра окончена! Выйграли "крестики"')
        elif dct['1'] is None or \
                dct['2'] is None or \
                dct['3'] is None or \
                dct['4'] is None or \
                dct['5'] is None or \
                dct['6'] is None or \
                dct['7'] is None or \
                dct['8'] is None or \
                dct['9'] is None:
            self.field_o()
        else:
            print('Ничья!')

    def win_check_o(self):
        if dct['1'] == dct['2'] == dct['3'] == 'O' or \
                dct['4'] == dct['5'] == dct['6'] == 'O' or \
                dct['7'] == dct['8'] == dct['9'] == 'O' or \
                dct['1'] == dct['4'] == dct['7'] == 'O' or \
                dct['2'] == dct['5'] == dct['8'] == 'O' or \
                dct['3'] == dct['6'] == dct['9'] == 'O' or \
                dct['1'] == dct['5'] == dct['9'] == 'O' or \
                dct['3'] == dct['5'] == dct['7'] == 'O':
                print(f'Игра окончена! Выйграли "нолики"')
        elif dct['1'] is None or \
                dct['2'] is None or \
                dct['3'] is None or \
                dct['4'] is None or \
                dct['5'] is None or \
                dct['6'] is None or \
                dct['7'] is None or \
                dct['8'] is None or \
                dct['9'] is None:
            self.field_x()
        else:
            print('Ничья!')

if __name__ == '__main__':
    Cross_zeroes = Game()
    Cross_zeroes.field_x()

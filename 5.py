import re  # модуль для операций с регулярными выражениями


class RomanNumber:
    roman_symbols = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
                     'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

    def __init__(self, ptr):
        if isinstance(ptr, int):
            if RomanNumber.is_int(ptr):  # если число может быть римским числом
                self.int_value = ptr
                self.rom_value = RomanNumber.roman_number(self)
            else:  # не может быть римским числом
                self.int_value = None
                self.rom_value = None
                print('ошибка')
        elif isinstance(ptr, str):  # если число-строка,т.е. может быть римским числом
            if RomanNumber.is_roman(ptr):  # если римское число
                self.rom_value = ptr
                self.int_value = RomanNumber.decimal_number(self)
            else:
                self.rom_value = None
                self.int_value = None
                print('ошибка')
        elif ptr != int(ptr):
            self.rom_value = None
            self.int_value = None
            print('ошибка')

    def __str__(self):
        if self.rom_value is None:
            return 'None'
        return f'{self.rom_value}'

    def __repr__(self):
        return str(self.rom_value)

    @staticmethod
    def is_int(value):
        if value < 0 or value > 3999:
            return False
        return True

    @staticmethod
    def is_roman(
            value):  # compile который выполняет компиляцию регулярного выражения и возвращает его в виде экземпляра класса Pattern.
        ptr = re.compile('^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$')
        if re.match(ptr, value):  # с начала строки сверяет строку с шаблоном птр
            return True
        return False

    '''обе функции возвращают объекты регулярного выражения'''

    def decimal_number(self):
        decimal_number = 0
        for i in range(len(self.rom_value)):
            if (i < len(self.rom_value) - 1 and RomanNumber.roman_symbols[self.rom_value[i]] <
                    RomanNumber.roman_symbols[self.rom_value[i + 1]]):
                decimal_number -= RomanNumber.roman_symbols[self.rom_value[i]]
            else:
                decimal_number += RomanNumber.roman_symbols[self.rom_value[i]]
        return decimal_number

    def roman_number(self):
        if self.int_value is None:
            return 'ошибка'
        num = self.int_value
        roman_num = ''
        if num // 1000 != 0:
            roman_num += 'M' * (num // 1000)
        num = num % 1000
        if num // 100 != 0:
            if 1 <= num // 100 <= 3:
                roman_num += 'C' * (num // 100)
            elif num // 100 == 4:
                roman_num += 'CD'
            elif num // 100 == 5:
                roman_num += 'D'
            elif 5 < num // 100 < 9:
                roman_num += 'D' + 'C' * ((num // 100) - 5)
            elif num // 100 == 9:
                roman_num += 'CM'
        num = num % 100
        if num // 10 != 0:
            if 1 <= num // 10 <= 3:
                roman_num += 'X' * (num // 10)
            elif num // 10 == 4:
                roman_num += 'LX'
            elif num // 10 == 5:
                roman_num += 'L'
            elif 6 <= num // 10 <= 8:
                roman_num += 'L' + 'X' * ((num // 10) - 5)
            elif num // 10 == 9:
                roman_num += 'XC'
        num %= 10
        if num != 0:
            if 1 <= num <= 3:
                roman_num += 'I' * num
            elif num == 4:
                roman_num += 'IV'
            elif num == 5:
                roman_num += 'V'
            elif 6 <= num <= 8:
                roman_num += 'V' + 'I' * (num - 5)
            elif num == 9:
                roman_num += 'IX'
        return roman_num


num_1 = RomanNumber(3999)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)
num_2 = RomanNumber(5690)
print(num_2.int_value)
num_3 = RomanNumber('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)
print(RomanNumber.is_int(-614))
print(RomanNumber.is_int(3758))

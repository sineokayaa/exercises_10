import re  # модуль для операций с регулярными выражениями


class RomanNumber:
    '''
    This class represents a Roman number.

    Attributes
    ----------
    - roman_symbols: dict, A dictionary mapping Roman symbols to their decimal values.
    - int_value: int, The integer value of the Roman number.
    - rom_value: str, The Roman numeral string value.

    Methods
    -------
    - __init__(self, ptr): Initializes a RomanNumber object with a Roman numeral or an integer.
    - __str__(self): Returns the string representation of the Roman numeral.
    - __repr__(self): Returns the string representation of the Roman numeral.
    - is_int(value): Checks if the input value is a valid positive integer within the range [1, 3999].
    - is_roman(value): Checks if the input value is a valid Roman numeral.
    - decimal_number(self): Converts the Roman numeral to its decimal equivalent.
    - roman_number(self): Converts the integer to its Roman numeral equivalent.
    - other_is_str(other): Converts the other parameter to a RomanNumber object if it's a string.
    - if_mistake(param): Checks if the input parameter represents an error.
    - __add__(self, other): Overloaded method for addition operation.
    - __sub__(self, other): Overloaded method for subtraction operation.
    - __truediv__(self, other): Overloaded method for true division operation.
    - __floordiv__(self, other): Overloaded method for floor division operation.
    - __mul__(self, other): Overloaded method for multiplication operation.
    - __pow__(self, other): Overloaded method for exponentiation operation.
    - __mod__(self, other): Overloaded method for modulus operation.
    '''
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
        '''
        Checks if the input value is a valid positive integer within the range [1, 3999].

        Parameters
        ----------
        - value: int, The input value to be checked.

        Returns
        -------
        bool: True if the value is a valid positive integer, False otherwise.
        '''
        if value <= 0 or value > 3999:
            return False
        return True

    @staticmethod
    def is_roman(
            value):  # compile который выполняет компиляцию регулярного выражения и возвращает его в виде экземпляра класса Pattern.
        '''
        Checks if the input value is a valid Roman numeral.

        Parameters
        ----------
        - value: str, The input value to be checked.

        Returns
        -------
        bool: True if the value is a valid Roman numeral, False otherwise.
        '''
        ptr = re.compile('^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$')
        if re.match(ptr, value):  # с начала строки сверяет строку с шаблоном птр
            return True
        return False

    # Both functions return objects of regular expression.

    def decimal_number(self):
        '''
        Converts the Roman numeral to its decimal equivalent.

        Returns
        -------
        int: The decimal equivalent of the Roman numeral.
        '''
        decimal_number = 0
        for i in range(len(self.rom_value)):
            if (i < len(self.rom_value) - 1 and RomanNumber.roman_symbols[self.rom_value[i]] <
                    RomanNumber.roman_symbols[self.rom_value[i + 1]]):
                decimal_number -= RomanNumber.roman_symbols[self.rom_value[i]]
            else:
                decimal_number += RomanNumber.roman_symbols[self.rom_value[i]]
        return decimal_number

    def roman_number(self):
        '''
        Converts the integer to its Roman numeral equivalent.

        Returns
        -------
        str: The Roman numeral equivalent of the integer.
        '''
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

    @staticmethod
    def other_is_str(other):
        '''
        Converts the other parameter to a RomanNumber object if it's a string.

        Parameters
        ----------
        - other: str, The input value to be converted to a RomanNumber object.

        Returns
        -------
        RomanNumber: The RomanNumber object representing the other parameter.
        '''
        other.rom_value = RomanNumber(other)
        other.int_value = RomanNumber(other)
        return other

    @staticmethod
    def if_mistake(param):
        '''
        Checks if the input parameter represents an error.

        Parameters
        ----------
        - param: str, The parameter to be checked.

        Returns
        -------
        bool: True if the parameter represents an error, False otherwise.
        '''
        if param == 'ошибка':
            return True
        return False

    def __add__(self, other):
        '''
        Overloaded method for addition operation.

        Parameters
        ----------
        - other: RomanNumber or str, The other operand to be added.

        Returns
        -------
        RomanNumber or str: The result of the addition operation.
        '''
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value + other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        res = RomanNumber(res)
        res = RomanNumber.roman_number(res)
        return RomanNumber(res)

    def __sub__(self, other):
        '''
        Overloaded method for subtraction operation.

        Parameters
        ----------
        - other: RomanNumber or str, The other operand to be subtracted.

        Returns
        -------
        RomanNumber or str: The result of the subtraction operation.
        '''
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value - other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        res = RomanNumber(res)
        res = RomanNumber.roman_number(res)
        return RomanNumber(res)

    def __truediv__(self, other):
        '''
        Overloaded method for true division operation.

        Parameters
        ----------
        - other: RomanNumber or str, The other operand to divide by.

        Returns
        -------
        RomanNumber or str: The result of the true division operation.
        '''
        if RomanNumber.if_mistake(self):
            return 'оsшибка'
        elif RomanNumber.if_mistake(other):
            return 'sssssss ошибка'
        if other.rom_value is None:
            return 'ssss ошибка'
        if type(other) == str:
            RomanNumber.other_is_str(other)
        res = self.int_value / other.int_value
        if not RomanNumber.is_int(res) or res != int(res):
            res_new = RomanNumber(res)
            return res_new
        res = int(res)
        res = RomanNumber(res)
        res = RomanNumber.roman_number(res)
        return RomanNumber(res)

    def __floordiv__(self, other):
        '''
        Overloaded method for floor division operation.

        Parameters
        ----------
        - other: RomanNumber or str, The other operand to divide by.

        Returns
        -------
        RomanNumber or str: The result of the floor division operation.
        '''
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value // other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        res = int(res)
        res = RomanNumber(res)
        res = RomanNumber.roman_number(res)
        return RomanNumber(res)

    def __mul__(self, other):
        '''
        Overloaded method for multiplication operation.

        Parameters
        ----------
        - other: RomanNumber or str, The other operand to multiply by.

        Returns
        -------
        RomanNumber or str: The result of the multiplication operation.
        '''
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value * other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        res = RomanNumber(res)
        res = RomanNumber.roman_number(res)
        return RomanNumber(res)

    def __pow__(self, other, modulo=None):
        '''
        Overloaded method for exponentiation operation.

        Parameters
        ----------
        - other: RomanNumber or str, The other operand to raise to the power of.

        Returns
        -------
        RomanNumber or str: The result of the exponentiation operation.

        '''
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value ** other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        res = RomanNumber(res)
        res = RomanNumber.roman_number(res)
        return RomanNumber(res)

    def __mod__(self, other):
        '''
        Overloaded method for modulus operation.

        Parameters
        ----------
        - other: RomanNumber or str, The other operand to take modulus with.

        Returns
        -------
        RomanNumber or str: The result of the modulus operation.
        '''
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value % other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        res = RomanNumber(res)
        res = RomanNumber.roman_number(res)
        return RomanNumber(res)

    '''def __iadd__(self, other):
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value + other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        self.int_value = res
        self.rom_value = RomanNumber(res)
        return self.rom_value

    def __ifloordiv__(self, other):
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value // other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        res = int(res)
        self.int_value = res
        self.rom_value = RomanNumber(res)
        return self.rom_value

    def __imod__(self, other):
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value % other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        self.int_value = res
        self.rom_value = RomanNumber(res)
        return self.rom_value

    def __imul__(self, other):
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value * other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        self.int_value = res
        self.rom_value = RomanNumber(res)
        return self.rom_value

    def __ipow__(self, other):
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value ** other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        self.int_value = res
        self.rom_value = RomanNumber(res)
        return self.rom_value

    def __isub__(self, other):
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value - other.int_value
        if not RomanNumber.is_int(res):
            return 'ошибка'
        self.int_value = res
        self.rom_value = RomanNumber(res)
        return self.rom_value

    def __itruediv__(self, other):
        if RomanNumber.if_mistake(self):
            return 'ошибка'
        elif RomanNumber.if_mistake(other):
            return 'ошибка'
        if type(other) == str:
            RomanNumber.other_is_str(other)
        if other.rom_value is None:
            return 'ошибка'
        res = self.int_value / other.int_value
        if not RomanNumber.is_int(res) or res != int(res):
            res_new = RomanNumber(res)
            return res_new
        res = int(res)
        self.int_value = res
        self.rom_value = RomanNumber(res)
        return self.rom_value'''


a = RomanNumber('XI')
b = RomanNumber('VII')
c = a + b
print(c)
d = RomanNumber('XII')
print(c - d)
e = RomanNumber('XXXIV')
f = e * a
print(f)
print(f / RomanNumber('II'))
g = f / b
print(g.rom_value)
print(f // b)
print(f % b)
print(RomanNumber('II') ** RomanNumber('X'))
a -= b
print(a)
b += RomanNumber('XX')
print(b)
b /= RomanNumber('III')
print(b)
b *= a
print(b)
b /= RomanNumber('X')
print(b)
e //= RomanNumber('X')
print(e)
e %= RomanNumber('II')
print(e)

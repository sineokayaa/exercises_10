import re  # модуль для операций с регулярными выражениями


class RomanNumber:
    '''
    This class represents a Roman number.

    Attributes
    ----------
    - roman_symbols: dict, A dictionary mapping Roman symbols to their decimal values.

    Methods
    -------
    - __init__(self, str): Initializes a RomanNumber object with a Roman numeral string.
    - __str__(self): Returns the string representation of the Roman numeral.
    - __repr__(self): Returns the string representation of the Roman numeral.
    - is_roman(value): Checks if the input value is a valid Roman numeral.
    - decimal_number(self): Converts the Roman numeral to its decimal equivalent.
    '''
    roman_symbols = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
                     'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

    def __init__(self, str):
        if RomanNumber.is_roman(str):
            self.rom_value = str
        else:
            self.rom_value = None
            print('ошибка')

    def __str__(self):
        if self.rom_value is None:
            return 'None'
        return f'{self.rom_value}'

    def __repr__(self):
        return str(self.rom_value)

    @staticmethod
    def is_roman(value):
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
        if re.match(ptr, value):
            return True
        return False

    def decimal_number(self):
        '''
        Converts the Roman numeral to its decimal equivalent.

        Returns
        -------
        int: The decimal equivalent of the Roman numeral.
        '''
        decimal_number = 0
        for i in range(len(self.rom_value)):
            if i < len(self.rom_value) - 1 and RomanNumber.roman_symbols[self.rom_value[i]] < RomanNumber.roman_symbols[
                self.rom_value[i + 1]]:
                decimal_number -= RomanNumber.roman_symbols[self.rom_value[i]]
            else:
                decimal_number += RomanNumber.roman_symbols[self.rom_value[i]]
        return decimal_number


num_1 = RomanNumber('MMMCMXCIX')
print(num_1.rom_value)
print(num_1.decimal_number())
print(num_1)
num_2 = RomanNumber('IIII')
print(num_2.rom_value)
num_3 = RomanNumber('XXIV')
print(num_3.decimal_number())
num_4 = RomanNumber('QER2')
nums = []
nums.append(num_1)
nums.append(num_2)
nums.append(num_3)
nums.append(num_4)
print(nums)
print(RomanNumber.is_roman('MMMCMLXXXVI'))
print(RomanNumber.is_roman('MMМMMLXXXVI'))

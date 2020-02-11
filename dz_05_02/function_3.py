print('Homework 6\n')
print('Function 3\n')
# Создать функцию, которая прибавляет элементы числа между собой.
# Например, есть число 123. Попав в нашу функцию, должно произойти следующее:
# 1 + 2 + 3 = 6.
# Результат суммирования - в консоль.

x = input('Enter the number to sum it: ')


def summa(y):
    for char in x:
        y += int(char)
    print('The sum of chars in', x, 'is', y)


summa(0)

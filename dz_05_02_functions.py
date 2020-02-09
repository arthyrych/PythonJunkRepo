print('Homework 6\n')

print('Function 1\n')
# Создать функцию, которая:
# Принимает последовательность чисел
# Превращает ее в список
# Выводит первый и последний элемент списка
my_list = []


def first_last():
    while True:
        x = input('Enter a number to add to the list or enter EXIT to exit:\n')
        if x == 'EXIT':
            break
        else:
            my_list.append(x)


first_last()
print('You\'ve created this list:', my_list)
print('The first value in the list is', my_list[0], 'and the last value in the list is', my_list[-1])

print('\nFunction 2\n')
# Найдите три ключа с самыми высокими значениями в словаре
# my_dict = {'a':645, 'b':3987, 'c': 093,'d':111, 'e':646, 'f': 20}

print('\nFunction 3\n')
# Создать функцию, которая прибавляет элементы числа между собой.
# Например, есть число 123. Попав в нашу функцию, должно произойти следующее:
# 1 + 2 + 3 = 6.
# Результат суммирования - в консоль.

print('\nFunction 4\n')
# Нужно написать функцию, которая будет считать сколько раз символ встречается в строке.
# Например, в строке "Денис даёт нам классные задачки, которые помогут нам найти лучшую работу!"
# символ "е" встречается 3 раза.

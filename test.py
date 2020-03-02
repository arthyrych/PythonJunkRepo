# 1) Напишите программу, вычисляющую среднее арифметическое двух чисел.


def average():
    print('Task 1. Getting an average.')
    first = int(input('Enter the first number: '))
    second = int(input('Enter the second number: '))
    print('The average from', first, 'and', second, 'is', (first + second) / 2)


average()

# 2) Введите три числа и выведите на экран значения суммы и произведения этих чисел.


def user_sum():
    print('\nTask 2. Getting sum and multiplication.')
    first = int(input('Enter the first number: '))
    second = int(input('Enter the second number: '))
    third = int(input('Enter the third number: '))
    print('The sum is', first, '+', second, '+', third, '=', first + second + third,)
    print('The multiplication is', first, '*', second, '*', third, '=', first * second * third)


user_sum()

# 3) Напишите простой конвертер валют (без возможности динамического выбора валют пользователем).
# Валюты заданы хардкодом и не изменяются. Тип валют на выбор программиста.
# тут обычная арифметика но можешь задать это что бы каждое задание это было новая функция


def money():
    print('\nTask 3. Money exchange UAH to USD.')
    uah = int(input('Enter the amount in UAH (Ukrainian Hryvnya): '))
    usd = round(uah / 24.1, 2)
    print(uah, 'UAH in USD (US dollars) will be', usd)


money()

# Сделай функцию которая вызывает у себя в теле бесконечный цикл в котором пользователь
# вводит число и это число проверяется на четность и сообщает об этом пользователю при
# этом что бы программа не закрывалась, а закрывалась только тогда когда при вводе числа ты как бы ввел пустую
# строку(просто нажав Enter)


def even_or_odd():
    print('\nTask 4. Is your number even or odd?')
    while True:
        x = input('Enter the number or press ENTER to close it: ')
        if not x:
            print('Program is closed.')
            break
        elif int(x) % 2 == 0:
            print(x, 'is an even number.')
        else:
            print(x, 'is an odd number.')


even_or_odd()

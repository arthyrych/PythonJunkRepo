# Написать калькулятор, который принимает 3 значение
# Первое значение  и второе значение цифры
# Третье значение это символ + (добавление) или - (отнимание) или * (Умножение) или / (Деление)
# После третьего значения должно произойти арифметическая операция первого и второго значения


def calc(first, second, action):
    final = 0
    if action == '+':
        final = first + second
    elif action == '-':
        final = first - second
    elif action == '*':
        final = first * second
    elif action == '/':
        final = first / second
    else:
        print('ERROR! Something went wrong. Please try again.')
    print('The result is:', first, action, second, '=', final)


print('This is our calculator!')
calc(int(input('Enter the first number: ')),
     int(input('Enter the second number: ')),
     input('Enter the action (+ or - or * or /): '))

# Написать функцию которая будет подсчитывать сколько четных и нечетных чисел в диапазоне который нужно ввести
# Также найдите сумму всех четных и сумму всех нечетных чисел отдельно


def new_fun(begin, end):
    print('Hello')


new_fun(int(input('Enter the number to count from: ')),
        int(input('Enter the number to count till: ')))

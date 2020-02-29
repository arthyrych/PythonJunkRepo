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
    chet = 0
    nechet = 0
    sum_chet = 0
    sum_nechet = 0
    while True:
        if begin > end:
            break
        else:
            if begin % 2 == 0:
                sum_chet += begin
                chet += 1
            else:
                sum_nechet += begin
                nechet += 1
        begin += 1
    print('The amount of even numbers between them is:', chet)
    print('The amount of odd numbers between them is:', nechet)
    print('The sum of even numbers between them is:', sum_chet)
    print('The sum of odd numbers between them is:', sum_nechet)


print('Let\'s count the amount of even and odd numbers! Also we will sum their values!')
new_fun(int(input('Enter the number to count from: ')),
        int(input('Enter the number to count till: ')))

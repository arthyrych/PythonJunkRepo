def calc():
    print('This is our calculator!')
    first = int(input('Enter the first number: '))
    second = int(input('Enter the second number: '))
    action = input('Enter the action (+ or - or * or /): ')
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

calc()


def new_fun():
    print('Let\'s count the amount of even and odd numbers! Also we will sum their values!')
    begin = int(input('Enter the number to count from: '))
    end = int(input('Enter the number to count till: '))
    chet = 0
    nechet = 0
    sum_chet = 0
    sum_nechet = 0
    while begin <= end:
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

new_fun()

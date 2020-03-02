def greeting():
    name = input('Enter your name: ')
    print('Hello,', name, '!')


def new_fun():
    print('Let\'s count the amount of even and odd numbers! Also we will sum their values!')
    begin = int(input('Enter the number to count from: '))
    end = int(input('Enter the number to count till: '))
    chet = 0
    nechet = 0
    sum_chet = 0
    sum_nechet = 0
    while begin < end:
        if begin % 2 == 0:
            sum_chet += begin
            chet += 1
        else:
            sum_nechet += begin
            nechet += 1
        begin += 1
    print('The amount of even numbers between them is', chet, 'and sum of even numbers is', sum_chet)
    print('The amount of odd numbers between them is', nechet, 'and sum of odd numbers is', sum_nechet)


def greeting(name):
    print("Hello, " + name)


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
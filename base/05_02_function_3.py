def summ():
    print('Function 3')
    x = input('Enter the number to sum it: ')
    y = 0
    for char in x:
        y += int(char)
    print('The sum of chars in', x, 'is', y)


summ()

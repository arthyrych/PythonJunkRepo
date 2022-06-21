def first_last():
    print('Function 1')
    my_list = []
    while True:
        x = input('Enter a number to add to the list or enter EXIT to exit: ')
        if x == 'EXIT':
            break
        else:
            my_list.append(x)
    print('You\'ve created this list:', my_list)
    print('The first value in the list is', my_list[0], 'and the last value in the list is', my_list[-1])


first_last()

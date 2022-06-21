def set_user_list_1():
    print('Function 1')
    user_list = []
    list_length = int(input('Enter the length of the list: '))
    arg_length = int(input('Enter the MAX value of an arg in the list: '))
    for i in range(list_length):
        print("Enter the value of ", i + 1, " element: ")
        while True:
            arg = input()
            if not arg:
                print("Error. Enter the value from ", 0, " to ", arg_length)
                continue
            if int(arg) > arg_length:
                print("Error. Enter the value from ", 0, " to ", arg_length)
                continue
            else:
                user_list.append(arg)
                print("Accepted!")
                break
    print(user_list)

set_user_list_1()


def set_user_list_2():
    print('Function 2')
    user_list = []
    while True:
        user_list_length = int(input("Enter the length of the list: "))
        if not user_list_length:
            print("Enter the value > 0")
            continue
        elif user_list_length > 0:
            print("Accepted!")
            break
        else:
            continue
    while True:
        user_list_arg_length = int(input("Enter the MAX arg of the element in the list: "))
        if not user_list_arg_length:
            print("Enter the value > 0")
            continue
        elif user_list_length > 0:
            print("Accepted!")
            break
        else:
            continue
    for i in range(user_list_length):
        print("Enter the value of ", i + 1, " element: ")
        while True:
            arg = input()
            if not arg:
                print("Error. Enter the value from ", 0, " to ", user_list_arg_length)
                continue
            if int(arg) > user_list_arg_length:
                print("Error. Enter the value from ", 0, " to ", user_list_arg_length)
                continue
            else:
                user_list.append(arg)
                print("Accepted!")
                break
    print("Checking the received data and giving back the ones which are bigger than 7: ")
    for i in range(len(user_list)):
        if int(user_list[i]) > 7:
            print("The element of the list", i + 1, "is having value", user_list[i], "and bigger than 7")


set_user_list_2()


def set_user_list_3():
    print('Function 3')
    user_list = []
    user_list_2 = []
    user_list_3 = []
    length_user_list = int(input('Enter the length of the first list: '))
    length_user_list_arg = int(input('Enter the MAX value of an arg in the first list: '))
    for i in range(length_user_list):
        print("Enter the value of", i + 1, "element:")
        while True:
            arg = input()
            if not arg:
                print("Error. Enter the value from", 0, "to", length_user_list_arg)
                continue
            if int(arg) > length_user_list_arg:
                print("Error. Enter the value from", 0, "to", length_user_list_arg)
                continue
            else:
                user_list.append(arg)
                print("Accepted!")
                break
    print('The first list is:', user_list)
    length_user_list_2 = int(input('Enter the length of the second list: '))
    length_user_list_arg_2 = int(input('Enter the MAX value of an arg in the second list: '))
    for i in range(length_user_list_2):
        print("Enter the value of", i + 1, "element:")
        while True:
            arg = input()
            if not arg:
                print("Error. Enter the value from", 0, "to", length_user_list_arg_2)
                continue
            if int(arg) > length_user_list_arg_2:
                print("Error. Enter the value from", 0, "to", length_user_list_arg_2)
                continue
            else:
                user_list_2.append(arg)
                print("Accepted!")
                break
    print('The second list is:', user_list_2)
    for x in user_list:
        if x in user_list_2:
            user_list_3.append(x)
    print('Here is a new list with the same values:', user_list_3)


set_user_list_3()

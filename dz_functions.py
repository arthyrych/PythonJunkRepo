print('Homework 4\n')

print('Function 1\n')
# Необходимо создать функцию, которая будет принимать два аргумента от
# пользователя и на основании этих аргументов создавать список.
# Первый аргумент - определяет длину списка
# Второй аргумент - определяет максимально возможное значение элемента списка

user_list = []
LENGTH_USER_LIST = 'Enter the length of the list: '
LENGTH_USER_LIST_ARG = 'Enter the MAX value of an arg in the list: '


def set_user_list(list_length, arg_length):
    for i in range(list_length):
        print("Enter the value of ", i, " element: ")
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


set_user_list(int(input(LENGTH_USER_LIST)), int(input(LENGTH_USER_LIST_ARG)))
print(user_list)

print('\nFunction 2\n')
# Необходимо написать функцию, которая будет принимать два аргумента по тому
# же принципу что и в предыдущей
# после чего анализировать список и выводить в консоль все элементы списка,
# которые больше 7.

user_list = []
user_list_length = 0
user_list_arg_length = 0


def set_user_list(list_length, arg_length):
    for i in range(list_length):
        print("Enter the value of ", i, " element: ")
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

    print("Checking the received data and giving back the ones which are bigger than 7: ")

    for i in range(len(user_list)):
        if int(user_list[i]) > 7:
            print("The element of the list ", i, " is having value ", user_list[i], " and bigger than 7")


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

set_user_list(user_list_length, user_list_arg_length)

print('\nFunction 3\n')
# Необходимо написать функцию, которая будет сравнивать два списка
# после чего анализировать и выводить одинаковые значения

user_list = []
user_list_2 = []
LENGTH_USER_LIST = 'Enter the length of the first list:'
LENGTH_USER_LIST_ARG = 'Enter the MAX value of an arg in the first list:'
LENGTH_USER_LIST_2 = 'Enter the length of the second list:'
LENGTH_USER_LIST_ARG_2 = 'Enter the MAX value of an arg in the second list:'


def set_user_list(list_length, arg_length):
    for i in range(list_length):
        print("Enter the value of ", i, " element: ")
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


def set_user_list_2(list_length, arg_length):
    for i in range(list_length):
        print("Enter the value of ", i, " element: ")
        while True:
            arg = input()
            if not arg:
                print("Error. Enter the value from ", 0, " to ", arg_length)
                continue
            if int(arg) > arg_length:
                print("Error. Enter the value from ", 0, " to ", arg_length)
                continue
            else:
                user_list_2.append(arg)
                print("Accepted!")
                break


def check_it():
    for x in user_list:
        if x in user_list_2:
            print('The following value is in both lists:', x)


set_user_list(int(input(LENGTH_USER_LIST)), int(input(LENGTH_USER_LIST_ARG)))
print('\nThe first list is:', user_list, '\n')
set_user_list_2(int(input(LENGTH_USER_LIST_2)), int(input(LENGTH_USER_LIST_ARG_2)))
print('\nThe second list is:', user_list_2, '\n')
check_it()

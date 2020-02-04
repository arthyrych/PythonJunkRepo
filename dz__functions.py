print('Homework 4\n')

print('Function 1\n')
# Необходимо создать функцию, которая будет принимать два аргумента от
# пользователя и на основании этих аргументов создавать список.
#
# Первый аргумент - определяет длину списка
# Второй аргумент - определяет максимально возможное значение элемента списка


def set_user_list(list_length, arg_length):
    print("--------------------------------------")

    for i in range(list_length):
        print("Введите значение ", i, " елемента: ")
        while True:
            arg = input()
            if not arg:
                print("Ошибка. Введите число от ", 0, " до ", arg_length)
                continue
            if int(arg) > arg_length:
                print("Ошибка. Введите число от ", 0, " до ", arg_length)
                continue
            else:
                user_list.append(arg)
                print("OK")
                break

    print("--------------------------------------")


user_list = []
LENGTH_USER_LIST = 'Введите длину списка: '
LENGTH_USER_LIST_ARG = 'Введите максимальное значение элемента списка: '

set_user_list(int(input(LENGTH_USER_LIST)), int(input(LENGTH_USER_LIST_ARG)))


# Необходимо написать функцию, которая будет принимать два аргумента по тому
# # же принципу что и в предыдущей
# после чего анализировать список и выводить в консоль все элементы списка,
# которые больше 7.


def set_user_list(list_length, arg_length):
    print("--------------------------------------")

    for i in range(list_length):
        print("Введите значение ", i, " елемента: ")
        while True:
            arg = input()
            if not arg:
                print("Ошибка. Введите число от ", 0, " до ", arg_length)
                continue
            if int(arg) > arg_length:
                print("Ошибка. Введите число от ", 0, " до ", arg_length)
                continue
            else:
                user_list.append(arg)
                print("OK")
                break

    print("--------------------------------------")
    print("Анализируем список и выводим элементы списка, которые больше 7:")

    for i in range(len(user_list)):
        if int(user_list[i]) > 7:
            print("Элемент списка ", i, " имеет значение ", user_list[i], " больше 7")

    print("--------------------------------------")


user_list = []
user_list_length = 0
user_list_arg_length = 0

while True:
    user_list_length = int(input("Введите длину списка: "))
    if not user_list_length:
        print("Введите значение > 0")
        continue
    elif user_list_length > 0:
        print("OK")
        break
    else:
        continue

while True:
    user_list_arg_length = int(input("Введите максимальное значение елемента: "))
    if not user_list_arg_length:
        print("Введите значение > 0")
        continue
    elif user_list_length > 0:
        print("OK")
        break
    else:
        continue

set_user_list(user_list_length, user_list_arg_length)


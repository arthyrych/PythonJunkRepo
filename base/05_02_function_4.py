# Нужно написать функцию, которая будет считать сколько раз символ встречается в строке.
# Например, в строке "Денис даёт нам классные задачки, которые помогут нам найти лучшую работу!"
# символ "е" встречается 3 раза.
print('Function 4')


def amount():
    our_str = input('Enter a string to sum \'a\' symbols in it: ')
    y = 0
    for char in our_str:
        if char == str('a'):
            y += 1
    if y > 0:
        print('The sum of \'a\' in string', '\'', our_str, '\'', 'is', y)
    else:
        print('No \'a\' in string \'', our_str, '\'')


amount()

# Нужно написать функцию, которая будет считать сколько раз символ встречается в строке.
# Например, в строке "Денис даёт нам классные задачки, которые помогут нам найти лучшую работу!"
# символ "е" встречается 3 раза.


def amount_mega():
    our_dict = {}
    sentence = input('Enter a sentence to count it\'s symbols in it: ')
    for char in sentence:
        symbol_value = 1
        if char in our_dict:
            symbol_value = our_dict[char] + 1
        our_dict[char] = symbol_value
    print(our_dict)


amount_mega()

print('Homework 6\n')
print('\nFunction 4\n')
# Нужно написать функцию, которая будет считать сколько раз символ встречается в строке.
# Например, в строке "Денис даёт нам классные задачки, которые помогут нам найти лучшую работу!"
# символ "е" встречается 3 раза.


def amount(our_str):
    y = 0
    for char in our_str:
        if char == str('a'):
            y += 1
    if y > 0:
        print('The sum of \'a\' in string', '\'', our_str, '\'', 'is', y)
    else:
        print('No \'a\' in string \'', our_str, '\'')


amount(input('Enter a string to sum \'a\' symbols in it: '))

# Нужно написать функцию, которая будет считать сколько раз символ встречается в строке.
# Например, в строке "Денис даёт нам классные задачки, которые помогут нам найти лучшую работу!"
# символ "е" встречается 3 раза.


def amount_mega(sentence):
    our_shit = {}
    for char in sentence:
        symbol_value = 1
        if char in our_shit:
            symbol_value = our_shit[char] + 1
        our_shit[char] = symbol_value
    print(our_shit)


amount_mega(input('Enter a sentence to count it\'s symbols in it: '))

print('Function 2')

my_dict = {'a': 645, 'b': 3987, 'c': 93, 'd': 111, 'e': 646, 'f': 20}
x = my_dict['a']
for key, value in my_dict.items():
    if value > x:
        x = value
y = my_dict['a']
for key, value in my_dict.items():
    if value > y and value < x:
        y = value
z = my_dict['a']
for key, value in my_dict.items():
    if value > z and value < x and value < y:
        z = value
print(x, y, z)

my_dict = {'a': 645, 'b': 3987, 'c': 93, 'd': 111, 'e': 646, 'f': 20}
new_my_dict = []
for a_index in range(3):
    biggest_number = 0

    for b_value in my_dict.values():
        if b_value in new_my_dict:
            continue
        if b_value > biggest_number:
            biggest_number = b_value
    new_my_dict.append(biggest_number)

for g in new_my_dict:
    print(g)
    
my_dict = {'a': 645, 'b': 3987, 'c': 93, 'd': 111, 'e': 646, 'f': 20}
new_my_dict = {}
for a_index in range(3):
    biggest_key = ''
    biggest_value = 0
    for b_key in my_dict.keys():
        if b_key in new_my_dict:
            continue
        if my_dict[b_key] > biggest_value:
            biggest_key = b_key
            biggest_value = my_dict[b_key]

    new_my_dict[biggest_key] = biggest_value

for g in new_my_dict:
    print(g, new_my_dict[g])

print('Homework 3\n')
# print('Task 1 with FOR:')
print('\nTask 2 with WHILE:')
print('\nEnter A, B, C each one from the new line and press ENTER')
A = input()
B = input()
C = input()
print(A, B, C)
while int(A) <= int(B):
    print('The value is ' + str(A) + '! Still not yet!')
    A = int(A) + int(C)
    if int(A) > int(B):
        print('Finally!' + ' Final ' + str(A) + '!')

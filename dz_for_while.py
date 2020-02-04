print('Homework 3\n')
# print('Task 1 with FOR:')
print('\nTask 2 with WHILE:')
print('\nEnter A, B, C each one from the new line and press ENTER')
A = int(input())
B = int(input())
C = int(input())
print(A, B, C)
while A <= B:
    print('The value is ' + str(A) + '! Still not yet!')
    A = A + C
    if A > B:
        print('Finally!' + ' Final ' + str(A) + '!')

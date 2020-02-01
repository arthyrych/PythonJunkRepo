print('Homework 3\n')

print('Task 1 with FOR:')
print('\nEnter A, B, C each one from the new line and press ENTER')
A = input()
B = input()
C = input()
print(A, B, C)
if int(A) > int(B):
    print('Svershilos!')
elif int(B) > int(A):
    print('Da nu!')
elif int(A) == int(B):
    print('A esli tak?')
    A = int(A) + int(C)
    B = int(B) - int(C)
    if int(A) > int(B):
     print('Svershilos!')
    elif int(B) > int(A):
     print('Da nu!')

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

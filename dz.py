print('Homework 3\n')

print('Task 1 with FOR:')
print('\nEnter A, B, C each one from the new line and press ENTER')
A = input()
B = input()
C = input()
print(A, B, C)
if A > B:
    print('Svershilos!')
elif B > A:
    print('Da nu!')
elif A == B:
    print('A esli tak?')
    A = int(A) + int(C)
    B = int(B) - int(C)
    if A > B:
     print('Svershilos!')
    elif B > A:
     print('Da nu!')

print('\nTask 2 with WHILE:')



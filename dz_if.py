print('Homework 3\n')

print('Fill in A, B, C (each one from the new line and press Enter)')
A = input()
B = input()
C = input()
print(A, B, C)
if int(A) > int(B):
    print('Svershilos!')
elif int(B) > int(A):
    print('Da nu!')
else:
    print('A esli tak?')
    A = int(A) + int(C)
    B = int(B) - int(C)
    if int(A) > int(B):
        print('Svershilos!')
    else:
        print('Da nu!')
print('Happy end!')

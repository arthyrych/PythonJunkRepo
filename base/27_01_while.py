A = int(input('Enter A: '))
B = int(input('Enter B: '))
C = int(input('Enter C: '))
print(A, B, C)
while A <= B:
    print('The value is ' + str(A) + '! Still not yet!')
    A += C
    if A > B:
        print('Finally!' + ' Final ' + str(A) + '!')

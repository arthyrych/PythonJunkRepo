print('Fill in A, B, C (each one from the new line and press Enter)')
A = input()
B = input()
C = input()
print(A, B, C)
if A > B:
    print('Svershilos!')
    if B > A:
        print('Da nu!')
        if A == B:
            print('A esli tak?')
            x = A + C
            y = B - C
            if x > y:
                print('Svershilos!')
                if y > x:
                    print('Da nu!')
print('Happy end!')
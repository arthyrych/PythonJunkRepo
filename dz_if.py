print('Homework 3\n')

print('Fill in A, B, C (each one from the new line and press Enter)')
A = int(input())
B = int(input())
C = int(input())
print(A, B, C)
if A > B:
    print('Finally!')
elif B > A:
    print('Oh, shit!')
else:
    print('What if?')
    A = A + C
    B = B - C
    if A > B:
        print('Finally!')
    else:
        print('Oh, shit!')
print('Happy end!')

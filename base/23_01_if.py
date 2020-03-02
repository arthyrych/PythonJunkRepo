A = int(input('Fill in A: '))
B = int(input('Fill in B: '))
C = int(input('Fill in C: '))
print(A, B, C)
if A > B:
    print('Finally!', A, '>', B)
elif B > A:
    print('Oh, no!', B, '>', A)
else:
    print('What if?')
    A += C
    B -= C
    if A > B:
        print('Finally!', A, '>', B)
    else:
        print('Oh, no!', B, '>', A)

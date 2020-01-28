print('Homework 2')

print('Task 1')
a, b, c, d = 5, 10, 20, 40
print(a + b)
print(d / b)
print(a * c)
print(d - c)

print('Task 2')
x = 'You\'re '
y = 'awesome'
z = x + y
print(z)

print('Task 3')
import random
Start = 9
Stop = 99
limit = 10
randomlist = [random.randint(Start, Stop) for iter in range(limit)]
del randomlist[-1]
print(randomlist)

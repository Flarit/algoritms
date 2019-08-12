from random import random



a = 10
b = [0]*a
c = []
for i in range(a):
    b[i] = int(random() * 10) + 10
    if b[i] % 2 == 0:
        c.append(i)
print( b )
print( c )
from random import random

a = 10
arr = [0] * a
for i in range(a):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]
max: int = 1
for i in range(a - 1):
    b = 1
    for k in range(i + 1, a):
        if arr[i] == arr[k]:
            b += 1
    if b > max:
        max = b
        num = arr[i]

if max > 1:
    print(max, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
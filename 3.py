from random import random


a = 10
arr = [0]*a
for i in range(a):
    arr[i] = int(random()*100)
    print(arr[i],end=' ')
print()

min = 0
max = 0
for i in range(a):
    if arr[i] < arr[min]:
        min = i
    elif arr[i] > arr[max]:
     max = i
print('arr[%d]=%d arr[%d]=%d' % (min + 1, arr[min], max + 1, arr[max]))
b = arr[min]
arr[min] = arr[max]
arr[max] = b

for i in range(10):
    print(arr[i], end=' ')
print()

from random import random

n = 10
arr = []
for i in range(n):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < n:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index + 1, ':', arr[index])
a = 5
b = 4
c = []
for i in range(b):
    b = []
    s = 0
    print("%d-я строка:" % i)
    for j in range(a - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    c.append(b)

for i in c:
    print(i)
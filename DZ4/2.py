import timeit
def ch2():
    num = [1,2]
    even = 0
    odd = 0
    for i in num:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Четных чисел - %.d, а нечетных %.d" % (even, odd))


print(timeit.timeit("ch2()", setup="from __main__ import ch2"))

#11,174 ,обрабатывается дольше чем первый вариант ,  сложность линейная


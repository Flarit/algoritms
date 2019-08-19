import timeit

def ch1():
    a = 12
    even = 0
    odd = 0

    while a > 0:
        if a % 2 == 0:
            even += 1
        else:
            odd += 1
        a = a // 10

    print("Even: %d, odd: %d" % (even, odd))



print(timeit.timeit("ch1()", setup="from __main__ import ch1"))


#9,962, обрабатывается быстрее чем второй вариант, сложность линейная
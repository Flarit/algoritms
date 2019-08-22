from random import randint

MAX_SIZE = 10

def sort(array):

    if len(array) < 2:
        return array

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    left = sort(left)
    right = sort(right)

    return merge(left, right)


def merge(list_1, list_2):
    result = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    result += list_1[i:]
    result += list_2[j:]
    return result


numbers = [randint(0, 50) for _ in range(MAX_SIZE)]

print(numbers)
print(sort(numbers))
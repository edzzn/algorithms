#!/bin/python3


def binary_search(a, q):
    min_index = 0
    max_index = len(a)-1
    while min_index <= max_index:
        middle_index = (max_index + min_index) // 2
        if q > a[middle_index] and middle_index:
            min_index = middle_index + 1

        elif q < a[middle_index]:
            max_index = middle_index - 1

        elif q == a[middle_index]:
            return 'FOUND', middle_index

    return 'NOT FOUND'


if __name__ == '__main__':
    a = [1, 3, 8, 15, 60, 84]
    q = 15
    result = binary_search(a, q)
    print(result)

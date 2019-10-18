#!/bin/python3


def find_smallest(a):
    smallest = a[0]
    smallest_index = 0
    for i in range(1, len(a)):
        if a[i] < smallest:
            smallest = a[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == '__main__':
    a = [8, 3, 7, 15, 60, 84]
    result = selection_sort(a)
    print(result)

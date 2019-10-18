#!/bin/python3
import random


def shuffle(a):
    for i in range(len(a)-2):
        random_index = random.randint(i, len(a)-1)
        print('random_index', random_index)
        aux = a[random_index]
        a[random_index] = a[i]
        a[i] = aux
    print(a)


if __name__ == '__main__':
    for l in range(6):
        print('---')
        a = [1, 2, 3]
        shuffle(a)

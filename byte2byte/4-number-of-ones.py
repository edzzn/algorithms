#!/bin/python3


def get_number_of_ones(n):
    counter = 0
    while n > 0:
        if n % 2:
            print('has 1 at the end', n)
            counter += 1

        n = n >> 1
        print(f'n: {n}, bin(n) {bin(n)}')
    return counter


if __name__ == '__main__':
    n = 14
    result = get_number_of_ones(n)
    print(f'result {result}')

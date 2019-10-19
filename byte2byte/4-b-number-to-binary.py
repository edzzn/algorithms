#!/bin/python3


def string_to_binary(b):
    print(f'Expected Result {int(b,2)}')
    total = 0
    for i, d in enumerate(b[:: -1]):
        total += int(d) * (2**i)
    return total


if __name__ == '__main__':
    b = '1011'
    result = string_to_binary(b)
    print(f'result {result}')

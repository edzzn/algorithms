#!/bin/python3
import random


def isPrime(n, max_tests):

    for i in range(max_tests):
        random_number = random.randint(2, n)
        print(random_number)
        if (random_number ** (n-1) % n != 1):
            random_number ** n % n == n
            return False
    return 'NOT FOUND'


if __name__ == '__main__':
    n = 11154546
    max_tests = 10
    result = isPrime(n, max_tests)
    print(result)

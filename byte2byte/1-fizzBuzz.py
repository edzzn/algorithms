#!/bin/python3


def fizz_buzz(x):
    for n in range(1, x+1):
        output = ''
        if n % 3 == 0:
            output += 'Fizz'

        if n % 5 == 0:
            output += 'Buzz'

        if not output:
            output = n

        print(output)


if __name__ == '__main__':
    x = 15
    fizz_buzz(x)
    # print(result)

#!/bin/python3


def make_change(x):
    coins = [25, 10, 5, 1]
    coin_counter = 0
    for coin in coins:
        while x >= coin:
            x -= coin
            coin_counter += 1
    return coin_counter


if __name__ == '__main__':
    x = 167
    result = make_change(x)
    print(f'result {result}')

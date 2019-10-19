#!/bin/python3


def is_anagram(s1, s2):
    if (len(s1) != len(s2)):
        return False

    letters = [0]*256

    for c in s1:
        letters[ord(c)] = 1 + letters[ord(c)]

    for c in s2:
        letters[ord(c)] -= 1

    for i in letters:
        if i != 0:
            return False

    return True


if __name__ == '__main__':
    s1 = 'tartPz'
    s2 = 'traAAA'
    result = is_anagram(s1, s2)
    print(f'result {result}')

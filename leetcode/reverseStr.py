#!/bin/python3


def reverseStr(s: str, k: int) -> str:
    curr_index = 0
    new_string = ''
    while True:
        if len(s[curr_index:]) > 2*k:
            new_string += s[curr_index:curr_index+k][::-1] + \
                s[curr_index+k:curr_index+2*k]
            curr_index += 2*k
            print(new_string)
        elif len(s[curr_index:]) >= k:
            new_string += s[curr_index:curr_index+k][::-1] + \
                s[curr_index+k:]
            curr_index += k
        else:

            new_string += s[curr_index:][::-1]
            break
        if len(new_string) == len(s):
            break
    return new_string


if __name__ == '__main__':
    result = reverseStr('a', 2)
    print(result)

#!/bin/python3


def balanced_string_split(text):
    balanced_strings_counter = 0
    r_counter = 0
    l_counter = 0

    for char in text:
        if char == 'R':
            r_counter += 1
        else:
            l_counter += 1

        if r_counter > 0 and r_counter == l_counter:
            balanced_strings_counter += 1

    r_counter = 0
    l_counter = 0

    return balanced_strings_counter


if __name__ == '__main__':
    a = "RLRRLLRLRL"
    result = balanced_string_split(a)
    print(result)

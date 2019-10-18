#!/bin/python3


def kadane(a):
    local_max = a[0]
    global_max = a[0]
    initial_index = 0
    final_index = 0
    for i, item in enumerate(a):
        if local_max + item > item:
            local_max += item
        else:
            local_max = item
            initial_index = i

        if local_max > global_max:
            global_max = local_max
            final_index = i

    return [global_max, initial_index, final_index]


if __name__ == '__main__':
    a = [1, -3, 2, 1, -1]
    result = kadane(a)
    print(result)

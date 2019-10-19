#!/bin/python3


# if sorted
# def numJewelsInStones(J: str, S: str) -> int:
#     counter = 0
#     for jewel in J:
#         local_counter = 0
#         for stone in S:
#             if jewel == stone:
#                 local_counter += 1

#             if jewel != stone and local_counter > 0:
#                 break
#         counter += local_counter

#     return counter

# def numJewelsInStones(J: str, S: str) -> int:
#     counter = 0

#     for jewel in J:
#         for stone in S:
#             if jewel == stone:
#                 counter += 1

#     return counter

# Best solution
def numJewelsInStones(J: str, S: str) -> int:
    counter = 0
    my_dict = dict()
    for stone in S:
        my_dict[stone] = my_dict.get(stone, 0) + 1

    for jewel in J:
        counter += my_dict.get(jewel, 0)

    return counter


if __name__ == '__main__':
    J = 'aAB'
    S = 'aaAbbbb'
    result = numJewelsInStones(J, S)
    print(result)

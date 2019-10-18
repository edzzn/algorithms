#!/bin/python3


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f'{self.val} -> {self.next}'


def findNth(a, n):
    top = Node(a[0])

    # Build the list
    current_node = top
    for i in range(1, len(a)):
        next_node = Node(a[i])
        current_node.next = next_node
        current_node = next_node

    # Search
    current_node = top
    follower_node = top
    step_counter = 0
    while current_node.next:
        current_node = current_node.next
        if step_counter >= n:
            follower_node = follower_node.next
        step_counter += 1
    print(f'n {n}, step_counter {step_counter}')
    if n <= step_counter:
        return follower_node.val
    else:
        return None


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    n_to_last = 4
    result = findNth(a, n_to_last)  # 4
    print(result)

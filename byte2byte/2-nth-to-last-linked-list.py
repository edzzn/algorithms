#!/bin/python3


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f'{self.val} -> {self.next}'


class Queue:
    def __init__(self, n):
        self.values = []
        self.max_length = n

    def add(self, val):
        if len(self.values) >= self.max_length:
            self.values.pop(0)
        self.values.append(val)

    def getNthToLast(self):
        return self.values[0]

    def __str__(self):
        return f'{self.values}'


def findNth(a, n):
    top = Node(a[0])
    queue = Queue(n)

    # Build the list
    current_node = top
    for i in range(1, len(a)):
        next_node = Node(a[i])
        current_node.next = next_node
        current_node = next_node

    # Search
    current_node = top
    while current_node:
        queue.add(current_node.val)
        current_node = current_node.next

    print(queue)
    return queue.getNthToLast()


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    n_to_last = 3
    result = findNth(a, n_to_last)  # 4
    print(result)

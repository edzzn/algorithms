#!/bin/python3


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return f'{self.value} -> [R: {self.right}, L: {self.left}]'


class BinaryTree:
    def __init__(self, root_node):
        self.root = root_node

    def add(self, node):
        current_node = self.root
        nodes_to_visit = []
        while current_node:
            if current_node.right == None:
                current_node.right = node
                break
            elif current_node.left == None:
                current_node.left = node
                break
            else:
                nodes_to_visit.append(current_node.right)
                nodes_to_visit.append(current_node.left)

                current_node = nodes_to_visit.pop(0)
        current_node.next = node
        print(f'Adding: {node}')

    def __str__(self):
        return f'{self.root}'


a = Node(1)
b = Node(2)
c = Node(3)
tree = BinaryTree(a)

print(tree)

tree.add(b)
print(tree)

tree.add(c)
print(tree)

tree.add(Node(4))

print(tree)

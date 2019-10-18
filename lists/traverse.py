class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f'[{self.val} -> {self.next}]'

    def traverse(self):
        top = self
        while top:
            print(top)
            top = top.next

    def find(self, value):
        top = self
        while top:
            if top.val == value:
                return top
            top = top.next


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
c.oo = 5
d.next = e

for var in vars(c):
    print(var, getattr(c, var))

print('****')
for var in dir(c):
    print(var, getattr(c, var))
print('****')
print(c.__dict__)
print('****')
print(vars(c))
print('****')


print(a.find(1))

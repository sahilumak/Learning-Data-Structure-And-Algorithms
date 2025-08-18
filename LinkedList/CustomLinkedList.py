class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
        
n1.next = id(n2)
n2.next = id(n3)
n3.next = id(n4)

print(n1.next)
print(n2.next)
print(n3.next)
print(n4.next)

print(id(n1))
print(id(n2))
print(id(n3))
print(id(n4))
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class Stack:
    def __init__(self):
        self.top  = None
    def isempty(self):
        return self.top == None
    def Push(self,data):
        new_node = Node(data)
        if self.top  == None:
            self.top  = new_node 
        else:
            new_node.next = self.top
            self.top = new_node
    def traverse(self):
        if (self.isempty()):
            return "Empty List"
        else:
            curr =self.top
            while curr != None:
                print(curr.data)
                curr = curr.next
    
    def Peek(self):
        if self.top == None:
            return None 
        else: 
            return self.top.data
    def Pop(self):
        if (self.isempty()):
            return "Empty Stack"
        else:
            temp = self.top.next
            self.top = temp
            
            
s1 = Stack()
s1.Push(10)
s1.Push(20)
s1.Push(30)
s1.Push(40)
s1.Push(50)
# print(s1.Peek())
# s1.traverse()
# print(s1.isempty())
s1.Pop()

s1.traverse()
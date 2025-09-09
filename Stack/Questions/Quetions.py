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
            peek = self.top
            temp = self.top.next
            self.top = temp
            return peek.data
        
# =======================================================================================


#Question 1---> String Reverse Using Stack:
def str_reverse(string):
    s = Stack()
    for i in string:
        s.Push(i)
    res = ''
    while(not s.isempty()):
        res = res + s.Pop()
    print(res)

# Question 2 --> Undo Redo  Operations
def undo_redo(Operation,text):
    Undo = Stack()
    Redo = Stack()
    for i in text:
        Undo.Push(i)
    for i in Operation:
        if i == 'u' or i == 'U':
            data = Undo.Pop()
            Redo.Push(data)
        elif i =='r' or i=='R':
            data = Redo.Pop()
            Undo.Push(data)
        else:
            return "Undifiend Operation Occurs "
    res = ""
    while(not Undo.isempty()):
        res = Undo.Pop() + res
    print(res)

# Question 3-->Bracket Stabality:
def Check_brakets(Equ):
    s = Stack()
    b = Stack()
    for i in Equ:
        if i == '(' or i == '[' or i=='{':
            s.Push(i)

        elif i ==')' or i == ']' or i =='}':
            if s.Peek == i:
                data = s.Pop()
                b.Push(data)
            else:
                print("Not Valid Equation")
                return
                
        
        
        return s.isempty()

# Question 4 ---> Celebrity Problem:


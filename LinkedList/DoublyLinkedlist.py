class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class Linkedlist:
    peak = None
    def __init__(self):
        self.head = None
        self.n = 0
    def __len__(self):
        return self.n
    def __str__(self):
        if self.head == None:
            return "Empty LinkedList" 
        else:
            result = " "
            curr = self.head
            while curr != None:
                result = result + str(curr.data) + '-->'
                curr = curr.next
            return result + 'None'
    def Create(self,value):
        New_node = Node(value)
        if self.head == None:
            self.head = New_node
        else:
            New_node.next = self.head
            self.head.prev = New_node
            self.head = New_node
        self.n += 1
    def Peak(self):
        if self.head == None:
            return "Empty List"
        else:
            Linkedlist.peak =self.head
            return Linkedlist.peak.data
    def forward(self):
        if Linkedlist.peak.next == None:
            return None
        else:
            curr = Linkedlist.peak
            Linkedlist.peak = curr.next
            return Linkedlist.peak.data
    def backword(self):
        if Linkedlist.peak.prev == None:
            return None
        else:
            curr = Linkedlist.peak
            Linkedlist.peak = curr.prev
            return Linkedlist.peak.data


l1 = Linkedlist()
# print(len(l1))
# print(l1)
l1.Create(10)
l1.Create(20)
l1.Create(30)
l1.Create(40)
print(l1)
# print(len(l1))
# print(l1.Peak())
# print(l1.forward())
# print(l1.forward())
# print(l1.Peak())
# print(l1.forward())
# print(l1.forward())
# print(l1.forward())
# print(l1)
# print(l1.forward())
print(l1.Peak())
print(l1.forward())
print(l1.forward())
print(l1.backword())
print(l1.backword())
print(l1.backword())
print(l1.backword())


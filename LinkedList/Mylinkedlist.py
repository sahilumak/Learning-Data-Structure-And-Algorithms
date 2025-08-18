class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0
    def __len__(self):
        return self.n
    def create(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:   # First node
            self.tail = new_node
        self.n += 1
    
    # Insert at tail
    def append(self, data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.n += 1
    def __str__(self):
        result = ''
        if self.head == None:
            return 'Empty LinkedList'
        else:
            curr = self.head
            while curr != None:
                result = result + str(curr.data) + "-->"
                curr = curr.next

            return (result +'None')
    def insert(self,index,value):
        count = 0
        if 0<=index<self.n:
            new_node = Node(value)
            curr = self.head
            while count+1 != index:
                curr = curr.next   
                count +=  1 
            temp = curr.next
            curr.next = new_node
            new_node.next  = temp 
            self.n += 1
        else:
            return 'Out of Range'
    
    def clear(self):
        self.n = 0
        self.head = None
        self.tail = None
    def delete(self):
        if self.n == 0:
            return 'Empty LinkedList'
        else:
            temp = self.head.next
            self.head = temp
            self.n -= 1
    

        

        

                

       






l1 = Linkedlist()
l1.create(10)
l1.create(20)
l1.create(30)
l1.create(50)
l1.create(70)
l1.create(40)
l1.create(50)
print(len(l1))
l1.append(100)
print(l1)
print(l1.insert(9,40))
print(l1)
# l1.clear()
# print(l1)
print(len(l1))
l1.delete()
print(l1)
print(len(l1))
# l1.head()
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class Linkedlist:
    peak = 0
    def __init__(self):
        self.head = None
        self.next = None
        self.n = 0
    def create(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        # if self.tail is None:   # First node
        #     self.tail = new_node
        self.n += 1
    def Peak(self):
        if self.head == None:
            return "Empty List"
        else:
            Linkedlist.peak =self.head
            return Linkedlist.peak.data
    # Insert at tail
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.create(data)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            new_node.next = None
            self.n += 1
    
    def __str__(self):
        result = ''
        if self.head==None:
            return "Empty LinkedList"
        else:
            curr = self.head
            while curr != None:
                result = result + str(curr.data) + "-->"
                curr = curr.next

        return (result +'None')
    
# Question 1--> Write a Python Program to find the maximum value in a linkedlist:
    def Maximum(self):
        if self.head == None:
            return "Empty List"
        else:
            if self.head.next == None:
                return self.head.data
            else:
                max = 0
                curr = self.head
                # curr2 = self.head.next
                while curr != None:
                    if curr.data >= max:
                        max = curr.data
                    else:
                        max = max
                    curr = curr.next
                return max
#Question 2--->Given a Linkedlist containing whole numbers,write a python function which finds and returns the Sum of all the elements at the odd position in the given linkedlist:

    def AddOdd(self):
        if self.head==None:
            return 0
        else:
            result = 0
            counter = 0
            curr = self.head
            while curr!=None:
                if counter%2 != 0:
                    result = result+curr.data
                curr = curr.next
                counter += 1
            return result
                
# Question 3--->Write a program to reverse the Linkedlist:
    def Reverse(self):
        if self.head ==None:
            return None
        else:
            prev = None
            curr = self.head
            while curr!= None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            self.head = prev
# Question 4 ---> Remove Duplicates From Linkedlist:
    def RemoveDuplicates(self):
        seen = set()
        curr = self.head
        seen.add(curr.data)
        if curr is None:
            return None
        else:
            while curr.next.next!=None:
                if curr.next.data in seen:
                    curr = curr.next.next
                else:
                    seen.add(curr.next.data)
                


l1 = Linkedlist()
l1.create(10)
l1.create(200000)
l1.create(200000)
l1.create(40)
l1.create(50)
l1.create(1000)
print(l1)
l1.RemoveDuplicates()
# l1.Reverse()
print(l1)
# print(l1.Maximum())
# print(l1.AddOdd())


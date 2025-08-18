class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        # self.tail = None
        self.n = 0
    def __len__(self):
        return self.n
    def create(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        # if self.tail is None:   # First node
        #     self.tail = new_node
        self.n += 1
    
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
    def insert(self,index,value):
        count = 0
        if index == 0:
            self.create(value)
        elif index == self.n:
            self.append(value)

        elif 0<index<self.n:
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
        # self.tail = None
    def delete(self):
        if self.n == 0 and self.head ==None:
            return "Empty List"
        else:
            temp = self.head.next
            self.head = temp
            self.n -= 1
    def pop(self):
        if self.head==None:
            return 'Empty LinkedList'
        if self.head.next ==None:
            popped = self.head.data
            self.head = None
            # self.tail = None
            self.n -= 1
            return popped
        
        else:
            curr = self.head
            while curr.next.next != None:
                curr = curr.next

            curr.next = None
            # self.tail = curr
            # self.tail.next = None
            self.n -= 1
    def search(self,value):
        count = 0
        if self.head == None:
            return "Empty LinkedList"
        else:
            curr = self.head
            while curr != None:
                if curr.data == value:
                    return count
                curr = curr.next
                count = count+1
            return "Not Fount"


# ====== Test Cases for LinkedList ======

# LL = Linkedlist()

# print("Initially:", LL)                      # Empty LinkedList
# print("Length:", len(LL))                   # 0

# # Append elements
# LL.append(10)
# LL.append(20)
# LL.append(30)
# print("\nAfter appending 10,20,30:", LL)     # 10-->20-->30-->None
# print("Length:", len(LL))                   # 3

# # Insert at head
# LL.insert(0, 5)
# print("\nAfter inserting 5 at head:", LL)   # 5-->10-->20-->30-->None

# # Insert in middle
# LL.insert(2, 15)
# print("\nAfter inserting 15 at index 2:", LL) # 5-->10-->15-->20-->30-->None

# # Insert at tail
# LL.insert(len(LL), 40)
# print("\nAfter inserting 40 at tail:", LL)   # 5-->10-->15-->20-->30-->40-->None

# # Delete from head
# deleted = LL.delete()
# print("\nDeleted head:", deleted)            # 5
# print("After deleting head:", LL)            # 10-->15-->20-->30-->40-->None

# # Pop from tail
# popped = LL.pop()
# print("\nPopped from tail:", popped)         # 40
# print("After pop:", LL)                      # 10-->15-->20-->30-->None

# # Clear the list
# LL.clear()
# print("\nAfter clearing:", LL)               # Empty LinkedList
# print("Length:", len(LL))                   # 0


 
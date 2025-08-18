import ctypes
class Mylist:
    def __init__(self):
        self.n = 0
        self.size = 1
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __make_array(self,size):
        return (size*ctypes.py_object)()

    def __resize(self,new_size):
        b = self.__make_array(new_size)
        self.size = new_size
        for i in range(self.n):
            b[i] = self.A[i]
        self.A = b

    def append(self,value):
        if self.size == self.n:
            self.__resize(self.size*2)
        self.A[self.n] = value
        self.n = self.n + 1
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return ('[' + result[:-1] + ']')
    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'Out of range'

    def pop(self):
        if self.n == 0:
            return 'Empty list'
        value = self.A[self.n-1]
        self.n -= 1
        return value

    def clear(self):
        self.n = 0
        self.size = 1
        self.A = self.__make_array(self.size)

    def find(self,value):
        for i in range(self.n):
            if self.A[i] == value:
                return i
        else:
            return 'Not in List'
    def insert(self,pos,value):
        if self.n == self.size:
            self.__resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        self.A[pos]=value
        self.n = self.n + 1
    def delete(self,pos):
        if 0<=pos<self.n:
            for i in range(pos,self.n-1):
                self.A[i] =self.A[i+1]
            self.n -= 1
        else:
            return 'Out of Range'
    def replace(self,pos,value):
        if 0<=pos<self.n:
            self.A[pos] = value
        else:
            return 'Out of Range'
    def remove(self,value):
        pos = self.find(value)
        if type(pos) == int:
            self.delete(pos)
        else:
            return pos
    def sort(self):
        pass
    def min(self):
        pass
    def max(self):
        pass
    def extend(self):
        pass
    


            
# ---- Test Cases for Mylist ----

l = Mylist()

# 1. Append
print("Append test:")
for i in range(1, 9):
    l.append(i * 10)
print(l)   # [10,20,30,40,50,60,70,80]

# 2. Length
print("Length:", len(l))  # 8

# 3. Get item (__getitem__)
print("Get item test:")
print(l[0])   # 10
print(l[3])   # 40
print(l[10])  # Out of range

# 4. Insert
print("Insert test:")
l.insert(2, 99)
print(l)   # [10,20,99,30,40,50,60,70,80]

# 5. Delete
print("Delete test:")
l.delete(3)
print(l)   # [10,20,99,40,50,60,70,80]

# 6. Replace
print("Replace test:")
l.replace(4, 555)
print(l)   # [10,20,99,40,555,60,70,80]

# 7. Find
print("Find test:")
print(l.find(555))   # index of 555
print(l.find(999))   # Not in List

# 8. Pop
print("Pop test:")
print("Popped:", l.pop())  # should return 80
print(l)

# 9. Clear
print("Clear test:")
l.clear()
print(l)   # []
print("Length after clear:", len(l))  # 0



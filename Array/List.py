import ctypes
class Mylist:
    def __init__(self):
        self.size = 1
        self.n = 0

        # Create a C type array with size  = self.size
        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        # This Code Creates a Ctype Array with size Capacity(Static array , Refrrential Array)
        return (capacity*ctypes.py_object)()

        
    def __len__(self):
        return (self.n)
    def append(self,New):
        if self.size ==self.n:
            self.__resize(self.size*2)
            
        self.A[self.n] = New
        self.n = self.n +1 
    def __resize(self,new_size):
        B = self.__make_array(new_size)
        self.size = new_size
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
       
    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    

    def __getitem__(self,index):
        if 0<=index < self.n :
            return self.A[index]
        else:
            return 'IndexError - Index Out Of Range'
    def pop(self):
        if self.n == 0:
            return 'Empty List'
        else:
            print(self.A[self.n-1])
            self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1
    
    def find(self,value):
        for i in range(self.n):
            if self.A[i] == value:
                return i
        return 'Not In List'
    def insert(self,index,value):
        if self.size == self.n:
            self.__resize(self.size*2)

        for i in range(self.n,index,-1):
            self.A[i] = self.A[i-1]
        self.A[index] = value
        self.n = self.n + 1

    def delete(self,pos):
        for i in range(pos,self.n-1):
            self.A[i] = self.A[i+1]
        self.n = self.n - 1
    

    def replace(self,pos,value):
        if self.size < pos:
            return 'out of range '
        self.A[pos]=value

    def remove(self,value):
        pos = self.find(value)
        if type(pos)==int:
            self.delete(pos)
        else:
            return pos

    
L = Mylist()
L.append(5)
L.append(25)
L.append('Hellow')
L.append(45)
L.append(100)
L.append(150)

L.insert(2,30)
print(L)

L.remove('Hellow')
# L.delete(3)
print(L)
# print(L.find('Hellow'))

# print(L)
# L.delete(2)
# print(L)
# print(L.find(100))
# L.clear()
# print(L)
# L.pop()
# print(L)
# L.pop()
# print(L)
# L.pop()
# L.pop()
# L.append(5)
# print(L)
# L.pop()
# print(L)
# L.pop()

        

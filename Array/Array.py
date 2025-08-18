#Creating Dynamic List 
import ctypes
class Mylist:
    def __init__(self):
        self.n = 0
        self.size = 1
        self.A = self.__make_array(self.size)
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __resize(self,new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A =B

    def append(self,value):
        if self.n == self.size:
            self.__resize(self.size*2)
        self.A[self.n] = value
        self.n += 1

    def __len__(self):
        return self.n
    
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    
    

l2 = Mylist()
l2.append(10)
l2.append(20)
l2.append(30)
len(l2)
print(l2)
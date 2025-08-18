#Tow Pointer:
def TwoSum(arr,target):
    left = 0
    right = len(arr)-1

    for i in range(len(arr)-1):
        if arr[left] + arr[right] == target:
            return left,right
        if arr[left]+arr[right] > target:
            right = right -1
        else:
            left = left + 1
# class Solution:
#     def __init__(self,arr):
#         self.arr = arr
#         self.result = []
#         self.left = 0
#         self.right = len(arr)-1
#     def sort(self):
#         new_arr =  sorted(self.arr)
#         return new_arr
#     def getPairs(self):
#         new_arr = self.sort()
#         for i in range(len(new_arr)-1):
#             if new_arr[self.left]+new_arr[self.right] == 0:
#                 self.result.append([self.left,self.right])
#             elif new_arr[self.left]+new_arr[self.right] > 0:
#                 self.right = self.right -1
#             else:
#                 self.left = self.left+1
#         return self.result



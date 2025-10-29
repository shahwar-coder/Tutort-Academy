'''
Geeksforgeeks: Wave Array (medium):
https://www.geeksforgeeks.org/problems/wave-array-1587115621/1
'''

from typing import List
class Solution:
    def _swap(self, arr: List[int], index: int)->None:
        """
        I just swap two elements.
        In Place manipulation, no returning
        """
        arr[index], arr[index+1] = arr[index+1], arr[index]
        
        
    def sortInWave(self, arr):
        if len(arr)<=1:
            return arr
        for index in range(len(arr)-1):
            if index%2==0:
                if arr[index]<arr[index+1]:
                    self._swap(arr, index)
            else:
                if arr[index]>arr[index+1]:
                    self._swap(arr, index)
        return arr
        
obj=Solution()
result = obj.sortInWave(arr=[1,2,3,4,5])
print(result)

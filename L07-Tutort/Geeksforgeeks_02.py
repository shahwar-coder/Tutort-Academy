'''
Geeksforgeeks: Wave Array (medium):
https://www.geeksforgeeks.org/problems/wave-array-1587115621/1
'''

from typing import List
class Solution:
    def swap(self, arr: List[int], index: int)->None:
        """
        I just swap two elements
        """
        temp=arr[index]
        arr[index]=arr[index+1]
        arr[index+1]=temp
        
        
    def sortInWave(self, arr):
        if len(arr)==1:
            return arr
        for index in range(len(arr)-1):
            if index%2==0:
                if arr[index]<arr[index+1]:
                    self.swap(arr, index)
            else:
                if arr[index]>arr[index+1]:
                    self.swap(arr, index)
        return arr

'''
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/description/
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        write = m + n - 1

        while j>=0: # will loop till all nums2 numbers are placed
            if i>=0 and nums1[i]>nums2[j]: # i>0, if imp as nums1 can finish before nums2
                nums1[write]=nums1[i]
                i-=1
            else:
                nums1[write]=nums2[j] # if nums2 is lenthier, then remaining can get copied here
                j-=1
            write-=1

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         for i in range(n):
#             nums1[m+i]=nums2[i]
#         nums1.sort()

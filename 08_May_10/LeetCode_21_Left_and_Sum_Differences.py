'''
2574. Left and Right Sum Differences
https://leetcode.com/problems/left-and-right-sum-differences/
'''



# Below was ORIGINAL but BRUTE FORCE
# class Solution:
#     def leftSum(self, nums: List[int]):
#         left_list=[]
#         for i,n in enumerate(nums):
#             if i==0:
#                 left_list.append(0)
#             else:
#                 left_list.append(sum(nums[:i]))
#         return left_list

#     def rightSum(self, nums: List[int]):
#         nums=list(reversed(nums))
#         right_list=[]
#         for i,n in enumerate(nums):
#             if i==0:
#                 right_list.append(0)
#             else:
#                 right_list.append(sum(nums[:i]))
#         return list(reversed(right_list))
        
  
#     def leftRightDifference(self, nums: List[int]) -> List[int]:
#         diff_list=[]
#         zipped = zip(self.leftSum(nums), self.rightSum(nums))
#         for a,b in zipped:
#             diff=abs(a-b)
#             diff_list.append(diff)
#         return diff_list

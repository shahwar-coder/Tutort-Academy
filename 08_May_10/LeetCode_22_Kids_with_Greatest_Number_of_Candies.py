'''
1431. Kids With the Greatest Number of Candies:
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
'''
# OPTIMISED
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        if not candies:
            return []
        original_max=max(candies)
        return [(candy + extraCandies) >= original_max for candy in candies]


# ORIGINAL BUT NOT OPTIMISED  
# from typing import List
# class Solution:
#     def isMax(self, kid_index: int, updated_candies: List[int])->bool:
#         """
#         Tells if the kid has max candies if given extra candies
#         """
#         max_val = max(updated_candies)
#         return max_val==updated_candies[kid_index]

#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         truthy_candies=[]
#         for i in range(len(candies)):
#             updated_candies=candies.copy()
#             updated_candies[i]+=extraCandies
#             if self.isMax(i, updated_candies):
#                 truthy_candies.append(True)
#             else:
#                 truthy_candies.append(False)
#         return truthy_candies

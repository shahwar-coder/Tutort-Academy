'''
670. Maximum Swap
https://leetcode.com/problems/maximum-swap/description/?utm_source=chatgpt.com
'''
# THIS SOLUTION NEEDS REATTAMPT, IT'S ONLY PARTIALLY CORRECT
# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         if not num:
#             return 0

#         num_str=str(num)
#         num_list=list(num_str)
#         max_digit=0
#         for i, n in enumerate(num_str):
#             if int(n)>=max_digit:
#                 max_digit=int(n)
#                 later_max_digit_index=i

#         num_list[0], num_list[later_max_digit_index] = num_list[later_max_digit_index], num_list[0]

#         return int("".join(num_list))


        
            


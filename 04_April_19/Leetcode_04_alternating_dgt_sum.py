'''
2544. Alternating Digit Sum:
https://leetcode.com/problems/alternating-digit-sum/description/
'''

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits=list(map(int, str(n)))
        return sum(digit if index%2==0 else -digit for index, digit in enumerate(digits))

# class Solution:
#     def alternateDigitSum(self, n: int) -> int:
#         total=0
#         for index, digit in enumerate(str(n)): #index starts 0
#             if index%2==0:
#                 total+=int(digit)
#             else:
#                 total-=int(digit)
#         return total


# 1st one I learned and improved
# Variable use and orthodox summing is avoided
            

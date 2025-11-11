'''
231. Power of Two:
https://leetcode.com/problems/power-of-two/
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      return n>0 and (n & (n-1))==0


'''
I am writing one example here for stating the logic here (bit manipulation):
Consider,
   n = 8  → binary 1000  
   n-1 = 7 → binary 0111  
   1000 & 0111 = 0000 → only powers of two produce 0 here.
'''

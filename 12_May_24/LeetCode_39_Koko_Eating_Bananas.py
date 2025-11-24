'''
875. Koko eating Bananas
https://leetcode.com/problems/koko-eating-bananas/description/
'''

import math
class Solution:
    def total_hours(self, piles, speed)->int:
        return sum(math.ceil(pile / speed) for pile in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0

        low, high = 1, max(piles)
        
        while low<=high:
            mid = low+(high-low)//2
            if self.total_hours(piles, mid)<=h:
                # mid is too fast, we need to try smaller speeds
                high=mid-1
            else:
                # mid is too slow, we need to try larger speeds
                low=mid+1
        return low # or high, as both will be same at the end

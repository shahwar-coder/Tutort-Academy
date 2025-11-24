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


# Easy-to-Understand Key Points for “Koko Eating Bananas”

# - Koko wants the **minimum eating speed K** so she finishes all piles in **h** hours.
# - If she eats at speed K:
#     time for one pile = ceil(pile / K)
# - Total time = sum of times for all piles.

# - We cannot brute-force all speeds up to max(piles). Too slow.
# - Instead, use **Binary Search on the answer (the speed K)**:
#     - Smallest possible speed = 1
#     - Largest possible speed = max pile size

# - For a guessed speed mid:
#     - Compute total_hours(piles, mid)
#     - If total_hours ≤ h → mid might be enough → try smaller speed (search left)
#     - Else → mid is too slow → increase speed (search right)

# - When the binary search ends, low = smallest valid speed.

# - Time Complexity: O(n · log(max(pile)))
# - Space Complexity: O(1)


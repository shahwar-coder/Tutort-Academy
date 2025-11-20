'''
1217. Minimum Cost to Move Chips to The Same Position:
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
'''

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
        Cost to move chips equals the smaller of the counts of chips on odd vs even positions.
        """
        odd = sum(pos&1 for pos in position)
        even = len(position)-odd
        return min(odd, even)


# OPTIMISED WAY TO FIND ODD (Bitwise AND '&')
# x = 7            # 111
# x & 1 → 1        # odd

# x = 12           # 1100
# x & 1 → 0        # even

'''
- Chips sitting on **even positions** can move to any other even position for **0 cost**.
- Chips sitting on **odd positions** can move to any other odd position for **0 cost**.
  (So chips move freely within their own group.)

- A chip only costs **1** to move when it needs to change from:
    odd → even, or
    even → odd.

- To gather all chips at one position:
    - You must choose either an ODD spot or an EVEN spot.
    - Chips already in that group cost **0**.
    - Chips in the opposite group cost **1 per chip** to cross over.

- So the total cost = number of chips that are on the *other* side.
    → If you choose an even position, cost = number of odd chips.
    → If you choose an odd position, cost = number of even chips.

- Therefore, the minimum cost = **the smaller of (odd_count, even_count)**.
  Because that’s the minimum number of chips that need to switch sides.

- Time: O(n) to count odd/even.
- Space: O(1).
'''

'''
1725. Number Of Rectangles That Can Form The Largest Square:
https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/description/
'''

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        if not rectangles:
            return 0
        count=0
        max_side=0
        for l,w in rectangles:
            side=min(l,w)
            if side>max_side:
                max_side=side
                count=1
            elif side==max_side:
                count+=1
        return count


# 1. Edge case: if rectangles == [] → return 0.
# 2. Init: max_side = 0, count = 0.
# 3. For each [l, w]:
#    - side = min(l, w)        # largest square this rect can form
#    - if side > max_side:     # new larger square found
#        max_side = side
#        count = 1
#    - elif side == max_side:  # another rect matches current largest
#        count += 1
# 4. Return count.

# Why correct:
# - max_side always holds the largest `min(l,w)` seen so far; count tracks how many equal that max.
# - Single pass guarantees every rectangle is considered.

# Complexity:
# - Time: O(n) (one pass)
# - Space: O(1) (a few scalars only)

# Quick example:
# - Input: [[5,8],[3,9],[5,12],[8,8]] → sides [5,3,5,8] → max_side=8, count=1 → return 1

      
'''
Reasons why the optimized (top) code is better (one more code is below, which I attempted first):

• Uses O(1) extra space instead of storing an entire list of side lengths (O(n) space in the second version).
• Performs the counting in a single pass, making it more efficient and direct.
• Avoids calling max() on a list, which requires an extra full pass over all elements.
• More memory-efficient because it doesn’t allocate an additional list (max_possible_sides).
• Cleaner logic: computes max_side and count simultaneously rather than separating into two phases.
• Fewer operations overall → better constant-time performance in practice.
• Idiomatic and concise for competitive programming / LeetCode style optimization.
• Easier to reason about: directly tracks what matters (current max and its frequency).
'''

# class Solution:
#     def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
#         if not rectangles:
#             return 0
#         max_possible_sides=[]
#         for l,w in rectangles:
#             max_possible_sides.append(min(l,w))
#         max_length=max(max_possible_sides)
#         return sum(i==max_length for i in max_possible_sides)

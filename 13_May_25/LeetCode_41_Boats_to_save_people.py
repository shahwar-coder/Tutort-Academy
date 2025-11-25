'''
881. Boats to Save People
https://leetcode.com/problems/boats-to-save-people/description/
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        left, right = 0, len(people)-1

        while left<=right:
            if people[left]+people[right]<=limit:
                boats+=1
                left+=1
                right-=1
            else:
                boats+=1
                right-=1 # because that larger weight person has left with one boat, and we shift 1 to left
        return boats


# Easy-to-Understand Key Points for “Boats to Save People”

# - Each boat can carry at most 2 people.
# - Total weight on a boat must not exceed `limit`.

# - Sort the people by weight.
#   - Lightest person at the left pointer.
#   - Heaviest person at the right pointer.

# - Greedy idea:
#     - Try to pair the lightest + heaviest person.
#     - If their sum ≤ limit → they can share a boat.
#         left += 1, right -= 1
#     - Else → heaviest person goes alone (too heavy to pair).
#         right -= 1
#     - In both cases, we used 1 boat → boats += 1

# - Continue until left > right.

# - Why it works:
#     - Pairing the heaviest with the lightest gives the best chance to fit two.
#     - If the heaviest can’t pair with the lightest, they can’t pair with anyone else.

# - Time: O(n log n) due to sorting.
# - Space: O(1) extra (sorting in-place, two pointers only).

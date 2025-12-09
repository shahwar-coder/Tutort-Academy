'''
1528. Shuffle String
https://leetcode.com/problems/shuffle-string/
'''

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result=['']*len(s)
        for i, index in enumerate(indices):
            result[index] = s[i]
        return ''.join(result)

# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         return ''.join([char for _, char in sorted(zip(indices, s), key=lambda x: x[0])])


'''
# Easy-to-Understand Key Points for “Shuffle String”

- You are given:
      s       → original string
      indices → target positions for each character of s

- The rule:
      s[i] must be placed at position indices[i] in the final string.

- Create a result array of the same length:
      result = [''] * len(s)
  (Using a list because strings are immutable in Python.)

- Loop through each character:
      for i, index in enumerate(indices):
          result[index] = s[i]
  → This directly places every character into its correct final position.

- Finally, join the list into a string:
      ''.join(result)

- Why this works:
    - Direct index placement avoids extra scans.
    - No need for sorting or complex operations.
    - Perfect for one-pass O(n) reconstruction.

- Time Complexity: O(n)
- Space Complexity: O(n) for the result list
'''

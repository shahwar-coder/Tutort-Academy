'''
2418. Sort the People
https://leetcode.com/problems/sort-the-people/description/
'''

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for height, name in sorted(zip(heights, names), reverse=True)]

      
# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         name_height_map = {}
#         for i in range(len(names)):
#             name_height_map[heights[i]] = names[i]
        
#         return [tup[1] for tup in sorted(name_height_map.items(), key = lambda x: x[0], reverse=True)]


'''
# Easy-to-Understand Key Points for “Sort the People”

- We need to sort people in **descending order** of their heights.
- Names and heights are given in separate lists but correspond by index.

- Zip the data together:
      zip(heights, names)
  → creates pairs like (height, name)

- Sort these pairs in reverse (descending) order:
      sorted(zip(heights, names), reverse=True)

- After sorting, extract only the names in the new order using a list comprehension:
      [name for height, name in ... ]

- Why this works:
    - Python sorts tuples by first element (height), which is exactly what we want.
    - reverse=True ensures tallest → shortest.

- Time Complexity: O(n log n) for sorting.
- Space Complexity: O(n) for the sorted list.
'''

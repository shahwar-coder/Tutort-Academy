'''
867. Transpose Matrix
https://leetcode.com/problems/transpose-matrix/description/
'''

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        rows<-->cols (Transpose)
        """
        return [list(row) for row in zip(*matrix)]

# - Transpose means flipping the matrix over its diagonal.
# - Rows become columns, and columns become rows.
# - Example: element at (row i, col j) moves to (row j, col i).
# - Python’s zip(*matrix) groups the 1st elements together, then 2nd, and so on → perfect for transposing.
# - list(row) is used because zip gives tuples and we want lists.
# - This one-liner works for any rectangular matrix (not only square).
# - Time: O(m*n) because every element is visited once.
# - Space: O(m*n) for the new transposed matrix.


# class Solution:
#     def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
#         """
#         rows<-->cols (Transpose)
#         """
#         new_matrix=[]
#         for i in zip(*matrix):
#             new_matrix.append(list(i))
#         return new_matrix

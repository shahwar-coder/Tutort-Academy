'''
1572. Matrix Diagonal Sum:
https://leetcode.com/problems/matrix-diagonal-sum/description/
'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Sum of Primary & Seconday elements, not repeating middle element.
        """
        if not mat:
            return 0

        diagonal_sum=0
        n=len(mat)

        for i in range(n):
            # primary diagonal
            diagonal_sum+=mat[i][i]
            # secondary diagonal
            if i!=n-1-i:
                diagonal_sum+=mat[i][n-1-i]
                
        return diagonal_sum


# Key Points:

# A square matrix has two special lines: the main diagonal and the opposite diagonal.
# Main diagonal = mat[i][i] → the element from top-left to bottom-right.
# Opposite diagonal = mat[i][n-1-i] → the element from top-right to bottom-left.
# We can get both diagonals using just one loop (i from 0 to n-1).
# For every i:
# Add the main diagonal element.
# Add the opposite diagonal element.
# But if both diagonals meet at the same middle cell (only in odd-sized matrices), add it only once.
# Keep a running total in a variable (diagonal_sum).
# Time: O(n) → we check one row per loop.
# Space: O(1) → we only store a few numbers.
# Final answer = sum of both diagonals without double-counting the middle.

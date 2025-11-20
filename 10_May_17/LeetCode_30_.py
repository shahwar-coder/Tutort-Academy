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

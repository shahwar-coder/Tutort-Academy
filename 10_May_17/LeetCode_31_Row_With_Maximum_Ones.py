'''
2643. Row With Maximum Ones:
https://leetcode.com/problems/row-with-maximum-ones/description/
'''

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        """
        Find the row with max ones, if same ones select the one with lower row index.
        Also find how many ones in that selected row.
        """
        if not mat:
            return [0,0]

        max_total_ones=0
        max_ones_index=0

        for index, row in enumerate(mat):
            # row_sum=sum(row)
            row_sum=row.count(1) # efficient for binary rows
            if row_sum>max_total_ones:
                max_total_ones=row_sum
                max_ones_index=index

        return [max_ones_index, max_total_ones]

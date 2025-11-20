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


# Easy-to-Understand Key Points for “Row With Maximum Ones”

# - We need two things:
#     1) Which row has the most number of 1s.
#     2) How many 1s that row contains.
# - Go through each row one by one and count how many 1s it has.
# - row.count(1) is simple and fast because the row only has 0s and 1s.
# - Keep track of:
#     - max_total_ones → the highest number of 1s found so far.
#     - max_ones_index → the row where this maximum happened.
# - If a row has more 1s than the current maximum, update both values.
# - If two rows have the same number of 1s, choose the one with the smaller index (this naturally happens because we only update on “>”).
# - After finishing all rows, return [row_index, number_of_ones].
# - Time: O(m*n) because we check every number in the matrix.
# - Space: O(1) because we only store counters.

'''
2678. Number of Senior Citizens
https://leetcode.com/problems/number-of-senior-citizens/description/
'''

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(detail[-4:-2])>60 for detail in details)

'''
• sum(x > 0 for x in nums) uses a generator — no list built, more memory-efficient.  
• sum([x > 0 for x in nums]) builds a list first — slower, uses extra space.  
• Functions like sum(), any(), all(), max(), min() accept generators directly.  
• Hence, omit [] inside such functions for cleaner and faster code.  
'''

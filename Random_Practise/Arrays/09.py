'''
1796. Second Largest Digit in a String
https://leetcode.com/problems/second-largest-digit-in-a-string/
'''

class Solution:
    def secondHighest(self, s: str) -> int:
        dgts = set()
        for ch in s:
            if ch.isdigit():
                dgts.add(int(ch)) 
        # now we have all unique digits

        # if dgts has 1 or no value, there can be no 2nd largest
        if len(dgts)<=1:
            return -1

        # if control come here, it has sufficient values
        # remove the max digit
        dgts.remove(max(dgts))
        return max(dgts)

# class Solution:
#     def secondHighest(self, s: str) -> int:
#         dgts = []
#         for ch in s:
#             if ch.isdigit():
#                 dgts.append(int(ch))

#         if not dgts:
#             return -1

#         dgts = set(dgts)
#         dgts.remove(max(dgts))

#         if len(dgts)<1:
#             return -1
#         else:
#             return max(dgts)

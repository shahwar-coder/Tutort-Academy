'''
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/
'''
'''This Solution is great, looks like two pointers but truely is not, TWO POINTER approach works "IN-PLACE"'''
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         filtered_chars=[]
#         for ch in s:
#             if ch.isalnum():
#                 filtered_chars.append(ch.lower())
#         new_s=''.join(filtered_chars)

#         n=len(new_s)
#         for i in range(n//2):
#             if new_s[i]!=new_s[n-i-1]:
#                 return False
#         return True

'''True Solution, Optimised'''

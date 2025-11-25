'''
Q1. What is the Meeting-in-the-Middle two-pointer pattern?
Ans:
It uses two pointers starting from opposite ends of a list or string
and moves them toward the center while comparing elements.
'''
# Example:
# left=0, right=n-1 → move inward each step.



'''
Q2. Why is this pattern ideal for palindrome checking?
Ans:
A string is a palindrome if the first and last characters match,
then the next pair matches, and so on.
Meeting in the middle allows checking these pairs efficiently.
'''
# Example:
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        # check matching characters
        if s[left] != s[right]:
            return False
        left += 1     # move toward middle
        right -= 1
    return True

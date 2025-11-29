'''
Q1. What is a sliding window in the simplest words?
Ans:
It is like looking at a small part of an array and then slowly sliding that part to the right.
'''
# Example: [2,1,3,2] and a window of size 3 → looks at [2,1,3], then [1,3,2]



'''
Q2. Why do we use a sliding window?
Ans:
Because it helps us check many parts of the array without starting the calculation again every time.
'''
# Example: Instead of summing 3 numbers again and again, we reuse the old sum.



'''
Q3. What is a fixed sliding window?
Ans:
A window whose size stays the same — like always looking at 3 numbers at a time.
'''
# Example: size = 3 → [2,1,3], [1,3,2], [3,2,4]



'''
Q4. What is a variable sliding window?
Ans:
A window that can grow or shrink depending on the condition of the problem.
'''
# Example: Increase window until sum ≥ target, then shrink from left.



'''
Q5. Why is sliding window faster than checking every possible group?
Ans:
Because we reuse the old work — we only remove one number and add one new number.
'''
# Example: Old sum = 6 → slide → new sum = 6 - old_left + new_right



'''
Q6. Where do we use sliding window in real problems?
Ans:
In problems asking for “best group of consecutive numbers” like maximum sum or longest streak.
'''
# Example: finding the longest run of 1’s in a binary array.

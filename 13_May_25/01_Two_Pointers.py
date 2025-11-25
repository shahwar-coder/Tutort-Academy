'''
Q1. What does “two pointers” mean in coding?
Ans:
It means using two index variables to scan an array at the same time.
They usually start at different positions and move independently.
'''
# Example:
# left = 0, right = n-1 → both move inward.



'''
Q2. Why are two pointers useful?
Ans:
They let us solve many problems in linear time O(n)
without using extra memory.
'''
# Example:
# Instead of nested loops (O(n²)), we use two pointers (O(n)).



'''
Q3. What are common types of pointer pairs?
Ans:
• Left & Right pointer  
• Slow & Fast pointer  
• Read & Write pointer  
• Pointer on arr1 & pointer on arr2  
Each pair solves a different category of problems.
'''
# Example:
# Slow/Fast → detect cycles, find middle of linked list.



'''
Q4. What is the goal of the two-pointer technique?
Ans:
To process arrays efficiently by reducing repeated work,
achieving O(n) time and O(1) extra space.
'''
# Example:
# Removing duplicates, moving zeroes, merging arrays → all O(n).



'''
Q5. When should you think about using two pointers?
Ans:
Whenever the problem involves:
• sorted arrays  
• searching from both ends  
• compressing or cleaning data  
• merging or comparing two lists  
• skipping or filtering elements efficiently
'''
# Example:
# Sorted array + target sum → perfect case for left & right.

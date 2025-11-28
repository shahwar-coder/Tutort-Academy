'''
Q1. What is a variable sliding window?
Ans:
It is a window on an array that can grow or shrink depending on a rule.
'''
# Example: Keep adding numbers until sum > 10, then shrink.

'''

Q2. How does the window grow?
Ans:
The right pointer moves to the right and we add the new element to the sum.
'''
# Example: Add 2 → Add 3 → Add 1…

'''

Q3. When do we shrink the window?
Ans:
We shrink when the window breaks the rule (like sum > 10).
'''
# Example: If sum = 16, start removing from the left.

'''

Q4. What do we track while moving the window?
Ans:
We track the size of the largest valid window.
'''
# Example: Best window = [2,3,1,4] size 4.

'''

Q5. Why is this method fast?
Ans:
Because we never reset; we reuse previous work by adding and removing numbers.
'''
# Example: window_sum += arr[right], window_sum -= arr[left]
'''

Q6. What is the goal of the example problem?
Ans:
Find the longest group of numbers whose sum is ≤ 10.
'''
# Example: Answer = 4
'''

Q7. What are the two pointers called?
Ans:
Left pointer (start) and right pointer (end). They define the window.
'''
# Example: window = arr[left:right+1]

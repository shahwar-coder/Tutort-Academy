'''
Q1. What problem does Kadane’s Algorithm solve?
Ans:
It finds the maximum sum of any continuous subarray in an array.
It chooses the best streak of numbers that stay together.
'''
# Example: [2, -1, 3] → best streak = [2, -1, 3] → sum = 4



'''
Q2. What are the two main variables in Kadane’s Algorithm?
Ans:
current_sum → sum of the ongoing streak.
max_sum → the best streak found so far.
'''
# Example: If current_sum reaches 7, update max_sum = 7.



'''
Q3. What formula does Kadane apply on every number x?
Ans:
current_sum = max(x, current_sum + x)
Then update:
max_sum = max(max_sum, current_sum)
'''
# Meaning: “Start from x or continue the streak?”



'''
Q4. Why do we compare x with (current_sum + x)?
Ans:
Because sometimes starting a new streak at x is better than extending a bad streak.
'''
# Example: current_sum = -10, x = 3 → better to start new streak → 3.



'''
Q5. How does Kadane ensure O(n) time?
Ans:
It makes only one pass through the array, doing constant work at each step.
'''
# One loop: for x in nums → O(n)



'''
Q6. What is the final output of Kadane’s Algorithm?
Ans:
The value stored in max_sum after finishing the loop.
This is the maximum subarray sum.
'''
# Example: For [1, -2, 4, -1, 3] → max_sum becomes 6.



'''
Q7. Why does Kadane not need recursion or checking all subarrays?
Ans:
Because it uses a greedy decision at each element:
continue the streak or restart it.
This eliminates the need to try every possible subarray.
'''
# Brute force subarrays = O(n²), Kadane = O(n)

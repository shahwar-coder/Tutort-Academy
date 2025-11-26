'''
Q1. What is a prefix sum in simple words?
Ans:
A prefix sum is a list of running totals where each position shows the sum of all numbers up to that point.
'''
# Example:
# nums   = [2, 5, 3]
# prefix = [2, 7, 10]



'''
Q2. How do you create a prefix sum?
Ans:
Start with the first number. Then keep adding each new number to the total you already have.
'''
# Example:
# Start: 2
# Add 5 → 7
# Add 3 → 10



'''
Q3. Why do we use prefix sums?
Ans:
Because they help us find the sum of any part of the list quickly without adding everything again.
'''
# Example:
# To get sum of first 3 numbers, prefix gives it instantly.



'''
Q4. How does prefix sum make adding a range faster?
Ans:
Instead of adding each number one-by-one, we use the totals already stored in the prefix list.
'''
# Example:
# Instead of adding 5 + 3 + 1 again, prefix helps in one step.



'''
Q5. What does prefix[i] represent?
Ans:
prefix[i] is the total of all numbers from the start up to index i.
'''
# Example:
# prefix[2] = nums[0] + nums[1] + nums[2]

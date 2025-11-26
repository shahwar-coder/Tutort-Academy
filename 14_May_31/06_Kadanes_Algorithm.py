'''
Q0. Why is Kadane’s Algorithm faster than divide and conquer?
Ans:
Kadane does the same job in O(n) by iterating once, without splitting.
'''
# Example: Kadane on [2, -1, 3, -4, 5]

# Initialize:
#     current_sum = 0
#     max_sum = -inf

# Step 1: element = 2
#     current_sum = max(2, current_sum + 2) = 2
#     max_sum = 2

# Step 2: element = -1
#     current_sum = max(-1, 2 + (-1)) = 1
#     max_sum = max(2, 1) = 2

# Step 3: element = 3
#     current_sum = max(3, 1 + 3) = 4
#     max_sum = max(2, 4) = 4

# Step 4: element = -4
#     current_sum = max(-4, 4 + (-4)) = 0
#     max_sum = 4

# Step 5: element = 5
#     current_sum = max(5, 0 + 5) = 5
#     max_sum = max(4, 5) = 5

# Final Answer = 5

# # Why faster?
#     - No recursion
#     - No splitting the array
#     - No merging left/right results
#     - Only one forward pass

# # Core rule:
#     If current_sum becomes negative → reset to 0 (start new subarray).


'''
Q1. What is Kadane’s Algorithm in simple words?
Ans:
It is a method to find the maximum total you can get from a continuous part of a list.
You walk through the numbers and keep a running sum, restarting whenever the sum goes negative.
'''
# Example: [2, -1, 3] → best continuous part is [2, -1, 3] = 4



'''
Q2. Why do we restart when the running sum becomes negative?
Ans:
Because a negative sum only pulls the next numbers down.
Starting fresh gives a better chance to increase the total.
'''
# Example: current_sum = -5 → adding future numbers becomes harder.



'''
Q3. What does "current_sum" mean?
Ans:
It is the sum you are building right now from the current streak of numbers.
If it turns bad (negative), throw it away and start again.
'''
# Example: For [4, -6], after -6 → restart because current_sum = -2



'''
Q4. What does "max_sum" mean?
Ans:
It is the best total seen so far while walking through the list.
We update it whenever current_sum becomes bigger.
'''
# Example: current_sum = 4 → max_sum = 4; later current_sum = 7 → max_sum becomes 7.



'''
Q5. What question does Kadane ask at every number?
Ans:
“Should I continue my current streak, or start fresh from this number?”
'''
# Example: At x = 5 → compare:
# continue:  (current_sum + 5)
# restart:   (5)


'''
Q6. What is the final answer given by Kadane’s Algorithm?
Ans:
The final answer is max_sum: the highest sum of any continuous part of the list.
'''
# Example: [2, -1, 3, -4, 5] → max_sum = 5

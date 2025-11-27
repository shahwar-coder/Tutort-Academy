'''
Q1. What is a prefix sum in simple words?
Ans:
A prefix sum is a list of running totals. Each new number adds to the total so far.
'''
# Example:
# [2,3,5] → prefix = [2,5,10]



'''
Q2. Why do we make a prefix-sum list?
Ans:
To find the sum of part of an array quickly without adding everything again.
'''
# Example:
# Need sum of first 3 numbers? Prefix already gives it.



'''
Q3. How do you build a prefix-sum list?
Ans:
Start with the first number, then keep adding each number to the total you have.
'''
# Example:
# Start: 2 → add 3 → 5 → add 5 → 10



'''
Q4. What does prefix[i] tell us?
Ans:
It tells us the total sum from the beginning of the list up to index i.
'''
# Example:
# prefix[2] = sum of arr[0], arr[1], arr[2]



'''
Q5. How does prefix sum make range-sum easier?
Ans:
Because we can subtract earlier totals and get the answer instantly, instead of adding numbers one by one.
'''
# Example:
# Sum(1→3) = prefix[3] - prefix[0]



'''
Q6. Where do we commonly use prefix sums?
Ans:
In problems where we need to find sums of parts of an array many times.
'''
# Example:
# Games, scoring, and math questions that ask “sum from L to R”

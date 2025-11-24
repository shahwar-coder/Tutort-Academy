'''
Q1. Why does binary search divide the problem size by 2 every time?
Ans:
Because it checks the middle element first.
Depending on the comparison, it throws away either the left half or the right half.
So the remaining size becomes n/2 each step.
'''
# Example:
# n=32 → 16 → 8 → 4 → 2 → 1



'''
Q2. What equation represents how many steps binary search takes?
Ans:
After k steps, the remaining elements are:
n / 2ᵏ
Binary search stops when only 1 element remains:
n / 2ᵏ = 1
'''
# Example:
# Solve → n = 2ᵏ



'''
Q3. How do we solve n = 2ᵏ to find k?
Ans:
Take log base 2 on both sides:
k = log₂(n)
This gives the number of iterations needed.
'''
# Example:
# If n=1024 → k=10 steps



'''
Q4. What does k represent in binary search analysis?
Ans:
k is the total number of times we divide the list by 2
before the search range becomes size 1.
So k is the number of iterations binary search performs.
'''
# Example:
# Asking “How many halvings from n to 1?” → answer is log₂(n)



'''
Q5. Why does log₂(n) mean binary search is very fast?
Ans:
Because log₂(n) grows very slowly.
Even huge arrays require only a few steps.
'''
# Example:
# n = 1,000,000 → log₂ ≈ 20 steps!



'''
Q6. Why is the time complexity written as O(log n) and not log₂(n)?
Ans:
Because changing the log base only changes a constant factor,
and Big-O ignores constants.
So log₂(n), log₁₀(n), and ln(n) are all O(log n).
'''
# Example:
# log₁₀(n) = log₂(n) / log₂(10)
# The "1 / log₂(10)" constant is ignored.

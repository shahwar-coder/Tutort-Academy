'''
Q1. When can binary search be used on an array?
Ans:
Binary search works only when the array is **sorted**.
If the array is not sorted, the mid comparison becomes meaningless.
'''
# Example:
# Sorted → [2,4,7,9] → OK
# Unsorted → [7,2,9,4] → binary search gives wrong result



'''
Q2. How does binary search reduce the search space?
Ans:
It compares the middle element with the target
and removes **half the elements** every time.
'''
# Example:
# 32 elements → 5 steps (approx)



'''
Q3. What is the stopping condition for binary search?
Ans:
Stop when:
1) arr[mid] == target → found  
2) left > right → not found (range is empty)
'''
# Example:
# If left becomes 6 and right is 5 → search ends → “not found”



'''
Q4. Why is binary search O(log n)?
Ans:
Because each step removes half of the numbers.
Halving repeatedly forms a logarithmic pattern.
'''
# Example:
# 1,000,000 elements → ~20 steps (because 2^20 ≈ 1,000,000)



'''
Q5. What happens if you compute mid incorrectly?
Ans:
Using mid = (left + right) // 2 is fine for Python,
but in some languages it may overflow.
A safer formula is:
mid = left + (right - left) // 2
'''
# Example:
# In C++/Java, large left+right may overflow integer range.



'''
Q6. Can binary search work on descending-sorted arrays?
Ans:
Yes, but the comparison conditions must flip:
If arr[mid] < target → search the **left** half.
If arr[mid] > target → search the **right** half.
'''
# Example:
# Array: [50,40,30,20], target=30  
# Mid=40 → 40 > 30 → go right

'''
Q1. How do you safely copy a 2D array (matrix)?
Ans:
Use copy.deepcopy() for true independent copying.
Shallow copy only copies the outer list, not inner lists.
'''
# Example
import copy
M = [[1,2],[3,4]]
deep = copy.deepcopy(M)
deep[0][0] = 99

print(M)     # unchanged
print(deep)  # modified



'''
Q2. Why does [[0]*3]*4 cause bugs, and how does it work internally?
Ans:
Because it repeats the *same list reference* 4 times.
So modifying one row modifies all.
Internally: outer list has 4 pointers to the same inner object.
'''
# Example
bad = [[0]*3]*4
bad[0][1] = 7
print(bad)  # All rows contain 7 at index 1



'''
Q3. What is the right pattern to create an identity matrix or dynamically generated matrix?
Ans:
Use nested comprehensions because they create fresh rows each iteration.
'''
# Example
def identity(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

print(identity(4))



'''
Q4. How do you efficiently compute prefix sums and use them for fast range queries?
Ans:
Prefix[i] = sum(arr[0..i-1])
Range sum from l..r is: prefix[r+1] - prefix[l]
This makes each range query O(1).
'''

# Example array
arr = [3, 1, 4, 2]

# Step 0 — create a prefix list of size len(arr)+1, filled with 0
prefix = [0] * (len(arr) + 1)
print("Initial prefix:", prefix)
# Output: [0, 0, 0, 0, 0]

# Step 1 — fill prefix sums
# prefix[i+1] = prefix[i] + arr[i]
for i in range(len(arr)):
    prefix[i + 1] = prefix[i] + arr[i]
    print(f"After processing arr[{i}] = {arr[i]}, prefix becomes: {prefix}")

# Final prefix array
print("Final prefix array:", prefix)
# Output: [0, 3, 4, 8, 10]

# Step 2 — compute a range sum using prefix
l = 1
r = 2
range_sum = prefix[r + 1] - prefix[l]
print(f"Range sum arr[{l}:{r}] =", range_sum)
# Output: 5  (because 1 + 4 = 5)

# Step 3 — verify by normal summation
print("Normal sum:", sum(arr[l:r+1]))
# Output: 5


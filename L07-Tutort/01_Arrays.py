'''
Q1. What is an array?
Ans:
An array stores multiple items in order, all under one name.
It’s useful for keeping related data together (like numbers or names).
'''
# Example
marks = [85, 90, 78]     # A list of marks
print(marks[1])          # Access → 90  (O(1))



'''
Q2. How is a Python list different from a traditional array?
Ans:
A Python list is *dynamic* (size can grow or shrink) 
and can hold *mixed data types*.
Traditional arrays store one fixed type and have fixed size.
'''
# Example
data = [1, "hi", 3.5]    # Works fine → mixed types allowed
# In array.array → only one type allowed



'''
Q3. What is the use of array.array in Python?
Ans:
`array.array` is used when you need a fixed-type array 
that uses less memory than a Python list.
It’s ideal for numeric data where all items share one type.
'''
# Example
import array
nums = array.array('i', [1, 2, 3])   # 'i' means integer type
print(nums[0])                       # Output: 1



'''
Q4. Why is numpy.array so popular for numeric computing?
Ans:
`numpy.array` is super fast and efficient for math operations.
It uses C code under the hood, so it’s perfect for large numerical datasets.
'''
# Example
import numpy as np
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
print(A + B)     # [5 7 9] → elementwise addition



'''
Q5. What are the common time complexities for array operations?
Ans:
Access → O(1)  
Append → O(1) (amortized)  
Insert/Delete → O(n)  
Search → O(n)
'''
# Example
names = ["Amy", "Bob", "Cara"]
print(names[2])   # O(1) → direct access
# Searching "Cara" takes O(n)



'''
Q6. Why are inserts and deletes slower than access in arrays?
Ans:
Because elements must shift to maintain order.
For example, inserting at the front moves all items one step right.
'''
# Example
nums = [10, 20, 30]
nums.insert(0, 5)   # Shifts all → O(n)
print(nums)         # [5, 10, 20, 30]

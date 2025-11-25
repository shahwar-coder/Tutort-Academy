'''
Q1. How do two pointers reduce time from O(n²) to O(n)?
Ans:
They allow you to scan an array from two directions at once
instead of using nested loops.
So each element is touched only once.
'''
# Example:
# Checking pairs in a sorted array:
# Brute force → nested loops O(n²)
# Two pointers → left+right → O(n)



'''
Q2. Why do two-pointer solutions not need extra arrays?
Ans:
Because one pointer reads data and the other pointer writes or compares,
all inside the same array.
This keeps space complexity at O(1).
'''
# Example:
# Remove elements, move zeroes → done in-place.



'''
Q3. Why is two-pointer logic often cleaner?
Ans:
It turns complex “jumping around the array” logic
into simple pointer movements:
left++, right--, slow++, fast+=2, etc.
'''
# Example:
# Palindrome check:
# Compare s[left] and s[right], then move both inward.



'''
Q4. Why is the two-pointer technique so popular in interviews?
Ans:
It appears in many common patterns:
sorting, merging, filtering, searching, cycle detection.
Mastering it solves a wide range of problems quickly.
'''
# Example:
# Classic interview tasks:
# - 2-sum (sorted)
# - reverse vowels
# - remove duplicates
# - merge two sorted arrays



'''
Q5. What is the “efficiency mindset” behind two pointers?
Ans:
Avoid re-checking elements.
Each pointer moves only forward (or inward),
so the total work is minimal and predictable.
'''
# Example:
# Linked list cycle detection → slow & fast pointers
# Only a few moves instead of scanning endlessly.

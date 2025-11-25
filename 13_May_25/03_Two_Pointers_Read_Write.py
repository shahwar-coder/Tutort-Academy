'''
Q1. What is the Read–Write two-pointer pattern used for?
Ans:
It is used to filter elements:
• One pointer reads the array
• The other pointer writes only the “good” elements.
This keeps the array clean in-place.
'''
# Example:
# Remove all 3s from [3,2,2,3]
# i reads each element, j writes only 2s.



'''
Q2. How do the two pointers move in this pattern?
Ans:
i moves every step (reads each element).
j moves only when a valid element is found and written.
'''
# Example:
# nums[i] != val → copy to nums[j] → j++



'''
Q3. Why does this pattern not need extra space?
Ans:
Because the write pointer j overwrites unwanted values
inside the same array.
Only two integers (i and j) are used → O(1) space.
'''
# Example:
# nums becomes the modified output itself.



'''
Q4. What does the final value of j represent after the loop?
Ans:
j is the count of valid elements.
It also marks how many leading positions form the filtered result.
'''
# Example:
# [3,2,2,3], val=3 → result length j=2 → result: [2,2]



'''
Q5. What is the time complexity of this pattern and why?
Ans:
Time complexity is O(n)
because the read pointer i passes through the array once.
'''
# Example:
# One scan → no nested loops.

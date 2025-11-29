'''
Q1. Why do intermediate sliding-window problems need a frequency map?
Ans:
Because we must track how many times each character appears inside the window.
This helps us check conditions like “at most K distinct chars” or “no repeats.”
'''
# Example:
# freq = {'a':2,'b':1}
# Helps decide when to shrink.



'''
Q2. How do we detect duplicates in a window for “Longest Substring Without Repeating Characters”?
Ans:
If the incoming character already exists in the frequency map,
shrink from the left until its count becomes 1 again.
'''
# Example:
# "a b c a"
# a repeats → shrink left until window has only one 'a'.



'''
Q3. What condition defines the K-distinct sliding window problem?
Ans:
Keep expanding the window while distinct_count ≤ K.
If distinct_count becomes K+1 → shrink from the left until it returns to K.
'''
# Example:
# Window with {'a','b','c'} and K=2 → must shrink.



'''
Q4. In variable windows with frequency maps, what does removing arr[left] do?
Ans:
You reduce its count in the map.
If its count becomes 0, you remove it from the map to reduce distinct count.
'''
# Example:
# freq['b'] goes from 1 → 0 → remove key.



'''
Q5. Why do we track the maximum window size AFTER fixing the window condition?
Ans:
Because the window is valid only when the condition is satisfied.
We record the max length after ensuring the window meets the rules.
'''
# Example:
# longest substring without repeating → update max only when all counts ≤ 1.



'''
Q6. What is the standard template for variable sliding-window problems?
Ans:
1) Expand right and update frequency.
2) While the window is invalid → shrink left.
3) Update answer when window becomes valid.
'''
# Example:
# while distinct > k: shrink from left
# update max_len afterward.



'''
Q7. Why is sliding-window O(n) even though left and right both move?
Ans:
Because each pointer moves only forward and never comes back.
Each element is added once and removed once → total operations = 2n → O(n).
'''
# Example:
# right moves across array once; left also moves across once.

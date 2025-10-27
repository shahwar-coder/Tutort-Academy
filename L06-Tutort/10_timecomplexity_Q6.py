'''
Question 6:
Algorithm A and Algorithm B have worst-case running times of O(n) and O(log n),
respectively. Therefore, algorithm B always runs faster than algorithm A.

Options:
1. True
2. False
'''

# Answer False , for bigger inputs YES B will be better/faster than A (log n is better than n) but not for small inputs.
# Always keep in mind the growth of these.


'''
Q1. Does O(log n) always mean faster than O(n)?
Ans:
❌ No.  
Big-O only describes **how runtime grows as n increases**, not actual speed.  
An O(log n) algorithm *scales* better, but could still be slower for small inputs due to constants or overhead.
'''



'''
Q2. What does Big-O actually tell us?
Ans:
- It gives the **upper bound** on how runtime grows with input size.  
- It ignores constants and small terms → focuses on long-term scaling.
'''



'''
Q3. Why can an O(log n) algorithm be slower initially?
Ans:
- Hidden constants, setup overhead, or large base factors.
- Big-O doesn’t capture “real runtime,” only trend as n→∞.
'''



'''
Q4. What’s the correct way to interpret the comparison?
Ans:
- O(log n) means the runtime grows **slower** with input size.
- But “always faster” is wrong — you can only say:
  “Algorithm B is more scalable for large n.”
'''
# Step-by-step:
# Small n → constants matter → A might win.
# Large n → growth rate dominates → B wins.

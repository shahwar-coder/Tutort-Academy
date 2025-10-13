'''
Q1. What’s the difference between permutations and combinations conceptually?
Ans:
- **Permutations** → Order matters (AB ≠ BA)  
- **Combinations** → Order doesn’t matter (AB = BA)
'''
# Example
from itertools import permutations, combinations

data = ['A', 'B', 'C']
print(list(permutations(data, 2)))  # [('A','B'),('A','C'),('B','A'),('B','C'),('C','A'),('C','B')]
print(list(combinations(data, 2)))  # [('A','B'),('A','C'),('B','C')]



'''
Q2. What modules/functions provide these in Python?
Ans:
- Both are available in the built-in `itertools` module.
- permutations(iterable, r)
- combinations(iterable, r)
'''
from itertools import permutations, combinations



'''
Q3. What’s the mathematical meaning of r in these functions?
Ans:
- r → size of the subset taken at a time.
- e.g., permutations(data, 2) → all 2-length arrangements of data.
'''
data = [1, 2, 3]
print(list(permutations(data, 2)))  # All ordered pairs of 2 elements



'''
Q4. How do permutation and combination counts differ?
Ans:
- Permutations: nPr = n! / (n - r)!  
- Combinations: nCr = n! / [r! * (n - r)!]
'''
import math
n, r = 5, 3
print("Permutations:", math.perm(n, r))   # 60
print("Combinations:", math.comb(n, r))   # 10



'''
Q6. Quick shorthand
✔ permutations → order matters  
✔ combinations → order doesn’t  
✔ use itertools  
✔ combinations_with_replacement → allows repeats  
✔ use math.perm() / math.comb() for counts
'''

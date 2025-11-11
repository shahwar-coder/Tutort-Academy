'''
Q1. What is Asymptotic Notation?
Ans:
- It’s a mathematical tool to describe how an algorithm’s running time (or space) grows as input size (n) increases.
- It focuses on growth trend, not exact values — ignores constants and small terms.
'''
# Example:
T(n) = 3n**2 + 5n + 20
# Step-by-step:
# 1️⃣ As n → ∞, n² term dominates (others grow slower).
# 2️⃣ So we say: T(n) = O(n²)
# Meaning: runtime grows proportionally to n² in worst case.



'''
Q2. What are the main types of Asymptotic Notations?
Ans:
- O(f(n)) → Upper bound (worst-case growth)
- Ω(f(n)) → Lower bound (best-case growth)
- Θ(f(n)) → Tight bound (exact/average growth)
'''
# Example:
def linear_search(arr, x):
    for i in arr:
        if i == x:
            return True
    return False

# Step-by-step:
# Best case → found at start → Ω(1)
# Worst case → not found → O(n)
# Average → roughly halfway → Θ(n)



'''
Q3. Why do we ignore constants and small terms in asymptotic analysis?
Ans:
- Constants don’t affect growth trend for large inputs.
- As n → ∞, dominant term dictates performance.

Example: O(3n² + 5n + 20) = O(n²)
'''
# Step-by-step:
# For n = 1,000:
#   3n² = 3,000,000
#   5n  = 5,000 (negligible)
#   20  = constant (irrelevant)
# So smaller terms vanish in comparison → only n² matters.



'''
Q4. How are O, Ω, and Θ related to each other?
Ans:
- O → Upper bound: T(n) ≤ c·f(n)
- Ω → Lower bound: T(n) ≥ c·f(n)
- Θ → Tight bound: both O and Ω hold true.
'''
# Visual analogy:
# O(n²): algorithm never grows faster than n²
# Ω(n²): algorithm never grows slower than n²
# Θ(n²): algorithm grows roughly as fast as n²



'''
Q5. Why do we use asymptotic notation?
Ans:
✅ Hardware-independent → compares algorithms fairly.  
✅ Focuses on scalability.  
✅ Simplifies complex runtime formulas into meaningful growth patterns.
'''
# Example:
# Algorithm A: 2n log n ops
# Algorithm B: n² ops
# For small n, B may be faster (smaller constant).
# For large n, O(n log n) always scales better than O(n²).



'''
Q6. Quick shorthand:
✔ O → at most  
✔ Ω → at least  
✔ Θ → exactly (tight)  
✔ Ignores constants and small terms  
✔ Used for scalability analysis
'''

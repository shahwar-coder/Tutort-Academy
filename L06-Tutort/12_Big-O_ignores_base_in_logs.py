'''
Q1. Why does the base of a logarithm not matter in Big-O notation?
Ans:
Because logarithms of different bases differ only by a constant factor — and Big-O ignores constant multipliers.
'''
# Example:
# log₂(n) = log₁₀(n) / log₁₀(2)
# ⇒ log₂(n) = 3.3219 × log₁₀(n)
# Step-by-step:
# Base change only scales by 3.32 (a constant).
# In Big-O, O(3.32·log n) = O(log n)



'''
Q2. What is the mathematical identity behind this property?
Ans:
log_b(n) = log_k(n) / log_k(b)
- The denominator log_k(b) is a constant for fixed bases.
- Hence, changing bases only multiplies the value by a constant factor.
'''
# Example:
# log₂(8) = 3, log₁₀(8) = 0.903
# Relation: log₂(8) = log₁₀(8) / log₁₀(2)
# 3 ≈ 0.903 / 0.301 → ✅ works exactly



'''
Q2. What is the mathematical identity behind this property?
Ans:
log_b(n) = log_k(n) / log_k(b)
- The denominator log_k(b) is a constant for fixed bases.
- Hence, changing bases only multiplies the value by a constant factor.
'''
# Example:
# log₂(8) = 3, log₁₀(8) = 0.903
# Relation: log₂(8) = log₁₀(8) / log₁₀(2)
# 3 ≈ 0.903 / 0.301 → ✅ works exactly



'''
Q3. What does “constant factor” mean in Big-O analysis?
Ans:
- Constants scale time but do not affect growth rate.
- O(3·n) and O(n) grow identically as n → ∞.
'''
# Example:
T₁(n) = 2·log₂(n)
T₂(n) = log₁₀(n)
# As n grows, both increase slowly and at the same rate → O(log n)



'''
Q4. Why do we always write O(log n) instead of specifying the base?
Ans:
- Base doesn’t affect asymptotic growth.
- Writing O(log n) is a universal shorthand for logarithmic complexity.
- Whether binary, decimal, or natural log, they all grow proportionally.
'''
# Example:
# Binary search → O(log₂ n)
# Heap operations → O(log₂ n)
# We simply write → O(log n)



'''
Q5. Does the choice of base matter in practice (real runtime)?
Ans:
Only if constants matter for very small n.
As n grows large, log base differences fade — the curves are almost parallel.
'''
# Example comparison:
import math
for n in [10, 100, 1000, 1000000]:
    print(f"n={n} | log2={math.log2(n):.3f} | log10={math.log10(n):.3f}")

# n=10       log₂=3.322   log₁₀=1.000
# n=100      log₂=6.644   log₁₀=2.000
# n=1000     log₂=9.966   log₁₀=3.000
# n=1e6      log₂=19.931  log₁₀=6.000
# # The ratio log₂/log₁₀ ≈ 3.32 → constant factor only.



'''
Q6. Quick summary:
✔ log base only changes by a constant factor  
✔ O(log₂ n) = O(log₁₀ n) = O(logₑ n)  
✔ Constant multipliers are ignored in Big-O  
✔ We write O(log n) universally for logarithmic growth
'''

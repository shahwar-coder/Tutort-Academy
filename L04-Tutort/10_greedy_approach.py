'''
Q1. What is the core idea behind a Greedy Algorithm?
Ans:
- A greedy algorithm always makes the **best local (immediate) choice** at each step.
- It assumes that a series of locally optimal decisions will yield the **global optimum**.
'''
# Example: Coin Change (Indian coins)
coins = [50, 20, 10, 5, 2, 1]
amount = 63
used = []

for c in coins:
    while amount >= c:
        used.append(c)
        amount -= c

print(used)  # [50, 10, 2, 1]
# Step-by-step:
# 63 → pick 50 → 13 → pick 10 → 3 → pick 2 → 1 → pick 1 → done.



'''
Q2. What are two key properties required for a greedy algorithm to be correct?
Ans:
1️⃣ **Greedy-choice property** → Local choice leads toward global optimum.  
2️⃣ **Optimal substructure** → Optimal solution can be built from smaller optimal parts.
'''
Example:
Indian coins satisfy both — every greedy step (largest coin ≤ target)
helps reach the globally minimum coin count.



'''
Q3. What are some classic examples of greedy algorithms?
Ans:
- Coin Change (canonical denominations)
- Huffman Coding
- Kruskal’s or Prim’s MST algorithms
- Activity Selection (earliest finishing first)
'''
# Activity Selection Idea
activities = [(1, 2), (3, 4), (0, 6), (5, 7)]
# Sort by end time
activities.sort(key=lambda x: x[1])



'''
Q4. When does a greedy algorithm fail?
Ans:
- When a local optimum doesn’t lead to the global optimum.
- Example: non-canonical coin systems or knapsack problems.
'''



'''
Q5. Why are greedy algorithms preferred when applicable?
Ans:
- Simple, fast (O(n log n) or better)
- Intuitive and easy to implement
- Work well when problem satisfies greedy properties
'''
# Example: Selecting max non-overlapping intervals
# Just sort by finish time and greedily pick compatible ones



'''
Q6. Quick shorthand
✔ Local best = Greedy choice  
✔ Global best = Overall optimum  
✔ Works only when greedy property + optimal substructure hold  
✔ Fast, elegant, but not universal  
✔ Always verify correctness mathematically
'''

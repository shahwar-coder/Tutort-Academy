'''
MONOTONIC INCREASING vs MONOTONIC DECREASING STACKS  
Basic, intuitive Q/A set (Easy → Medium → Clear Understanding)

============================================================
Q1. What is the simple difference between an increasing and a decreasing monotonic stack?
Ans:
• Increasing stack → values go UP from bottom → top (like stairs going up).  
• Decreasing stack → values go DOWN from bottom → top (like stairs going down).

# Visual:
Increasing:  [1, 2, 4]
Decreasing: [9, 7, 5]

------------------------------------------------------------

Q2. How does the “pop condition” differ between the two?
Ans:
• Increasing stack → pop while new_value < stack_top  
  (because the new value breaks the “increasing” order)

• Decreasing stack → pop while new_value > stack_top  
  (because the new value breaks the “decreasing” order)

# Mnemonic:
→ New smaller → breaks increasing  
→ New bigger → breaks decreasing

------------------------------------------------------------

Q3. When should I use a monotonic **increasing** stack?
Ans:
Use an increasing stack when you are looking for a **smaller element** that appears later.

Typical problems:
• Next Smaller Element to the Right  
• Next Smaller Element to the Left  
• Histogram / rectangle areas (tracking next smaller bounds)

# Intuition:
Increasing stack waits for a **smaller value** to come and pop larger ones.

------------------------------------------------------------

Q4. When should I use a monotonic **decreasing** stack?
Ans:
Use a decreasing stack when you want to find a **greater element** that appears later.

Typical problems:
• Next Greater Element to the Right  
• Daily Temperatures  
• Stock Span (variation)

# Intuition:
Decreasing stack waits for a **bigger value** to come and pop smaller ones.

------------------------------------------------------------

Q5. What’s the REAL intuition behind choosing increasing vs decreasing?
Ans:
Ask yourself:
❓ "Do I want the next **greater** element?"  
→ Use a **decreasing** stack  
   (because a bigger value will pop smaller ones)

❓ "Do I want the next **smaller** element?"  
→ Use an **increasing** stack  
   (because a smaller value will pop larger ones)

# Summary:
Next GREATER → Decreasing stack  
Next SMALLER → Increasing stack

------------------------------------------------------------
'''

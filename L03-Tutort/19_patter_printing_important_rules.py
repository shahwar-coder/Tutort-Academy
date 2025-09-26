'''
Q1. What is the general structure of a pattern printing problem?
Ans:
- Most patterns are built from these three logical components:
   1. **Left Padding**: spaces to align the shape.
   2. **Payload**: the actual content (numbers, stars, letters).
   3. **Join Strategy**: how payload elements are separated (space, nothing, comma, etc.)
'''
# EXAMPLE:
'''
🧩 Question:
🔹Input:
6
🔹Output:
     1
    2 2
   3 3 3
  4 4 4 4
 5 5 5 5 5
6 6 6 6 6 6
'''
n=6
for i in range(1,n+1):
    raw_left_padding = " "*(n-i)
    payload = str(i)*i
    print(raw_left_padding + " ".join(payload))

'''
Here:
" " * (n - i)        → Padding
str(i) * i           → Payload
" ".join(payload)    → Join strategy
'''




'''
Q2. How do you decide the direction of padding?
Ans:
- Left padding is used when the pattern is right-aligned or centered.
- No padding needed for left-aligned patterns.

Example:
'''
Right-aligned:
    1
   2 2
  3 3 3   ← needs padding

Left-aligned:
1
2 2
3 3 3     ← no padding




'''
Q3. How do you control the payload content?
Ans:
- The payload is usually based on the loop variable `i` or its transformation.
- You might repeat:
   - a fixed symbol (e.g., "*")
   - a number (e.g., str(i))
   - a character (e.g., chr(64 + i) for A, B, C...)

Example:
'''
# Numbers
payload = str(i) * i

# Characters
payload = chr(64 + i) * i

# Asterisks
payload = "*" * i




'''
Q4. When do you use " ".join()?
Ans:
- Use `" ".join(payload)` when you want space-separated values.
- Without it, everything sticks together (e.g., 333 vs 3 3 3).
- Works only if payload is a sequence (string or list).

Example:
'''
" ".join("333") → "3 3 3"
" ".join(["*"]*3) → "* * *"



'''
Q5. Can this be done with one loop?
Ans:
- Yes, if:
   - The row can be built using only the loop index.
   - You avoid manually printing each element in an inner loop.
- Joining and string multiplication help reduce nested loops.

Example:
'''
for i in range(1, n+1):
    line = " " * (n - i) + " ".join(str(i) * i)
    print(line)





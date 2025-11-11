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


# I understand the padding + payload and join POWER for pattern printing but you can read below once.

'''
Step-by-step (for n=6):

For each row i from 1 to n:
1) Compute leading spaces:
   raw_left_padding = " " * (n - i)
   - For i=3, n=6 → "   " (3 spaces) to right-align the row.

2) Build the row’s content (the visible numbers):
   payload = str(i) * i
   - For i=3 → "333"
   " ".join(payload)
   - Treats "333" as ['3','3','3'] and inserts spaces → "3 3 3"

3) Concatenate and print the full line:
   raw_left_padding + " ".join(payload)
   - For i=3 → "   " + "3 3 3" → "   3 3 3"

Tip:
- For robustness (e.g., multi-digit tokens), prefer:
  items = " ".join([str(i)] * i)
  print(" "*(n-i) + items)
  This joins whole tokens, not characters.
'''


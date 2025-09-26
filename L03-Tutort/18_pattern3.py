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

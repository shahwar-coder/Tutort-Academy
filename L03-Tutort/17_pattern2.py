'''
🧩 Question:
🔹Input:
6

🔹Output:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
n=6
for i in range(1,n+1):
  for j in range(1,(n-i+1)+1):
    print(f"{j}", end=" ")
  print()

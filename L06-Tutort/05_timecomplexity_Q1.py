for (int i = 1; i <= m; i += c) {
   // constant-time work
}

for (int i = 1; i <= n; i += c) {
   // constant-time work
}

'''
for(i = 1; i <= m; i += c) → O(m) # actually m/c times but constant is dropped
for(i = 1; i <= n; i += c) → O(n) # actually n/c times but constant is dropped

Since loops are sequential → add them:
Total = O(m + n)

If m ≈ n, we say O(n).
Rule: sequential loops add; nested loops multiply.
'''

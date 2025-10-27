int a = 0;

for (i = 0; i < N; i++) {
    for (j = N; j > i; j--) {
        a = a + i + j;
    }
}

# ====== UNDERSTANDING =====

'''
Code:
for (i = 0; i < N; i++) {
    for (j = N; j > i; j--) {
        a = a + i + j;
    }
}

Outer loop: runs N times.
Inner loop: runs (N - i) times for each i.
Total = N + (N-1) + (N-2) + ... + 1 = N(N+1)/2 → O(N²)

✅ Time Complexity: O(N²)
✅ Space Complexity: O(1)
'''

int a = 0, b = 0;

for (i = 0; i < N; i++) {
    a = a + rand();
}

for (j = 0; j < M; j++) {
    b = b + rand();
}
'''
Options:
O(N * M) time, O(1) space
O(N + M) time, O(N + M) space
O(N + M) time, O(1) space
O(N * M) time, O(N + M) space
'''

# ==== UNDERSTANDING ====
'''
Code:
int a = 0, b = 0;
for(i = 0; i < N; i++) a = a + rand();
for(j = 0; j < M; j++) b = b + rand();

Time Complexity  = O(N + M)
Space Complexity = O(1)

Explanation:
- Each loop runs independently (sequential).
- Each loop body has constant-time work.
- Only a few fixed variables → constant space.
Rule: sequential loops add, nested loops multiply.
'''

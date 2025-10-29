# Problem 1:

int a = 0, b = 0;

for (i = 0; i < N; i++) {
    a = a + rand();
}

for (j = 0; j < M; j++) {
    b = b + rand();
}


'''SOLVING
int a = 0, b = 0; ----------------- O(1)

for (i = 0; i < N; i++) { --------- O(n)
    a = a + rand(); --------------- O(1)
}

for (j = 0; j < M; j++) { --------- O(m)
    b = b + rand(); --------------- O(1)
}

# Final : 
- Time Complexity -> O(m+n)
- Space Complexity -> O(1)
'''

# ==========================================

'''
Time Complexity Analysis:
• The statement "int a = 0, b = 0" is a single constant-time step → O(1)
• The first for-loop runs from 0 to N-1 → N iterations
    - Inside the loop only constant-time work is done → O(1)
    - Total for first loop → N * O(1) = O(N)
• The second for-loop runs from 0 to M-1 → M iterations
    - Inside the loop only constant-time work is done → O(1)
    - Total for second loop → M * O(1) = O(M)
• Final time complexity = O(N) + O(M) = O(N + M)
'''

'''
Space Complexity Analysis:
• Variables a, b, i, j all occupy a fixed amount of memory → O(1)
• No additional memory grows with input size
• No arrays, lists, or dynamic allocations used
• Final space complexity = O(1)
'''



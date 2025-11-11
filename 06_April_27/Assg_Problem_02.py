# Problem 2:

int a = 0;

for (i = 0; i < N; i++) {
    for (j = N; j > i; j--) {
        a = a + i + j;
    }
}

'''SOLVING
int a = 0;

for (i = 0; i < N; i++) { ----------- O(n)
    for (j = N; j > i; j--) { ------- when i=0 -> N times , i=1 -> N-1 times , i=2 -> N-2 times, so N+(N-1)+(N-2)+....+1 = N(N+1)/2 ~ N^2 Therefore O(N^2) 
        a = a + i + j; -------------- O(1)
    }
}
# Final:
- Time Complexity : O(N^2)
- Space Complexity : O(1)
'''

# =============================================================

'''
Time Complexity Analysis:
• The outer loop runs from i = 0 to N−1 → N iterations → O(N)
• The inner loop runs from j = N down to i+1
      - For i = 0 → runs N times
      - For i = 1 → runs (N−1) times
      - For i = 2 → runs (N−2) times
      - ...
      - For i = N−1 → runs 1 time
• Total operations = N + (N−1) + (N−2) + ... + 1
• This forms an arithmetic series = N(N + 1) / 2
• Simplified using Big-O notation → O(N²)
'''

'''
Space Complexity Analysis:
• Only variables a, i, j are used
• Count of variables does not grow with N
• No arrays or dynamic memory structures involved
• Space usage remains constant regardless of input size
• Overall space complexity → O(1)
'''

# Problem 3:

int a = 0, i = N;

while (i > 0) {
    a += i;
    i /= 2;
}

'''SOLVING
int a = 0, i = N;

while (i > 0) { ------------ O(log n) # for increments ir decrements like eg. i*=2 or i/=2 etc, time complexity is log n (base 2 here as we have 2)
    a += i;
    i /= 2;
}
# Final:
- Time Complexity -> O(log n)
- Space Complexity -> O(1)
'''

# ============================================================

'''
Time Complexity Analysis:
• The loop continues while i > 0
• Each iteration divides i by 2 → exponential decrease
• Number of iterations ≈ log₂(N)
• Only constant-time work inside the loop → O(1)
• Final time complexity → O(log N)
'''

'''
Space Complexity Analysis:
• Only variables a and i are used → fixed memory
• No extra data structures or memory allocation
• Space usage does not depend on input size
• Final space complexity → O(1)
'''


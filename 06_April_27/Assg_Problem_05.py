# Problem 5:

var value = 0;

for (var i = 0; i < n; i++) {
    for (var j = 0; j < i; j++) {
        value += 1;
    }
}

'''
Time Complexity Analysis:
• Outer loop: i goes from 0 to n−1 → n iterations → O(n)
• Inner loop: for a fixed i, j runs 0..i−1 → i iterations
• Total operations across all i:
    - Sum = 0 + 1 + 2 + ... + (n−1) = n(n−1)/2
• This arithmetic series grows quadratically with n
• Final time complexity → O(n^2)
'''

'''
Space Complexity Analysis:
• Variables used: value, i, j → constant number of scalars
• No arrays, lists, or dynamic allocations
• Space does not depend on n
• Final space complexity → O(1)
'''


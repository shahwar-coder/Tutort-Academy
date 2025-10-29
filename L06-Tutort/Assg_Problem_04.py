# Problem 4:

for (var i = 0; i < n; i++) {
    i *= k;
}

'''SOLVING
for (var i = 0; i < n; i++) { ------------- 
                                          |---------------> Over all : O(log n) # base is k
    i *= k; -------------------------------
}
# Final:
- Time Complexity: O(log n)
- Space Complexity: O(1)
'''

# ========================================================

'''
Time Complexity Analysis:
• Although the loop includes i++, multiplication by k dominates the growth
• i increases exponentially: i = i * k (approximately)
• Loop stops when i >= n → requires about logₖ(n) iterations , base of log can be ignored by Big-O
• Time Complexity → O(log n)

Space Complexity Analysis:
• Only variable i is used → constant memory
• Space Complexity → O(1)
'''

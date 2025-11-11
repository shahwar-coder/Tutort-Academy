int i, j, k = 0;

for (i = n / 2; i <= n; i++) {
    for (j = 2; j <= n; j = j * 2) {
        k = k + n / 2;
    }
}

'''
O(n)
O(n log n)
O(n²)
O(n² log n)
'''

#  ===== UNDERSTANDING =====

'''
Outer loop: i = n/2 → n → O(n)
Inner loop: j = 2 → n (multiply by 2 each time) → O(log n)

Total time = O(n × log n)
Space = O(1)

✅ Final Answer: O(n log n)
'''

'''
Q1. What is the purpose of the Sieve of Eratosthenes?
Ans:
- To efficiently find **all prime numbers up to a given limit n**.
- It avoids repeated divisions by systematically eliminating multiples.
'''
# Intuition example:
# For n = 10 → Start with all True
# Cross out multiples of 2 → 4, 6, 8, 10
# Cross out multiples of 3 → 6, 9
# Remaining: [2, 3, 5, 7]



'''
Q2. How does the sieve algorithm work step by step?
Ans:
1️⃣ Create a Boolean array of size n+1 (all True initially).  
2️⃣ Start from p = 2.  
3️⃣ For each prime p, mark all multiples (p*p, p*p+p, …) as False.  
4️⃣ Continue up to √n.  
5️⃣ Remaining True indices → primes.
'''
n = 10
# Initially: [True]*11
# p = 2 → mark 4,6,8,10
# p = 3 → mark 9
# Result primes = [2,3,5,7]



'''
Q3. Why do we start crossing out from p² instead of 2p?
Ans:
- Because smaller multiples (like 2p, 3p, …, (p-1)p)
  were already marked when processing smaller primes.
- It avoids redundant work → optimizes performance.
'''
Example: For p=5, 2×5=10, 3×5=15, 4×5=20 are already crossed by 2 and 3.
Start from 5×5=25.



'''
Q4. What is the time complexity of the Sieve of Eratosthenes?
Ans:
- O(n log log n)
- Much faster than checking each number individually (O(n√n)).
'''
# Because each composite number is marked a limited number of times — roughly proportional to n log log n.



'''
Q5. What are the main advantages and limitations of this sieve?
Ans:
✅ Advantages:
   - Very efficient for large n.
   - Easy to implement.  
🚫 Limitations:
   - Requires O(n) memory.
   - Not suitable for extremely large n (>10⁸) unless memory optimized.
'''



'''
Q6. Quick shorthand
✔ Mark multiples starting from p²  
✔ Stop at √n  
✔ O(n log log n) time  
✔ O(n) space  
✔ Simple yet powerful prime generator
'''

'''
204. Count Primes
https://leetcode.com/problems/count-primes/
'''


class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        limit=int(n**0.5)
        primes=[True]*n
        primes[0]=primes[1]=False
        for i in range(2, limit+1):
            for j in range(i*i, n, i):
                primes[j]=False
        return sum(primes)
      
# INTUITIVE BUT TO RECALL CAN READ BELOW:



'''
Detailed Flow & Reasoning — Sieve of Eratosthenes (countPrimes)

Goal: count primes strictly less than n.

1) Early exit
   • if n < 2: return 0
   • Reason: there are no primes < 2. This short-circuits trivial cases and simplifies the rest.

2) Initialize boolean array
   • primes = [True] * n
   • primes[0] = primes[1] = False
   • Meaning: index k is assumed prime (True) until proven composite (False).
   • Why length n? Problem asks for primes < n, so valid indices are 0..n-1.

3) Compute the loop bound (limit)
   • limit = int(n**0.5)
   • Reason: any composite number m has at least one factor ≤ sqrt(m). To mark all multiples < n,
     you only need to consider potential prime factors i up to √(n−1). Iterating beyond sqrt(n) is redundant.

4) Outer loop over potential primes i
   • for i in range(2, limit + 1):
       if primes[i]:   # (recommended guard)
           # inner marking...
   • Rationale: only start marking multiples when i is still flagged True (i is prime). If i is already False,
     its multiples were already marked by smaller primes.

5) Inner loop — mark multiples starting at i*i
   • for j in range(i*i, n, i):
         primes[j] = False
   • Why start at i*i?
     - Any multiple k = i * m with m < i was already marked earlier when processing factor m.
     - The first unmarked multiple that hasn't been addressed yet is i*i.
     - This reduces repeated work and is the key optimization of the sieve.
   • Why step by i?
     - We mark i*i, i*(i+1), i*(i+2), ... i.e., every multiple of i.

6) After loops — count remaining True entries
   • return sum(primes)
   • Each True corresponds to a prime < n.

---- Correctness intuition ----
• Initialization assumes primality; marking composites eliminates non-primes.
• Because every composite number has a smallest prime factor p ≤ √(composite),
  that composite will be marked when the sieve processes p. Therefore no composite remains unmarked.
• Remaining True entries must be primes.

---- Complexity ----
• Time: O(n log log n) (classic sieve bound). Practically very fast for n up to millions.
  - Outer loop up to √n, inner marking uses arithmetic progression marking which overall sums to n(1/2 + 1/3 + 1/5 + ...) ≈ n log log n.
• Space: O(n) for the boolean array.

---- Edge cases & correctness notes ----
• n small: n = 0 or 1 → function returns 0 immediately.
• n = 2 → primes = [True, False]? (we set size n; primes[0]=False, primes[1]=False, sum=0) → correct.
• Using range(i*i, n, i) ensures we never mark index ≥ n, preserving the "strictly less than n" invariant.

---- Micro-optimizations & trade-offs ----
• Guard `if primes[i]:` before inner loop — avoids unnecessary inner iterations for composite i.
• Skip even numbers after handling 2:
  - Mark all even indices False initially (except 2), then iterate i from 3..√n step 2 and mark j step 2*i.
  - Saves half the iterations (practical speedup) at cost of slightly more code.
• Slice assignment (primes[i*i:n:i] = [False]*k) can be compact and sometimes faster in CPython.
• Sieve uses O(n) memory — fine for LeetCode constraints, but if memory is very tight use segmented sieve.

---- Practical example (n = 30) — quick trace
• primes initially True for 0..29, then 0/1 set False.
• i = 2 (prime) → mark 4,6,8,...,28 False.
• i = 3 (prime) → mark 9,12,15,...,27 False.
• i = 4 (now False) → skip (guard avoids work).
• i = 5 (prime) → mark 25 (and 30 but outside range).
• stop when i > √29 (√29 ≈ 5.38 → limit = 5).
• sum True indices → primes are {2,3,5,7,11,13,17,19,23,29} → count = 10.

---- Final note ----
This implementation is the canonical and practical way to count primes < n. The critical ideas to remember:
• Build boolean mask for 0..n-1, mark multiples, start at i*i, loop i to √n, and guard on primes[i].
• These steps make the sieve both correct and efficient.
'''

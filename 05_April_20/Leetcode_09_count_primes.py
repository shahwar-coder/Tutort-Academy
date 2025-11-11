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

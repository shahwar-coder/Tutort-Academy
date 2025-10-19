'''
263. Ugly number
https://leetcode.com/problems/ugly-number/description/
'''

class Solution:
    desired_primes=(2,3,5)
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        for prime in self.desired_primes:
            while n%prime==0: #jab tak uss prime se katega , kaatte jaao.
                n//=prime
        return n==1



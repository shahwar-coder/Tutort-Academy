'''
Prime check is optimised now.

- <=1 , nothing Prime
- <=3, meaning 2 or 3, then of course Prime
- Everything divisible by 2 or 3, not Prime
- Why we start with i=5, because we have to test with pairs 6k-1 and 6k+1 (again, because prime numbers are either 1 before 6's multiple or 1 after 6's multiple)

6×1 − 1 = 5 ✅ prime
6×1 + 1 = 7 ✅ prime
6×2 − 1 = 11 ✅ prime
6×2 + 1 = 13 ✅ prime
6×3 − 1 = 17 ✅ prime
6×3 + 1 = 19 ✅ prime
'''

class Solution:
    def isPrime(self,n: int)->bool:
        """
        Check if number prime or not
        """
        if n<=1:
            return False
        if n<=3:
            return True
        if n%2==0 or n%3==0:
            return False
        i=5
        while i*i<n:
            if n%i==0 or n%(i+2): # i = 6k-1 and i = 6k+1 (both)
                return False
            i+=6
        return True

    def countSetBits(self, n: int)->int:
        """
        Count total 1's in bin form of the number : Total set bits
        """
        return n.bit_count()     


    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        Count Prime Set Bits
        """
        if left>right:
            return 0
        count=0
        for number in range(left, right+1):
            if self.isPrime(self.countSetBits(number)):
                count+=1
        return count

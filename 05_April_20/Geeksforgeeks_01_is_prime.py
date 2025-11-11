'''
Prime Number or not
https://www.geeksforgeeks.org/problems/prime-number2314/1
'''

class Solution:
    def isPrime(self, n):
        if n<=1:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return True

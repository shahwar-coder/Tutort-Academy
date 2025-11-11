'''
2160. Minimum sum of four digit number after splitting digits :
https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/
'''
'''
GREEDY APPROACH (Optimised version)
-> For fixed 4 digit number
-> Split of 2 dgts + 2 dgts will produce minimum sum
-> 10s place of num1 (smallest digit) then 10s place of num2 (second smallest digit)
-> common sense
'''

class Solution:
    def minimumSum(self, num: int) -> int:
        digit0 = num//1000
        digit1 = (num//100)%10
        digit2 = (num//10)%10
        digit3 = num%10

        ascending_digits=sorted([digit0, digit1, digit2, digit3])
        num1 = ascending_digits[0]*10+ascending_digits[2]
        num2 = ascending_digits[1]*10+ascending_digits[3]
        return num1 + num2



'''
🧩 Minimum Sum of Four-Digit Number — Greedy Flow

1️⃣  🔢 Extract each digit from the 4-digit input number.  
2️⃣  🧮 Sort the digits in ascending order.  
3️⃣  🧠 Greedy logic → 
     • Put smaller digits in the 10’s place of both numbers.  
     • Put larger digits in the 1’s place.  
     → Minimizes total sum.  
4️⃣  🧾 Form num1 = 10×d0 + d2, num2 = 10×d1 + d3.  
5️⃣  ➕ Return (num1 + num2) as the minimum possible sum.  
'''

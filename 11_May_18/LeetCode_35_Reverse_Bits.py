'''
Reverse Bits
https://leetcode.com/problems/reverse-bits/description/
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        bin_num = format(n, '032b')
        rev = bin_num[::-1]
        return int(rev, 2)



# Easy-to-Understand Key Points for “Reverse Bits”

# - Every input number is treated as a **32-bit binary number**.
# - First, convert the number into a 32-bit binary string:
#     format(n, '032b')
#     → ensures leading zeros are included.
# - Reverse the binary string using slicing:
#     rev = bin_num[::-1]
# - Convert the reversed binary string back to an integer:
#     int(rev, 2)
# - This gives the final result where all 32 bits have been flipped in order.
# - Time: O(32) → effectively constant time.
# - Space: O(32) → storing the 32-bit string.




# n = 56
# binary_32 = ""

# for i in range(31, -1, -1):   # loop from bit 31 → bit 0
#     bit = (n >> i) & 1
#     binary_32 += str(bit)

# print(binary_32)

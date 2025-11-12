'''
66. Plus One
https://leetcode.com/problems/plus-one/
'''
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(map(str, digits)))
        number+=1
        return list(map(int, list(str(number))))



# 💡 Approach Notes — Plus One
# -----------------------------
# 1️⃣ Input is a list of digits representing a non-negative integer.
#     Example: [1, 2, 3] → represents 123
#
# 2️⃣ Join all digits to form a string → "123"
#
# 3️⃣ Convert that string to an integer → 123
#
# 4️⃣ Add 1 → 124
#
# 5️⃣ Convert the new number back to string → "124"
#
# 6️⃣ Split each character and convert back to int → [1, 2, 4]
#
# ✅ Returns the updated list of digits.
#
# ⚙️ Time Complexity: O(n)
# 🧠 Space Complexity: O(n)

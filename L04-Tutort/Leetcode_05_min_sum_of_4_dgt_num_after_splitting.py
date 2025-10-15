'''
2160. Minimum sum of four digit number after splitting digits :
https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/
'''

class Solution:
    def to_number(self, tup: tuple)->int:
        return int(''.join(tup))

    def minimumSum(self, num: int) -> int:
        num_str=str(num)
        all_sum=[]
        all_unique_possible_arrangements = list(set(permutations(num_str, len(num_str))))
        for arrangement in all_unique_possible_arrangements:
            for index, _ in enumerate(arrangement): # _ as character won't be used, only index
                a=arrangement[:index]
                b=arrangement[index:]
                if len(a) and len(b): # helps discard the pairs where any one is empty
                    a=self.to_number(a)
                    b=self.to_number(b)
                    all_sum.append(sum([a,b]))
        return min(all_sum)



'''
🧩 Minimum Sum of Four-Digit Number — Flow

1️⃣  🔢 Convert input number → string of digits.  
2️⃣  ♻️ Generate all unique permutations of those digits (4! = 24 total).  
3️⃣  🔍 For each permutation →  
     • Split into two non-empty parts (a, b).  
     • Convert each to integer.  
     • Compute their sum and store it.  
4️⃣  🧮 After testing all possible splits of all permutations →  
     • Find and return the minimum sum value.  
'''

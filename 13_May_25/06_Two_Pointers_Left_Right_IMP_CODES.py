'''
Q. What types of problems does the Left–Right pattern solve?
Ans:
• Pair-sum problems  
• Check if array has two numbers matching a condition  
• Three-sum (after fixing one element)  
• Finding closest pair  
• Removing duplicates in sorted arrays
'''

# ────────────────────────────────────────────────────────
# 1) PAIR–SUM PROBLEM (classic)
# Example: check if any pair adds up to target
# --------------------------------------------------------
def has_pair_with_sum(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1
    return False


# ────────────────────────────────────────────────────────
# 2) CHECK IF TWO NUMBERS MATCH A CONDITION
# Example: check if any two numbers differ by exactly `k`
# --------------------------------------------------------
def has_pair_with_diff(nums, k):
    nums.sort()
    left, right = 0, 1

    while right < len(nums):
        diff = nums[right] - nums[left]
        if diff == k:
            return True
        elif diff < k:
            right += 1
        else:
            left += 1
            if left == right:
                right += 1
    return False


# ────────────────────────────────────────────────────────
# 3) THREE–SUM (after fixing one element)
# Example: find all triplets that sum to zero
# --------------------------------------------------------
def three_sum(nums):
    nums.sort()
    res = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1

    return res


# ────────────────────────────────────────────────────────
# 4) FINDING CLOSEST PAIR
# Example: two numbers whose sum is closest to target
# --------------------------------------------------------
def closest_pair(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    best = float('inf')
    pair = None

    while left < right:
        s = nums[left] + nums[right]
        if abs(s - target) < best:
            best = abs(s - target)
            pair = (nums[left], nums[right])

        if s < target:
            left += 1
        else:
            right -= 1

    return pair


# ────────────────────────────────────────────────────────
# 5) REMOVE DUPLICATES IN SORTED ARRAY
# Example: return new length after removing duplicates
# --------------------------------------------------------
def remove_duplicates(nums):
    if not nums:
        return 0

    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]

    return left + 1

'''
Q. When should you choose the Read–Write pattern?
Ans:
Use it when you need to:
• remove elements  
• compress/clean arrays  
• move valid items to the front  
• process arrays in-place  
without using extra memory.
'''
# ────────────────────────────────────────────────────────
# 1) REMOVE ELEMENTS
# Example: remove all occurrences of `val`
# --------------------------------------------------------
def remove_element(nums, val):
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:     # keep only non-val items
            nums[write] = nums[read]
            write += 1
    return write   # new length


# ────────────────────────────────────────────────────────
# 2) COMPRESS / CLEAN ARRAYS
# Example: remove all zeros
# --------------------------------------------------------
def remove_zeros(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:       # valid item
            nums[write] = nums[read]
            write += 1
    return write


# ────────────────────────────────────────────────────────
# 3) MOVE VALID ITEMS TO THE FRONT
# Example: move all even numbers to the front
# --------------------------------------------------------
def move_even_front(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] % 2 == 0:   # valid = even
            nums[write] = nums[read]
            write += 1
    return write   # count of evens placed in front


# ────────────────────────────────────────────────────────
# 4) PROCESS IN-PLACE
# Example: keep only values >= 5, and double them
# --------------------------------------------------------
def filter_and_double(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] >= 5:                 # valid condition
            nums[write] = nums[read] * 2     # processing in-place
            write += 1
    return write   # new useful length

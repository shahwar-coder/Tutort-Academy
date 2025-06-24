'''
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

ask:
Rewrite this function into a tail-recursive version using an extra parameter accumulator to carry the result.

✅ Your function should:
Be named tail_recursive_sum(n, acc)
Call itself with updated values and return the result directly (tail call)
Then, test it with print(tail_recursive_sum(5, 0))
(Expected output: 15)
'''

# TASK 1:
# First write the code for Recursive Sum:

def recursive_sum(num: int)->int:
    if num == 0:
        return 0
    return num + recursive_sum(num-1)

# TASK 2:
# Do the recursive sum problem using tail call.
def tail_recursive_sum(num: int, acc: int=0)->int:
    if num==0: # why this condition works and is important is ===>> ultimately the 'num' will be reduced to nothing which is "ZERO". And 'acc' has to be returned.
        return acc
    return tail_recursive_sum(num=num-1, acc=acc+num)

'''
- We reduce number one by one, eg. if num=56, we are doing , 56, 55, 54, 53.....
- And once we get 56, 55, 54, 53.... each time, we accumulate them in accumulator 'acc'
'''

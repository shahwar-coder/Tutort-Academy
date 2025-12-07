'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        answer=[0]*n

        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]: # loop till it finds a warmer temperature
                index=stack.pop()
                answer[index]=i-index
            stack.append(i)
        return answer


'''
### Core Idea (Monotonic Decreasing Stack)
We want to find, for each day, **how many days until a warmer temperature**.
Use a stack that keeps indices of temperatures in a **decreasing order**.
- When we find a warmer day, we pop the colder days from stack and update their result.

### How the Stack Is Used
Stack stores **indices** of unresolved days (waiting for a warmer day).
- If current temp is **higher** than the temp at the top index of stack:
    → we found a warmer day
    → compute difference in days and fill the answer
- Repeat until stack is again valid (decreasing)

### State Update While Iterating
For each index `i`:
- While stack not empty AND `temperatures[i] > temperatures[stack[-1]]`
    - Pop index → calculate `i - popped_index`
    - Store result in the answer array
- Push current index onto stack (still waiting for warmer day)

### Why Zeros in the End?
If no warmer day is found later,
- The answer remains **0** (as initialized)

### Final Answer
`answer` list where answer[i] = number of days to wait for a warmer day  
(or 0 if none exists)

### Why This Works
- Each index is pushed and popped **at most once**
- Stack ensures we only do useful comparisons
- Efficient solution vs. brute force pair checking

### Complexity
Time: O(n) → each index handled once  
Space: O(n) → stack + answer storage
'''


'''DRY-RUN
| Day (i) | Temp | Stack Before | Condition Check | Action Taken                        | Updated Answer    | Stack After |
| ------: | ---: | ------------ | --------------- | ----------------------------------- | ----------------- | ----------- |
|       0 |   73 | []           | —               | Push 0                              | [0,0,0,0,0,0,0,0] | [0]         |
|       1 |   74 | [0]          | 74 > 73 → True  | Pop 0 → answer[0] = 1−0 = 1, Push 1 | [1,0,0,0,0,0,0,0] | [1]         |
|       2 |   75 | [1]          | 75 > 74 → True  | Pop 1 → answer[1] = 2−1 = 1, Push 2 | [1,1,0,0,0,0,0,0] | [2]         |
|       3 |   71 | [2]          | 71 > 75 → False | Push 3                              | [1,1,0,0,0,0,0,0] | [2,3]       |
|       4 |   69 | [2,3]        | 69 > 71 → False | Push 4                              | [1,1,0,0,0,0,0,0] | [2,3,4]     |
|       5 |   72 | [2,3,4]      | 72 > 69 → True  | Pop 4 → answer[4] = 5−4 = 1         | [1,1,0,0,1,0,0,0] | [2,3]       |
|         |      | [2,3]        | 72 > 71 → True  | Pop 3 → answer[3] = 5−3 = 2         | [1,1,0,2,1,0,0,0] | [2]         |
|         |      | [2]          | 72 > 75 → False | Push 5                              | [1,1,0,2,1,0,0,0] | [2,5]       |
|       6 |   76 | [2,5]        | 76 > 72 → True  | Pop 5 → answer[5] = 6−5 = 1         | [1,1,0,2,1,1,0,0] | [2]         |
|         |      | [2]          | 76 > 75 → True  | Pop 2 → answer[2] = 6−2 = 4         | [1,1,4,2,1,1,0,0] | []          |
|         |      | []           | —               | Push 6                              | [1,1,4,2,1,1,0,0] | [6]         |
|       7 |   73 | [6]          | 73 > 76 → False | Push 7                              | [1,1,4,2,1,1,0,0] | [6,7]       |
'''

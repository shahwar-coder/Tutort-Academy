'''
933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/
'''

class RecentCounter:

    def __init__(self):
        self.timestamps = deque()

    def ping(self, t: int) -> int:
        self.timestamps.append(t)

        while self.timestamps[0]<t-3000: # we directly remove te timestamps that won't fall in the new range, older ones, we pop them out.
            self.timestamps.popleft()

        return len(self.timestamps)

            
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


'''
### Problem in Simple Words
You keep calling `.ping(t)` with increasing timestamps `t`.
You must return **how many calls happened in the last 3000 ms**:
that means in the range:
    [t - 3000, t]

Any older calls are no longer counted.

---

### Core Idea (Sliding Window Using Queue)
Use a **queue (deque)** to store timestamps of recent calls.
Since `t` is always increasing:
- Newest calls go to the **right**
- Remove old timestamps from the **left**

This automatically keeps only the timestamps that are still valid.

---

### Why Removing from the Left Works
`deque` pops from the left efficiently → O(1)
And since timestamps are **sorted by arrival**:
- The oldest timestamps are always in front
- Just remove them while they fall outside the valid range:
  any `timestamp < t - 3000` must be discarded

After cleanup, the queue size = number of valid recent calls

---

### Execution Flow of `ping(t)`
1️⃣ Append the new timestamp  
2️⃣ Remove timestamps **older than 3000 ms**  
3️⃣ Return how many timestamps remain inside the window

---

### Why This Approach Is Good
- Every timestamp enters and leaves once → **efficient**
- No need to re-check entire history
- Maintains a clean sliding window of recent calls

---

### Complexity
Time: O(1) amortized per ping  
Space: O(n) → number of timestamps in the last 3000 ms
'''

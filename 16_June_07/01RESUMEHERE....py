'''
1482. Minimum Number of Days to Make m Bouquets
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
'''

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # we need m bouquets
        # each bouquets should have k adjacent flowers
        # m*k flowers are needed (visualise with no overlap)

        if m*k>len(bloomDay):
            return -1

        def bouquetsOnThatDay(day: int):
            """
            On that day how many bouquests can be formed?
            """
            blooms=0
            bouquets=0
            for d in bloomDay:
                if d<=day:
                    blooms+=1
                    if blooms==k:
                        bouquets+=1
                        blooms=0
                else:
                    blooms=0
            return bouquets

        minDay = min(bloomDay)
        maxDay = max(bloomDay)
        # Below part can be replaced with binary search as linear sorted days...
        # for day in range(minDay, maxDay+1): # eg. for this [7,7,7,7,12,7,7], we need to run 7 -> 12
        #     if bouquetsOnThatDay(day)>=m:
        #         return day

        # binary search for optimisation
        while minDay<=maxDay:
            mid = (minDay+maxDay)//2
            if bouquetsOnThatDay(mid)>=m:
                result=mid
                maxDay=mid-1
            else:
                minDay=mid+1

        return result


'''
### Core Idea (Binary Search on Minimum Day)
We want the **earliest day** when we can make at least `m` bouquets.
- Each bouquet needs **k adjacent flowers**.
- A flower can be used only if it has bloomed (day >= its bloomDay).
- Instead of checking every day one by one, we **binary search** on the answer (the day).

### Feasibility Check: bouquetsOnThatDay(day)
For a given day:
- We walk through bloomDay from left to right.
- If bloomDay[i] ≤ day → this flower is bloomed:
    - Increase `blooms` (current streak of consecutive bloomed flowers).
    - If `blooms == k`:
        - We formed 1 bouquet → `bouquets += 1`
        - Reset `blooms = 0` (since those k flowers are used).
- If bloomDay[i] > day:
    - Reset `blooms = 0` (streak breaks, adjacency resets).
- At the end, `bouquets` = how many bouquets we can form on that day.

### Early Impossibility Check
- We need `m` bouquets, each of size `k`.
- Total flowers needed = `m * k`.
- If `m * k > len(bloomDay)`:
    - Not enough flowers in total → return -1 immediately.

### Binary Search Range (Search Space)
- The earliest possible day is `minDay = min(bloomDay)`  
  (before this, not even the first flower can bloom).
- The latest possible day is `maxDay = max(bloomDay)`  
  (by this day, all flowers that ever bloom have bloomed).

We binary search over this range [minDay, maxDay].

### Binary Search Logic
While minDay <= maxDay:
- mid = (minDay + maxDay) // 2  → this is our "candidate" day.
- Check how many bouquets we can make on `mid`:
    - If bouquetsOnThatDay(mid) ≥ m:
        - It is **possible** to make enough bouquets by this day.
        - Try to see if we can do it **earlier**:
            - result = mid      (mid is a valid answer candidate)
            - maxDay = mid - 1  (search in the left half)
    - Else (bouquetsOnThatDay(mid) < m):
        - Too early, not enough bouquets possible.
        - We need a **later** day:
            - minDay = mid + 1  (search in the right half)

### Final Answer
- `result` will store the **smallest day** on which we can make at least `m` bouquets.
- Return `result`.

### Why This Works
- As day increases:
    - More flowers bloom.
    - The number of bouquets we can form **never decreases**.
- This makes the function “Can we make ≥ m bouquets on this day?” **monotonic**:
    - false, false, ..., false, true, true, ...
- A monotonic condition over a range is perfect for **binary search on the answer**.

### Complexity
Let:
- n = number of flowers = len(bloomDay).
- D = range of days = max(bloomDay) - min(bloomDay).

For each binary search step:
- We scan the array once inside bouquetsOnThatDay → O(n).

Total:
- Time: O(n * log D)  
- Space: O(1) extra space.
'''

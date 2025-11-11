'''
Q1. Why can’t sets be sliced or indexed in Python?
Ans:
- Because sets are **unordered collections**, their elements have no fixed position.
- Indexing/slicing requires order → sets don’t preserve one.
'''
s = {10, 20, 30}
# ❌ Error: 'set' object is not subscriptable
# print(s[0])



'''
Q2. How can you access elements from a set then?
Ans:
- You can loop over a set using for-loops.
- Or convert it to an ordered collection like a list.
'''
s = {1, 2, 3, 4}
for item in s:
    print(item)
# Order may differ each time



'''
Q3. How do you slice a set safely?
Ans:
- Convert to list first: list(myset)[start:end]
- But remember: the order depends on the list conversion, not the original set.
'''
s = {10, 20, 30, 40, 50}
print(list(s)[1:3])  # Example output: [20, 30] (order not guaranteed)



'''
Q4. What if you need a consistent slicing order?
Ans:
- Use sorted() before slicing — this gives a stable, predictable sequence.
'''
s = {50, 10, 30, 40, 20}
print(sorted(s)[1:4])  # [20, 30, 40]



'''
Q5. What’s a memory-efficient way to slice large sets?
Ans:
- Use itertools.islice() → it lazily slices without converting everything to a list.
'''
from itertools import islice

s = {10, 20, 30, 40, 50}
print(list(islice(s, 2, 4)))  # Slices 2nd to 4th element (in iteration order)



'''
Q6. Quick shorthand
✔ Sets = unordered → no slicing/indexing  
✔ Convert to list() for slicing  
✔ Use sorted() for stable order  
✔ Use islice() for lazy slicing  
✔ Be mindful: set order may vary between runs
'''


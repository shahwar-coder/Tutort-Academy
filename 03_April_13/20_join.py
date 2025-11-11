'''
Q1. What does join() do in Python?
Ans:
- Combines elements of a sequence into a single string.
- Uses the string it's called on as the separator.

Example:
'''
words = ["I", "love", "Python"]
print(" ".join(words))  # I love Python



'''
Q2. Why must elements be strings in join()?
Ans:
- join() can only combine strings.
- If you try joining numbers, it raises a TypeError.
'''
nums = [1, 2, 3]
# " ".join(nums)  → ❌ TypeError
print(" ".join(map(str, nums)))  # ✅ "1 2 3"



'''
Q3. How is join() the reverse of split()?
Ans:
- split() breaks a string into a list.
- join() stitches it back together.

Example:
'''
s = "a-b-c"
parts = s.split("-")        # ['a', 'b', 'c']
rejoined = "-".join(parts)  # 'a-b-c'



'''
Q4. How is join() better than manual string concatenation?
Ans:
- Efficient: avoids repeated string copies.
- Readable: shows clearly what joins what.

Example:
'''
names = ["Alice", "Bob", "Eve"]
print(", ".join(names))  # Alice, Bob, Eve

# Better than:
# result = names[0] + ", " + names[1] + ...




'''
Q5. Can join() be used with characters in a string?
Ans:
- Yes, since a string is an iterable of characters.

Example:
'''
print("-".join("abc"))  # a-b-c



'''
Q6. Quick shorthand
- "sep".join(iterable) → join with separator
- Use map(str, ...) if elements are not strings
- Efficient, readable, and very Pythonic
'''

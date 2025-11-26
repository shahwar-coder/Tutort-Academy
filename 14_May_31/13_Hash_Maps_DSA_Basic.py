'''
Q1. What is a hash map in DSA terms?
Ans:
A hash map is a data structure that stores key → value pairs and lets you access values in O(1) average time.
'''
# Example:
# mp["age"] = 22  → lookup is instant.



'''
Q2. How does a hash map find the location to store a key?
Ans:
It uses a hash function that converts the key into an index of an internal array.
'''
# Example:
# "apple" → hash → 31 → stored at index 31.



'''
Q3. What is a hash collision?
Ans:
A collision happens when two different keys produce the same index.
Hash maps handle this by chaining or open addressing.
'''
# Example:
# "cat" and "dog" both map to index 14 → stored in a small linked list (chaining).



'''
Q4. Why are basic operations O(1) on average?
Ans:
Because the hash function jumps directly to the correct index,
so no scanning or searching is needed.
'''
# Example:
# mp["id"] → directly fetched from its bucket.



'''
Q5. What common DSA tasks become easier with hash maps?
Ans:
Counting frequencies, checking duplicates, fast membership checks,
pair-sum problems, sliding windows, and grouping items.
'''
# Example:
# Seen-before check in O(1) → ideal for Two Sum and duplicate detection.



'''
Q6. What is the difference between key and value in a hash map?
Ans:
The key is what you search with, and the value is the data returned for that key.
Keys must be unique; values may repeat.
'''
# Example:
# "roll": 44, "age": 44 → both values = 44, but keys are different.



'''THINK OF DICTIONARY HERE
Q7. Why is hashing better than arrays for storing non-numeric keys?
Ans:
Arrays only use numeric indices, but hash maps can store any type of key
(strings, objects, etc.) by hashing them to a numeric index internally.
'''
# Example:
# mp["apple"] works, but arr["apple"] does not.

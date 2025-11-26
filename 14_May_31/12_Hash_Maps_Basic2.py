'''
Q1. Can we use words (like "apple") as keys in a normal array?
Ans:
No. Arrays only allow numbers as positions. Words don’t work as indexes.
'''
# Example:
# arr["apple"] → ❌ not allowed



'''
Q2. What kind of keys can a hash map use?
Ans:
A hash map can use any key—words, numbers, even pairs—because it converts them internally.
'''
# Example:
# mp["apple"], mp[101], mp[(2,3)] → all allowed



'''
Q3. Why do hash maps feel more “flexible” than arrays?
Ans:
Because arrays only let you use number positions, but hash maps accept many types of keys.
'''
# Example:
# array → arr[0]
# hash map → mp["fruit"]



'''
Q1. Why can arrays not use string keys?
Ans:
Arrays are built around numeric indices. They expect positions like 0,1,2,…  
Strings don’t map to those positions automatically.
'''
# arr["apple"] → invalid



'''
Q2. How do hash maps allow keys like "apple" or (2,3)?
Ans:
They run the key through a hash function, which converts it into a number used as the index.
'''
# "apple" → hash → number → placed in bucket



'''
Q3. What advantage do hash maps provide over arrays?
Ans:
Hash maps let you store and access data using meaningful keys, not just numbers.
'''
# mp["age"] is clearer than arr[3]



'''
Q4. Why is a hash map still fast even with non-numeric keys?
Ans:
Because hashing quickly converts any key into a numeric index in O(1) time.
'''
# "banana" → hash → stored immediately



'''
Q1. What structural limitation prevents arrays from using non-numeric keys?
Ans:
Arrays rely on contiguous memory, and accessing arr[k] means jumping to base + k offset.  
This only works if k is an integer.
'''
# arr["apple"] cannot compute memory offset



'''
Q2. How does a hash map overcome this limitation?
Ans:
A hash map uses a hash function to turn any key into an integer index, letting it store diverse key types.
'''
# key → hash → index → bucket



'''
Q3. Why do hash maps store key-value pairs instead of only values like arrays?
Ans:
Because multiple different keys may hash to the same index (collision),  
so the map stores both key and value to verify the correct entry.
'''
# bucket may contain: ("apple",50), ("cat","yes")



'''
Q4. How does hashing allow constant-time lookup even with complex keys?
Ans:
Because the hash function computes the bucket index in constant time,
and searching inside that bucket is short due to low collisions.
'''
# get("apple") → compute hash → jump to bucket → find value



'''
Q1. Is a set the same as a hash map?
Ans:
A set is like a hash map but without values.  
It only stores keys to check if something exists.
'''
# Example:
# set:     {"apple", "banana"}  → only keys
# hashmap: {"apple":50}        → key + value



'''
Q2. Is a set basically a hash map?
Ans:
Yes. A set works like a hash map that only stores keys and no values.  
Internally, it still uses hashing and buckets.
'''
# Example:
# In Python:
# set uses hashing → add("a"), check if "a" exists → O(1)



'''
Q3. Is a hash set implemented using the same structure as a hash map?
Ans:
Yes. A hash set is typically implemented using the same hash table as a hash map,
but each key maps to a dummy value (like True).  
This keeps lookup O(1) while storing only keys.
'''
# Example:
# Internal representation:
# "apple" → True
# "cat"   → True
# Value is irrelevant; only key presence matters.


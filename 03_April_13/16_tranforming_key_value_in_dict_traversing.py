'''
Q1. What is a dictionary comprehension?
Ans:
- A compact way to create or transform dictionaries using a for-loop inside curly braces.
- Syntax: {key_expr: val_expr for key, val in dict.items()}
'''
d = {"a": 1, "b": 2}
squared = {k: v**2 for k, v in d.items()}
print(squared)  # {'a': 1, 'b': 4}



'''
Q2. How can you filter items inside a dict comprehension?
Ans:
- Add an if-condition at the end to include only certain pairs.
'''
d = {"x": 1, "y": 5, "z": 3}
filtered = {k: v for k, v in d.items() if v > 2}
print(filtered)  # {'y': 5, 'z': 3}



'''
Q3. How can you transform only keys or only values?
Ans:
- Change the key or value expression accordingly.

Example:
'''
d = {"a": 1, "b": 2}
upper_keys = {k.upper(): v for k, v in d.items()}
doubled_vals = {k: v * 2 for k, v in d.items()}



'''
Q4. Can you use enumerate() inside a dict comprehension?
Ans:
- Yes, for index → value mappings.

Example:
'''
names = ["Tom", "Jerry"]
indexed = {i: name for i, name in enumerate(names)}
print(indexed)  # {0: 'Tom', 1: 'Jerry'}



'''
Q5. Quick shorthand
- {k:v for k,v in d.items()} → base form
- Add if to filter
- Change k or v expressions to transform
'''

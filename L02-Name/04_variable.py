'''
Q1. What is a variable in Python?
Ans:
- A variable is just a name (label) that refers to an object in memory.
- It does not hold the value directly; it points to it.

Example:
'''
x = 42
print(id(x))

# Step-by-step:
# 1. 42 (int object) created in memory.
# 2. Name x refers to that object.
# 3. id(x) shows memory reference (implementation detail).



'''
Q2. How does dynamic typing work with variables?
Ans:
- Python infers type when assigning, and you can rebind to another type later.

Example
'''

x = 10       # int
x = "ten"    # now str
print(x)

# Step-by-step:
# 1. First x → int object 10.
# 2. Then x rebinds to string "ten".



'''
Q3. What are the rules for naming variables?
Ans:
- Must start with a letter or underscore.
- Case-sensitive.
- Cannot be a reserved keyword.

Example:
'''
_valid = 123 #valid
Age = 25 #valid
# class = 5   # ❌ error: reserved keyword



'''
Q4. What’s the difference between variable rebinding and mutation?
Ans:
- Rebinding → variable points to a new object.
- Mutation → object changes, variable still points to the same one.

Example:
'''
# 🔑 Variable Rebinding vs Mutation

# • Rebinding → variable points to a new object.
# • Mutation  → object itself changes, variable still points to same object.

# --- Example of Mutation ---
lst = [1, 2]
lst2 = lst       # both point to same list
lst.append(3)    # mutates the list in place
print(lst2)      # [1, 2, 3]
# Reason: same object shared, so change is visible through both names.

# --- Example of Rebinding ---
lst = [1, 2]
lst2 = lst       # both point to same list initially
lst = [1, 2, 3]  # rebinding lst → new object
print(lst2)      # [1, 2]
# Reason: lst2 still points to old list, lst now points to a new one.




'''
Q5. How does multiple assignment work in Python?
Ans:
- Python supports tuple unpacking in assignment.

Example:
'''
a, b = 5, 10
print(a, b)

# Step-by-step:
# 1. RHS (5, 10) → tuple.
# 2. LHS unpacks → a=5, b=10.



'''
Q6. What happens when two variables reference the same object?
Ans:
- Both names point to the same memory object. Changing a mutable object through one name affects the other.

Example:
'''
a = b = [1, 2]
a.append(3)
print(b)

# Step-by-step:
# 1. a and b both point to same list.
# 2. append changes that list.
# 3. Both a and b see [1,2,3].



'''
Q7. Common pitfalls & best practices
Ans:
- Be careful with mutable defaults (e.g., in function arguments).
- Use descriptive variable names.
- Avoid shadowing built-ins (e.g., don’t name a variable list or dict).
'''

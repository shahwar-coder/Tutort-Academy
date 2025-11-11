# Logical Operators Demo

age = 20
has_id = True

print("Age:", age, ", Has ID:", has_id)

# Using 'and'
print("Eligible to vote (age >= 18 AND has ID):", age >= 18 and has_id)

# Using 'or'
print("Can enter hall (age >= 18 OR has ID):", age >= 18 or has_id)

# Using 'not'
print("Is underage (NOT age >= 18):", not (age >= 18))


# Age: 20 , Has ID: True
# Eligible to vote (age >= 18 AND has ID): True
# Can enter hall (age >= 18 OR has ID): True
# Is underage (NOT age >= 18): False

'''
📌 Summary – Logical Operators in Python  

- **Operators**:  
  - and → True if both conditions true.  
  - or  → True if at least one condition true.  
  - not → Negates condition (True ↔ False).  

- **Usage**: Combine conditions in decision making.  
- **Precedence**: 'not' > 'and' > 'or'.  
- **Note**: Can return truthy/falsy operands, not always strict True/False.  

🔑 Key Idea: Logical operators allow building complex conditions for control flow.  
'''

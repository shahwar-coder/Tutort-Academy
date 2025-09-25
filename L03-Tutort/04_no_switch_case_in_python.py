'''
Q1. Does Python have a switch-case statement?
Ans:
- No traditional switch-case like C/Java.
- Python offers alternatives: if-elif-else, dict mapping, match-case (3.10+).
'''



'''
Q2. How can if-elif-else replace switch?
Ans:
- Good for small sets of conditions.
- Readable but can get long.

Example:
'''
day = 3
if day == 1:
    print("Mon")
elif day == 2:
    print("Tue")
elif day == 3:
    print("Wed")
else:
    print("Other")

# Step-by-step:
# Checks sequentially until match (day==3 → "Wed").




'''
Q3. How can a dict be used as a switch replacement?
Ans:
- Map keys to results or functions.
- Cleaner than multiple if-elif.

Example:
'''
def mon(): return "Mon"
def tue(): return "Tue"
def wed(): return "Wed"

switch = {1: mon, 2: tue, 3: wed}
print(switch.get(3, lambda: "Other")())

# Step-by-step:
# switch[3] → wed function.
# Call it → "Wed".



'''
Q4. What is match-case (Python 3.10+)?
Ans:
- Structural pattern matching.
- Closest to switch-case but more powerful.

Example:
'''
day = 2
match day:
    case 1: print("Mon")
    case 2: print("Tue")
    case 3: print("Wed")
    case _: print("Other")

# Step-by-step:
# match checks case 2 → prints "Tue".



'''
Q5. When should each approach be used?
Ans:
- if-elif-else → beginners, simple conditions.
- dict mapping → when mapping keys to values/actions.
- match-case → Python 3.10+, for cleaner & more advanced pattern checks.
'''



'''
Q6. Quick shorthand
- No switch in Python.
- Use: if-elif-else, dict mapping, or match-case.
- Dict = efficient, match-case = modern & powerful.
'''

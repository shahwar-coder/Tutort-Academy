'''
Q1. What is match-case in Python?
Ans:
- A control structure introduced in Python 3.10.
- Works like switch-case but more powerful (supports patterns and destructuring).
'''
x = 2
match x:
    case 1: print("One")
    case 2: print("Two")
    case _: print("Other")

# Step-by-step:
# match x → value is 2 → matches case 2 → prints "Two".



'''
Q2. How do you use multiple values in one case?
Ans:
- Use "|" (OR) to match multiple possibilities.

Example:
'''
day = "Sat"
match day:
    case "Sat" | "Sun":
        print("Weekend")
    case _:
        print("Weekday")

# Step-by-step:
# "Sat" matches "Sat" | "Sun" → prints "Weekend".



'''
Q3. How does match-case act as a default?
Ans:
- case _ acts as the fallback branch.

Example:
'''
color = "purple"
match color:
    case "red": print("Stop")
    case "green": print("Go")
    case _: print("Unknown")

# Step-by-step:
# color="purple" → no case match → falls to case _.



'''
point = (0, 5)
match point:
    case (0, y): print(f"On Y-axis at {y}")
    case (x, 0): print(f"On X-axis at {x}")
    case (x, y): print(f"Point {x},{y}")

# Step-by-step:
# Matches (0,y) → y=5 → prints "On Y-axis at 5".
'''
point = (0, 5)
match point:
    case (0, y): print(f"On Y-axis at {y}")
    case (x, 0): print(f"On X-axis at {x}")
    case (x, y): print(f"Point {x},{y}")

# Step-by-step:
# Matches (0,y) → y=5 → prints "On Y-axis at 5".



'''
Q5. Can match-case work with guards (conditions)?
Ans:
- Yes, add "if condition" to refine a case.

Example:
'''
num = 7
match num:
    case n if n % 2 == 0: print("Even")
    case n: print("Odd")

# Step-by-step:
# num=7 → case n if n%2==0 fails.
# Falls to case n → prints "Odd".



'''
Q6. Why is match-case better than if-elif in some cases?
Ans:
- Cleaner for many options.
- Supports structural pattern matching (like tuple unpacking).
- More readable for complex branching.
'''


'''
Q7. Quick shorthand
- match-case = modern switch + patterns.
- "|" for multiple values.
- "_" = default.
- Supports destructuring + guards.
'''

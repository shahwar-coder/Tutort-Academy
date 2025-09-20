'''
Q1. What is the role of control structures in Python?
Ans:
- Control structures decide the flow of execution.
- Without them, code would run strictly top-to-bottom.

Example:
'''
x = 5
if x > 0:
    print("Positive")
print("Done")

# Step-by-step:
# 1. Check condition → True → prints "Positive".
# 2. Always prints "Done".



'''
Q2. How do conditional statements work (if/elif/else)?
Ans:
- Decide between branches of code.
- Only one branch in the chain runs.

Example:
'''
score = 85
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
else:
    print("C")

# Step-by-step:
# 1. 85 >= 90 → False
# 2. 85 >= 75 → True → "B"
# 3. Else skipped.



'''
Q3. How does a for loop work in Python?
Ans:
- Iterates directly over sequences or iterables.
- Cleaner than indexing manually.

Example:
'''
for ch in "hi":
    print(ch)

# Step-by-step:
# 1. Take first char "h".
# 2. Then "i".



'''
Q4. How does a while loop work?
Ans:
- Repeats until condition is False.
- Useful when number of iterations unknown.

Example:
'''
x = 3
while x > 0:
    print(x)
    x -= 1

# Step-by-step:
# 1. x=3 → prints 3 → x=2
# 2. x=2 → prints 2 → x=1
# 3. x=1 → prints 1 → x=0 → loop ends.



'''
Q5. What does break do inside loops?
Ans:
- Exits the loop immediately.

Example:
'''
for i in range(5):
    if i == 3:
        break
    print(i)

# Step-by-step:
# 1. Prints 0,1,2.
# 2. At i==3, break exits loop → stops completely.



'''
Q6. What does continue do inside loops?
Ans:
- Skips current iteration, continues with next.

Example:
'''
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

# Step-by-step:
# 1. i=0 → even → continue (skip print).
# 2. i=1 → odd → print 1.
# 3. Repeats → prints 1,3.



'''
Q7. What is loop-else and how is it useful?
Ans:
- else after loop runs only if loop ends without break.
- Useful for search tasks.

Example:
'''
nums = [2,4,6]
for n in nums:
    if n % 2 != 0:
        print("Odd found")
        break
else:
    print("All even")

# Step-by-step:
# 1. Loop checks each n.
# 2. No break (all even).
# 3. else runs → "All even".



'''
Q8. How can control structures be nested?
Ans:
- You can place if inside loop, loop inside if, etc.
- Indentation defines scope.

Example:
'''
for i in range(3):
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")

# Step-by-step:
# 1. i=0 → even → print.
# 2. i=1 → odd → print.
# 3. i=2 → even → print.

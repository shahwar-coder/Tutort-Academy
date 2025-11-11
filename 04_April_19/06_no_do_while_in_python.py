'''
Q1. Why doesn’t Python have a native do-while loop?
Ans:
- Python’s philosophy prefers clarity and avoids redundant loop types.
- The `while True: ... if not condition: break` idiom covers all do-while needs.
'''
# Classic do-while equivalent in Python
while True:
    print("Runs at least once")
    if False:
        break



'''
Q2. How does a simulated do-while loop differ from a normal while loop?
Ans:
- Normal while → checks condition *before* running.
- Simulated do-while → runs *once before* checking.
'''
# while loop
x = 0
while x > 0:
    print("Never runs")

# do-while simulation
x = 0
while True:
    print("Runs once before check")
    if x > 0:
        break
    break



'''
Q3. When is a do-while style loop useful?
Ans:
- When the loop must run at least once before condition check:
   • Menus / input validation
   • Retry systems
   • Dynamic game or simulation loops
'''
while True:
    pwd = input("Enter password: ")
    if pwd == "admin":
        print("Access granted")
        break
    print("Try again!")



'''
Q4. What’s the key logic pattern behind do-while in Python?
Ans:
- Infinite loop + break based on condition.
- Body executes first → condition checked after.
'''
while True:
    # do something
    if not condition:
        break



'''
Q5. What are common mistakes in simulating do-while?
Ans:
- Forgetting the `break` → infinite loop.
- Checking condition before body → acts like normal while.
'''
# ❌ Wrong — condition checked first
while condition:
    ...

# ✅ Correct — run first, then check
while True:
    ...
    if not condition:
        break



'''
Q6. Quick shorthand
- Python lacks native do-while  
- Simulate using while True and break  
- Guarantees one execution  
- Ideal for menus, input, retries
'''

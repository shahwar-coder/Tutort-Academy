'''
Q1. How does a while loop differ from a for loop in Python?
Ans:
- for → used when the number of iterations is **known** or finite.
- while → used when iteration continues until a **condition becomes false**.
'''
# for: known range
for i in range(3):
    print(i)   # 0 1 2

# while: unknown stop time
i = 0
while i < 3:
    print(i)
    i += 1



'''
Q2. Why is while more flexible?
Ans:
- It doesn’t depend on a predefined sequence or range.
- Great for loops where the end condition depends on user input, state, or data.
'''
password = ""
while password != "admin":
    password = input("Enter password: ")
print("Access granted")
# yahan input mein hi phasa diye hain, jab tak sahi nahi daalega, user se input poochte rahega hamesha...


'''
Q3. What are common use cases for while loops?
Ans:
- Reading input until a condition fails  
- Simulations with dynamic states  
- Infinite loops (with break)  
- Polling or waiting for events
'''
count = 0
while True:
    print(count)
    count += 1
    if count == 3:
        break



'''
Q4. What are potential pitfalls with while loops?
Ans:
- Risk of **infinite loops** if condition never becomes False.
- Must manually update loop variables inside the loop.
'''



'''
Q5. When should you prefer for vs while?
Ans:
- for → when you know the range or dataset beforehand.  
- while → when condition depends on runtime logic or variable change.
'''
# for → pattern generation
for i in range(1, 6):
    print("*" * i)

# while → continue until condition fails
n = 5
while n > 0:
    print("*" * n)
    n -= 1




'''
Q6. Quick shorthand
- while → condition-based iteration  
- for → sequence/range iteration  
- Always ensure condition changes inside while  
- Use break for manual exits
'''

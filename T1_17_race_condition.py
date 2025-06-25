'''
- RACE CONDITION
- A race condition happens when two or more parts of your code (like threads or processes) try to access or modify the same shared data at the same time, and the final result depends on who gets there first.
- It’s like two people trying to write on the same whiteboard at the same time — someone’s work gets messed up.

| Concept          | Meaning                                                    |
| ---------------- | ---------------------------------------------------------- |
| Race condition   | When two things change the same data at once, causing bugs |
| Where it happens | In threading, multiprocessing, even asyncio if not careful |
| Fix it with      | Locks (`threading.Lock()`), queues, or message passing     |
| Common symptoms  | Wrong results, crashes, works sometimes but not always     |

'''

# Example

import threading

counter = 0

def increase():
    global counter
    print("Reading:", counter)
    counter += 1
    print("Writing:", counter)

t1 = threading.Thread(target=increase)
t2 = threading.Thread(target=increase)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final counter:", counter)


'''
Reading: 0
Reading: 0
Writing: 1
Writing: 1
Final counter: 1  ❌ (should have been 2)
'''

'''
Let’s now fix the ultra-simple race condition using a Lock — to make sure only one thread can access the shared variable at a time.
'''

import threading

counter = 0
lock = threading.Lock()

def increase():
    global counter
    with lock:  # 🔐 only one thread allowed in this block at a time
        print("Reading:", counter)
        counter += 1
        print("Writing:", counter)

t1 = threading.Thread(target=increase)
t2 = threading.Thread(target=increase)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final counter:", counter)


# Final Correct Approach with Lock (OUTPUT):

'''
Reading: 0
Writing: 1
Reading: 1
Writing: 2
Final counter: 2  ✅
'''

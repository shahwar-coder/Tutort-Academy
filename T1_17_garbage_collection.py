'''
1. GARBAGE COLLECTION
- GC
- Garbage Collection : Automatic Memory Cleanup

2. GC in Python perspective
- Python automatically finds the unused/ unreachable variables/objects and frees their memory so your program does not run out of RAM
- You do not need to manually delete objects (Python does this for you)
'''

'''
HOW DOES IT WORK ?
'''
'''
1. REFERENCE COUNTING:
- Every object has a count of how many variables point to it.

2. CYCLE DETECTOR (not discussed here)
'''
a = [1, 2, 3]  # ref count = 1
b = a          # ref count = 2
del a          # ref count = 1
del b          # ref count = 0 → object destroyed!

'''
- When the reference count becomes 0, Python deletes the object immediately
- Simple, Fast, Automatic
'''

# Quick Demo 

import gc

class MyClass:
    def __del__(self):
        print("Object Deleted!!")

def create_object():
    obj = MyClass()

create_object() # Output: Object destroyed

'''
🧠 Flow / Explanation:
- `obj` is created inside the function.
- Once the function ends, there's no more reference to it.
- Python calls __del__() and deletes it automatically.
✅ Garbage collection happened silently!
'''


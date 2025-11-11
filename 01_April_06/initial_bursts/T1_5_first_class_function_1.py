'''
- first class function
- it is a function which is treated like another variable
- you can:
    - assign functions to variables
    - pass them a s arguments to other functions
    - return them from other functions
    - store them in data structures
- functions are the "First-Class-Citizens" in python
'''

# Example 1 (Assigning a function to a variable)
def read_my_name(name: str)->str:
    """Read my name aloud"""
    return name

engineer=read_my_name

print(engineer("Shahwar"))



# Example 2 (Passing function as an argument):
def shout(text: str)->str:
    """Shout out loud"""
    return text.upper()

def whisper(text: str)->str:
    """Only whisper"""
    return text.lower()

def speak(func, text):
    """Use incoming function with the parameter"""
    return func(text)

print(speak(shout, "ShAhWaR"))
print(speak(whisper, "ShAhWaR"))


# Example 3 (Returning a function from a function)
def sound_maker():
    def make_sound():
        print("Beep!!!")
    return make_sound

# use
alarm=sound_maker()
alarm()

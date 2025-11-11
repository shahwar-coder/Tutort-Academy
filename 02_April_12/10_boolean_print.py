'''
Q. Take a boolean and print:
'''
bool_map={"1": True, 
           "0": False, 
           "true": True, 
           "false": False}

user_input = input("Enter a Boolean Value: ").strip().lower()

result = bool_map.get(user_input, None)

if result is not None:
  print("Your Boolean Value is : ", result)
else:
  print("Not a Boolean!")



'''
Summary: Boolean Input and Print

Approach:
- Normalize user input with strip() and lower().
- Use a dictionary (bool_map) to map valid string inputs ("true","false","1","0") to actual booleans.
- Lookup input in dictionary with get(); default to None if not found.
- If result is not None, print the boolean value; else print "Not a Boolean!".

Key Points:
- Handles case-insensitivity and whitespace.
- Converts specific string inputs to real boolean type.
- Dictionary makes the code clean, extensible, and efficient (O(1) lookup).
'''

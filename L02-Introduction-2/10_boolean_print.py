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



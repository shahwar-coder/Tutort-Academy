'''
Q. Take a boolean and print:
'''
bool_book={"1": True, 
           "0": False, 
           "true": True, 
           "false": False}
bool_value = input("Enter a Boolean Value: ").strip().lower()
result = bool_book.get(bool_value, None)
if result is not None:
  print("Your Boolean Value is : ", result)
else:
  print("Not a Boolean!")



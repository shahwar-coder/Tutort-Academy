'''
Q. For the given data, print cleaned data, removing what ever is not valid finite numbers
'''

import math
# data = [1, 2, 3.0, 4.23, nan, None, inf, -inf, 5.0]
data = [1, 2, 3.0, 4.23, math.nan, math.inf, -math.inf, 5.0] #that's how you write nan, inf, -inf (not directly)
cleaned_data = [datum for datum in data if math.isfinite(datum)]
print(f"data : {data}")
print(f"cleaned_data : {cleaned_data}")

# There can be advancements in program by making reusable functions eg. def clean_numbers
# You can check for types first as well, in case the list has, None, etc

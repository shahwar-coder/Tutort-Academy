'''
Replacement for:
1. Switch Cases/ Match Case
2. If else chains
'''

day = "Sat"

day_map = {
    "Mon": "Workday",
    "Tue": "Workday",
    "Wed": "Workday",
    "Thu": "Workday",
    "Fri": "Workday",
    "Sat": "Weekend",
    "Sun": "Weekend",
}

message = day_map.get(day, "Unknown day")
print(message)  # Weekend


'''
Why this is nice:
- No repeated `if` conditions.
- Easy to add/change a mapping without touching control flow.
- `.get(..., default)` provides the default case.
'''

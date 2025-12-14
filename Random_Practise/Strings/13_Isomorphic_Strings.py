'''
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/description/
'''
class Solution:
    def map_check(self, txt1: str,txt2: str, char_map: dict)->bool:
        for i in range(len(txt1)):
            if txt1[i] not in char_map:
                char_map[txt1[i]]=txt2[i]
            else:
                if char_map.get(txt1[i]) != txt2[i]:
                    return False
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        # We need to check map in both directions.
        char_map_s_to_t = {}
        char_map_t_to_s = {}

        return (
            self.map_check(txt1=s, txt2=t, char_map=char_map_s_to_t) 
            and
            self.map_check(txt1=t, txt2=s, char_map=char_map_t_to_s)
        )


'''
### Problem in Simple Words
Two strings `s` and `t` are **isomorphic** if:
- Each character in `s` can be replaced to get `t`
- The replacement must be **consistent**
- No two different characters can map to the same character

Example:
- `"egg"` → `"add"` ✅
- `"foo"` → `"bar"` ❌
- `"paper"` → `"title"` ✅

---

### Core Idea (Character Mapping)
We check whether characters from one string can be mapped to the other **one-to-one**.

Important rule:
- One character → one fixed character
- Mapping must be **unique in both directions**

That’s why we check mappings **both ways**.

---

### Why Two Maps Are Needed
Only checking `s → t` is **not enough**.

Example:
- `s = "ab"`
- `t = "cc"`

`s → t` mapping:
a → c
b → c

This looks valid in one direction, but it breaks the rule:
two different characters map to the same character.

So we must also check:
- `t → s`

---

### How `map_check` Works
For each position `i`:
- If character from `txt1` is **not yet mapped**:
    → create mapping to corresponding character in `txt2`
- If it **is already mapped**:
    → ensure it maps to the **same character as before**
    → otherwise return False

If the loop finishes → mapping is consistent.

---

### Execution Flow
1. Check mapping from `s → t`
2. Check mapping from `t → s`
3. Only if **both pass**, the strings are isomorphic

---

### Why This Works
- Ensures **consistency** (same char always maps the same way)
- Ensures **uniqueness** (no two chars map to one char)
- Covers all tricky cases cleanly

---

### Complexity
- Time: O(n)  
- Space: O(n) for the two maps
'''

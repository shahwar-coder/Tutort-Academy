'''
2085. Count Common Words With One Occurrence
https://leetcode.com/problems/count-common-words-with-one-occurrence/description/
'''

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        frequency1 = {}
        frequency2 = {}
        count=0

        for word in words1:
            frequency1[word] = frequency1.get(word, 0) + 1

        for word in words2:
            frequency2[word] = frequency2.get(word, 0) + 1

        for word in frequency1.keys():
            if frequency1.get(word, 0) == 1 and frequency2.get(word, 0) == 1:
                count+=1



'''
# Improved, Easy-to-Understand Key Points for
# “Count Common Words With One Occurrence”

- Goal:
    Count how many words appear:
        • exactly once in words1 AND
        • exactly once in words2.

- Build two frequency maps:
      frequency1[word] = how many times word appears in words1
      frequency2[word] = how many times word appears in words2

- Why use frequency1.get(word, 0)?
    - If the word does NOT exist in the dictionary,
      .get() safely returns 0 instead of causing a KeyError.
    - This makes checks like (frequency2.get(word, 0) == 1)
      safe and clean without needing "if word in dictionary".
    - It simplifies code and avoids bugs.

- After building both maps:
    Loop through each unique word in words1:
        - If frequency1[word] == 1 AND frequency2.get(word, 0) == 1:
              → this word appears once in both lists
              → increase the result count

- Why loop through frequency1.keys() instead of words2?
    - Because a valid word MUST appear in words1 exactly once.
    - No need to check words that don't appear in words1 at all.

- This method avoids:
    - Nested loops
    - Repeated scanning of lists
    - Extra sets or sorting

- Time Complexity:
      O(n + m)  
      (Single pass to count, single pass to compare)
- Space Complexity:
      O(n + m)  
      (Two frequency maps)

- Tools used:
    - Hashmaps (dicts) → fast O(1) frequency lookup
    - .get(key, default) → safe access for missing words

'''

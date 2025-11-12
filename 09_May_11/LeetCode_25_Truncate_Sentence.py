'''
1816. Truncate Sentence
https://leetcode.com/problems/truncate-sentence/description/
'''

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sentences=(s.strip()).split(" ")
        return " ".join(sentences[:k])

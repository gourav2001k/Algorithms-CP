# https://leetcode.com/problems/find-words-containing-character/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)
        out = []
        for i in range(n):
            if x in words[i]:
                out.append(i)
        return out

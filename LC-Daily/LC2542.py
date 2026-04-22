# https://leetcode.com/problems/words-within-two-edits-of-dictionary/description/

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        out = []
        for word in queries:
            for option in dictionary:
                if self.check(word, option):
                    out.append(word)
                    break
        return out

    def check(self, a, b):
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                c += 1
            if c > 2:
                break
        return c <= 2

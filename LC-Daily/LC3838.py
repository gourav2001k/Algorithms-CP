# https://leetcode.com/problems/weighted-word-mapping/description

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out = []
        for word in words:
            s = 0
            for c in word:
                s += weights[ord(c)-97]
            out.append(chr(122-(s % 26)))
        return "".join(out)

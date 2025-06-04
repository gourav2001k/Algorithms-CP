# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description/

class Solution:
    def answerString(self, word: str, f: int) -> str:
        if f == 1:
            return word
        n = len(word)
        maxL = 1+n-f
        out = ''
        for i in range(n):
            x = ''
            for j in range(i, min(n, i+maxL)):
                x += word[j]
                if x > out:
                    out = x
                elif x < out[:len(x)]:
                    break
        return out

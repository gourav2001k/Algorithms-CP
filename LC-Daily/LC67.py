# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        out, c = '', 0
        i, j = n-1, m-1
        while i >= 0 and j >= 0:
            t = int(a[i])+int(b[j])+c
            out += str(t % 2)
            c = t//2
            i -= 1
            j -= 1

        while i >= 0:
            t = int(a[i])+c
            out += str(t % 2)
            c = t//2
            i -= 1

        while j >= 0:
            t = int(b[j])+c
            out += str(t % 2)
            c = t//2
            j -= 1

        if c:
            out += str(c)

        return out[::-1]

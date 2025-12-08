# https://leetcode.com/problems/count-square-sum-triples/description/

class Solution:
    def countTriples(self, n: int) -> int:
        out = 0
        for i in range(1, n):
            for j in range(i+1, n):
                c = i**2+j**2
                croot = c**0.5
                if croot > n:
                    continue
                if int(croot)**2 != c:
                    continue
                out += 1
        return out << 1

# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n, m = len(bank), len(bank[0])
        prev, out = 0, 0
        for i in range(n):
            c = 0
            for j in range(m):
                if bank[i][j] == '1':
                    c += 1
                    out += prev
            if c:
                prev = c
        return out

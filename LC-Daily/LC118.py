# https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        prev = [1]
        out = [prev]
        for i in range(1, n):
            cur = [1]
            for j in range(1, len(prev)):
                cur.append(prev[j]+prev[j-1])
            cur.append(1)
            out.append(cur)
            prev = cur
        return out

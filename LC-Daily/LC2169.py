# https://leetcode.com/problems/count-operations-to-obtain-zero/description/

class Solution:
    def countOperations(self, n1: int, n2: int) -> int:
        c = 0
        while n1 and n2:
            if n1 < n2:
                n1, n2 = n2, n1
            c += n1//n2
            n1 -= (n1//n2)*n2
        return c

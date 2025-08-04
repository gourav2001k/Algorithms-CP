# https://leetcode.com/problems/fruit-into-baskets/description/

class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        n = len(arr)
        a, b = -1, -1
        i1, i2 = 0, 0
        out, prev = 0, 0
        for i in range(n):
            if arr[i] == a or a == -1:
                a = arr[i]
                i1 = i
            elif arr[i] == b or b == -1:
                b = arr[i]
                i2 = i
            elif i1 < i2:
                a = arr[i]
                prev = i1+1
                i1 = i
            else:
                b = arr[i]
                prev = i2+1
                i2 = i
            out = max(out, i+1-prev)
        return out

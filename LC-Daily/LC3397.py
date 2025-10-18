# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

class Solution:
    def maxDistinctElements(self, arr: List[int], k: int) -> int:
        n = len(arr)
        intervals = []
        for x in arr:
            intervals.append([x-k, x+k, 1])

        intervals.sort()
        out = []
        for a, b, c in intervals:
            if out and a <= out[-1][1]:
                x, y, z = out[-1]
                if a-x > z:
                    x += 1
                y = max(y, b)
                z = min(z+1, y-x+1)
                out[-1] = [x, y, z]
            else:
                out.append([a, b, c])

        res = 0
        for a, b, c in out:
            res += min(c, b-a+1)
        return res

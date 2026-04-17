# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description/

class Solution:
    def minMirrorPairDistance(self, arr: List[int]) -> int:
        n = len(arr)

        out = n
        loc = dict()
        def rev(x): return int(str(x)[::-1])
        for x in range(n):
            if arr[x] in loc:
                out = min(out, x-loc[arr[x]])
            loc[rev(arr[x])] = x

        return out if out != n else -1

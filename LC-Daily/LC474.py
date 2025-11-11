# https://leetcode.com/problems/ones-and-zeroes/description/

class Solution:
    def findMaxForm(self, strs: List[str], n: int, m: int) -> int:
        arr = []
        l = len(strs)
        for s in strs:
            z = s.count('0')
            o = len(s)-z
            arr.append((z, o))

        @lru_cache(None)
        def solve(i, x, y):
            if i == l:
                return 0
            out = solve(i+1, x, y)
            if arr[i][0] <= x and arr[i][1] <= y:
                out = max(out, solve(i+1, x-arr[i][0], y-arr[i][1])+1)
            return out

        return solve(0, n, m)

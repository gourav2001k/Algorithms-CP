# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/

class Solution:
    def maximumJumps(self, arr: List[int], t: int) -> int:
        n = len(arr)
        MN = -10**18
        out = [MN for i in range(n)]
        out[0] = 0
        for i in range(n):
            if out[i] == MN:
                continue
            for j in range(i+1, n):
                if abs(arr[j]-arr[i]) <= t:
                    out[j] = max(out[j], out[i]+1)
        if out[n-1] == MN:
            return -1
        return out[n-1]

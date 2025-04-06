# https://leetcode.com/problems/largest-divisible-subset/description/

class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr.sort()
        dp = [1 for i in range(n)]
        prevs = [i for i in range(n)]
        for i in range(n):
            for j in range(i):
                if not arr[i] % arr[j]:
                    if dp[j]+1 > dp[i]:
                        prevs[i] = j
                        dp[i] = dp[j]+1

        idx = dp.index(max(dp))
        out = []
        while prevs[idx] != idx:
            out.append(arr[idx])
            idx = prevs[idx]
        out.append(arr[idx])
        return out

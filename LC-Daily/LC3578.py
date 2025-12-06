# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

class Solution:
    def countPartitions(self, arr: List[int], k: int) -> int:
        n = len(arr)
        mod = 10**9+7
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        prev, presum = 0, dp[0]
        minQ, maxQ = deque(), deque()
        for i in range(n):
            while minQ and minQ[-1][0] >= arr[i]:
                minQ.pop()
            while maxQ and maxQ[-1][0] <= arr[i]:
                maxQ.pop()
            minQ.append((arr[i], i))
            maxQ.append((arr[i], i))
            while maxQ[0][0]-minQ[0][0] > k:
                x = min(maxQ[0][1], minQ[0][1])
                if maxQ[0][1] < minQ[0][1]:
                    maxQ.popleft()
                else:
                    minQ.popleft()
                while prev <= x:
                    presum -= dp[prev]
                    presum %= mod
                    prev += 1
            dp[i+1] += presum
            dp[i+1] %= mod
            presum += dp[i+1]
            presum %= mod
        return dp[n]

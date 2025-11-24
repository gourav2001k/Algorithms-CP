# https://leetcode.com/problems/greatest-sum-divisible-by-three/description/?

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        if not s % 3:
            return s
        h1, h2 = [], []
        for x in nums:
            if x % 3 == 1:
                if len(h1) > 1:
                    if x < h1[-1]:
                        h1.pop()
                    else:
                        continue
                heappush(h1, x)
            elif x % 3 == 2:
                if len(h2) > 1:
                    if x < h2[-1]:
                        h2.pop()
                    else:
                        continue
                heappush(h2, x)
        if s % 3 == 2:
            h1, h2 = h2, h1
        x = 10**6
        if h1:
            x = min(x, h1[0])
        if len(h2) > 1:
            x = min(x, heappop(h2)+heappop(h2))
        return s-x

# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        l, r = 0, n-1
        for i in range(n):
            if colors[i] ^ colors[n-1]:
                l = i
                break
        for i in range(n-1, -1, -1):
            if colors[0] ^ colors[i]:
                r = i
                break

        return max(r, n-1-l)

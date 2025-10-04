# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        out = 0  # potential minimum answer
        # starting with the widest container
        while i < j:
            out = max(out, min(height[i], height[j])*(j-i))
            # since, width is reduced we are increasing the height
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return out

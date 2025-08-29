# https://leetcode.com/problems/alice-and-bob-playing-flower-game/description/

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # odd first * even second + even first * odd second
        return ((n+1) >> 1)*(m >> 1)+(n >> 1)*((m+1) >> 1)

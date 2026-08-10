# https://leetcode.com/problems/stone-game-iv/

class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        x = 1
        out = False
        if not n:
            return out
        while x**2 <= n:
            if not self.winnerSquareGame(n-x**2):
                out = True
                break
            x += 1
        return out

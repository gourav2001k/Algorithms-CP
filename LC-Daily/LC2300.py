# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        potions.sort()
        out = []
        for i in range(n):
            x = success/spells[i]
            out.append(m-bisect_left(potions, x))
        return out

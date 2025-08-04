# https://leetcode.com/problems/fruits-into-baskets-ii/description

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        taken = [0 for i in range(n)]
        out = 0
        for f in fruits:
            done = False
            for i in range(n):
                if taken[i]:
                    continue
                if baskets[i] < f:
                    continue
                taken[i] = 1
                done = True
                break
            if not done:
                out += 1
        return out

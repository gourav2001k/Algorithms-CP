# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        out = -10**9
        for i in range(k):
            t = 0
            for j in range(i, n, k):
                if t < 0:
                    t = 0
                t += energy[j]
            out = max(out, t)
        return out

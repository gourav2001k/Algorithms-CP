# https://leetcode.com/problems/reordered-power-of-2/description/

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        for i in range(32):
            if Counter(str(2**i)) == Counter(str(N)):
                return True
        return False

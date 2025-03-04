# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for mask in range(1 << 15):
            t = 0
            for i in range(15):
                if (1 << i) & mask:
                    t += 3**i
            if t == n:
                return True
        return False

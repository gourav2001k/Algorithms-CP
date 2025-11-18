# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        end = [0 for i in range(n+1)]
        end[0] = 1
        for i in range(n):
            if not end[i]:
                continue
            if bits[i] == 0:
                end[i+1] = 1
            elif i+1 < n:
                end[i+2] = 1
        return bool(end[n-1])

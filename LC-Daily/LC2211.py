# https://leetcode.com/problems/count-collisions-on-a-road/

class Solution:
    def countCollisions(self, directions: str) -> int:
        out = 0
        prev, right = 0, 0
        for d in directions:
            if d == 'R':
                right += 1
                prev = 0
            elif d == 'S':
                out += right
                right = 0
                prev = 1
            else:
                if right:
                    out += right+1
                    prev = 1
                else:
                    out += prev
                right = 0
        return out

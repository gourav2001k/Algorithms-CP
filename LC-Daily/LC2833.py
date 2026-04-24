# https://leetcode.com/problems/furthest-point-from-origin/description/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n = len(moves)
        l = moves.count('L')
        r = moves.count('R')
        return abs(l-r)+n-(l+r)

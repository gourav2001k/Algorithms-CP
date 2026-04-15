# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/

class Solution:
    def closestTarget(self, words: List[str], target: str, x: int) -> int:
        n = len(words)
        out = n
        for i in range(n):
            if words[i] == target:
                out = min(out, (i-x) % n, (x-i) % n)
        return out if out != n else -1

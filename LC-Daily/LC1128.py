# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = Counter()
        out = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            out += count[(a, b)]
            count[(a, b)] += 1
        return out

# https://leetcode.com/problems/count-number-of-trapezoids-i/description/

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        count = Counter()
        for a, b in points:
            count[b] += 1

        multiSum = 0
        out, mod = 0, 10**9+7
        for x in count:
            count[x] = (count[x]*(count[x]-1)) >> 1
            multiSum += count[x]
            multiSum %= mod

        for x in count:
            out += ((multiSum-count[x]) % mod)*count[x]
            out %= mod
        out *= pow(2, mod-2, mod)  # divide by 2, to avoid double counting
        return out % mod

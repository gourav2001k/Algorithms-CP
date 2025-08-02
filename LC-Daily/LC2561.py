# https://leetcode.com/problems/rearranging-fruits/description/

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = Counter(basket1+basket2)
        for x in count:
            if count[x] & 1:
                return -1

        m = basket1[0]
        c1 = Counter(basket1)
        c2 = Counter(basket2)
        extra1, extra2 = [], []
        for x in count:
            m = min(x, m)
            for _ in range(abs(c1[x]-c2[x]) >> 1):
                if c1[x] > c2[x]:
                    extra1.append(x)
                else:
                    extra2.append(x)

        e = len(extra1)
        extra1.sort()
        extra2.sort()

        out = 0
        for i in range(e):
            out += min(2*m, min(extra1[i], extra2[e-1-i]))
        return out

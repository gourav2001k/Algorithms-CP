# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/description/

class Solution:
    @lru_cache(None)
    def earliestAndLatest(self, n: int, x: int, y: int) -> List[int]:
        if n == 2:
            return [1, 1]
        if x == n+1-y:
            return [1, 1]
        a, b = n, 1
        for mask in range(1 << (n >> 1)):
            seq = []
            for j in range(n >> 1):
                if j+1 == x or j+1 == y:
                    seq.append(j+1)
                elif (1 << j) & mask and n-j != x and n-j != y:
                    seq.append(j+1)
                else:
                    seq.append(n-j)
            if n & 1:
                seq.append((n+1) >> 1)
            seq.sort()
            p1, p2 = self.earliestAndLatest(
                len(seq), seq.index(x)+1, seq.index(y)+1)
            a, b = min(a, p1+1), max(b, p2+1)
        return a, b

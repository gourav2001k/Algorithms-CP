# https://leetcode.com/problems/next-greater-numerically-balanced-number/description/

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        x = len(str(n))
        globalAns = 7777777

        def find(x, mask):
            out = globalAns
            if x < 0:
                return out
            if not x:
                keys = []
                for x in range(7):
                    if (1 << x) & mask:
                        keys += [x+1]*(x+1)
                for perm in permutations(keys):
                    k = int("".join(map(str, perm)))
                    if k <= n:
                        continue
                    out = min(out, k)
                return out
            for i in range(7):
                if mask & (1 << i):
                    continue
                k = find(x-i-1, mask | (1 << i))
                out = min(out, k)
            return out

        out = find(x, 0)
        if out == globalAns:
            out = find(x+1, 0)
        return out

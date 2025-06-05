# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n, N = len(s1), 26
        par = [i for i in range(N)]

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(a, b):
            x, y = find(a), find(b)
            if x == y:
                return
            par[x] = y

        for i in range(n):
            union(ord(s1[i])-97, ord(s2[i])-97)

        groups = defaultdict(list)
        for i in range(N):
            groups[find(i)].append(chr(97+i))

        out = ''
        for i in baseStr:
            out += groups[par[ord(i)-97]][0]
        return out

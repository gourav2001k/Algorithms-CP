# https://leetcode.com/problems/avoid-flood-in-the-city/description/?

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        filled = dict()

        par = [i for i in range(n+1)]

        def findPar(x):
            if x != par[x]:
                par[x] = findPar(par[x])
            return par[x]

        def union(x):
            par[x] = findPar(x+1)

        out = [1 for i in range(n)]
        for i in range(n):
            if not rains[i]:
                continue
            out[i] = -1
            union(i)
            if rains[i] not in filled:
                filled[rains[i]] = i
                continue
            dry = findPar(filled[rains[i]]+1)
            if dry >= i:
                return []
            union(dry)
            out[dry] = rains[i]
            filled[rains[i]] = i

        return out

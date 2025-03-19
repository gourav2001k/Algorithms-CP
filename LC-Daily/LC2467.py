# https://leetcode.com/problems/most-profitable-path-in-a-tree/description/

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        # adjusting to neutralise the bob effect
        def findBob(cur, d=0, par=-1):
            if cur == bob:
                amount[bob] = 0
                return d
            for x in g[cur]:
                if x == par:
                    continue
                k = findBob(x, d+1, cur)
                if k:
                    if d*2 > k:
                        amount[cur] = 0
                    elif d*2 == k:
                        amount[cur] //= 2
                    return k

        findBob(0)

        # now just a greedy approach to find Alice max
        def maxSum(cur=0, par=-1):
            out = -10**9
            for x in g[cur]:
                if x == par:
                    continue
                out = max(out, maxSum(x, cur))
            if len(g[cur]) < 2 and par != -1:
                out = 0
            return out+amount[cur]

        return maxSum()

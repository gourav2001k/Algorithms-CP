# https://leetcode.com/problems/maximum-number-of-k-divisible-components/

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        def solve(root, par=None):
            out, s = 0, values[root]
            for cur in g[root]:
                if cur == par:
                    continue
                a, b = solve(cur, root)
                out += a
                s += b
            if not s % k:
                return out+1, 0
            return out, s

        return solve(0)[0]

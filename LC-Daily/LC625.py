# leetcode.com/problems/lexicographically-smallest-string-after-applying-operations

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add(s, a):
            x = ''
            for i in range(len(s)):
                if i & 1:
                    x += str((int(s[i])+a) % 10)
                else:
                    x += s[i]
            return x

        def rotate(s, b):
            return s[-b:]+s[:-b]

        vis = set()

        def dfs(s, a, b):
            if s in vis:
                return
            vis.add(s)
            dfs(add(s, a), a, b)
            dfs(rotate(s, b), a, b)

        dfs(s, a, b)
        return sorted(list(vis))[0]

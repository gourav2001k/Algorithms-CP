# https://leetcode.com/problems/snakes-and-ladders

class Solution:
    def snakesAndLadders(self, mat: List[List[int]]) -> int:
        n = len(mat)
        l = n**2

        def coordinates(x):
            a, b = x//n, x % n
            if a & 1:
                b = n-1-b
            a = n-1-a
            return a, b

        dp = [l for i in range(l)]
        dp[0] = 0
        q = deque([0])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == l-1:
                    return dp[cur]
                for x in range(cur+1, min(cur+7, l)):
                    y = x
                    a, b = coordinates(x)
                    if mat[a][b] != -1:
                        y = mat[a][b]-1
                    if dp[y] > dp[cur]+1:
                        dp[y] = dp[cur]+1
                        q.append(y)
        return -1

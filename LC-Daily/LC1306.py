# https://leetcode.com/problems/jump-game-iii/description/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [0 for i in range(n)]
        vis[start] = 1
        q = deque([start])
        while q:
            x = q.popleft()
            if not arr[x]:
                return True
            a, b = x-arr[x], x+arr[x]
            if 0 <= a < n and not vis[a]:
                vis[a] = 1
                q.append(a)
            if 0 <= b < n and not vis[b]:
                vis[b] = 1
                q.append(b)
        return False

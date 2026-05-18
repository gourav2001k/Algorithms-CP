# https://leetcode.com/problems/jump-game-iv/description/

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        vis = [0 for i in range(n)]
        groups = defaultdict(list)
        for i in range(n):
            groups[arr[i]].append(i)

        vis[0] = 1
        q = deque([(0, 0)])
        while q:
            x, d = q.popleft()
            if x == n-1:
                return d
            ops = [x-1, x+1]+groups[arr[x]]
            for k in ops:
                if groups[arr[x]]:
                    groups[arr[x]].pop()
                if not 0 <= k < n:
                    continue
                if vis[k]:
                    continue
                vis[k] = 1
                q.append((k, d+1))
        return -1

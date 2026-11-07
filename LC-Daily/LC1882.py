# https://leetcode.com/problems/process-tasks-using-servers/description/

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free, occupied = [], []
        for i, w in enumerate(servers):
            heappush(free, (w, i))

        t = 0
        out = []
        for i, ts in enumerate(tasks):
            if not free:
                t = occupied[0][0]
            while occupied and t >= occupied[0][0]:
                heappush(free, (occupied[0][1], occupied[0][2]))
                heappop(occupied)
            out.append(free[0][1])
            heappush(occupied, (t+ts, free[0][0], free[0][1]))
            heappop(free)
            if i == t:
                t += 1
        return out

# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/description/

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)
        tasks.sort()
        workers.sort(reverse=True)

        def check(x):
            chance = pills
            sortedSet = SortedList(workers[:x])
            for i in range(x-1, -1, -1):
                if sortedSet[i] >= tasks[i]:
                    sortedSet.pop()
                elif chance:
                    idx = sortedSet.bisect_left(tasks[i]-strength)
                    if idx > i:
                        return False
                    chance -= 1
                    sortedSet.pop(idx)
                else:
                    return False
            return True

        l, r = 0, min(n, m)+1
        while l+1 < r:
            m = (l+r) >> 1
            if check(m):
                l = m
            else:
                r = m
        return l

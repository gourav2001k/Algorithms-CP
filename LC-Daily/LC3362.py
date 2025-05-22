# https://leetcode.com/problems/zero-array-transformation-iii/description/

class Solution:
    def maxRemoval(self, arr: List[int], queries: List[List[int]]) -> int:
        n = len(arr)
        queries.sort(reverse=True)
        takenEndTimes = []
        availableEndTimes = []
        for time in range(n):
            while queries and queries[-1][0] <= time:
                heappush(availableEndTimes, -queries.pop()[1])
            while takenEndTimes and takenEndTimes[0] < time:
                heappop(takenEndTimes)

            while arr[time] > len(takenEndTimes):
                if not availableEndTimes or -availableEndTimes[0] < time:
                    return -1
                heappush(takenEndTimes, -heappop(availableEndTimes))

        return len(availableEndTimes)

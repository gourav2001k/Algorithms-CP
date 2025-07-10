# https://leetcode.com/problems/meeting-rooms-iii/description/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        roomHeap = [i for i in range(n)]
        meetEnds = []
        heapify(roomHeap)
        count = [0 for i in range(n)]
        curTime = 0
        for a, b in meetings:
            curTime = max(a, curTime)
            if not roomHeap:
                curTime = max(curTime, meetEnds[0][0])
            while meetEnds and meetEnds[0][0] <= curTime:
                x, y = heappop(meetEnds)
                heappush(roomHeap, y)

            r = heappop(roomHeap)
            count[r] += 1
            heappush(meetEnds, (curTime+b-a, r))

        return count.index(max(count))

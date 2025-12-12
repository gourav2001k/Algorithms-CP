# https://leetcode.com/problems/count-mentions-per-user/description/

class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        l = len(events)

        def mapper(x): return (int(x[1]), 0 if x[0]
                               == "OFFLINE" else 1, x[2].split())
        events = list(map(mapper, events))
        events.sort()
        out = [0 for i in range(n)]
        extra = 0

        offline = []  # minHeap
        online = set([i for i in range(n)])
        for i in range(l):
            t, typ, idx = events[i]
            while offline and offline[0][0] <= t:
                tt, xx = heappop(offline)
                online.add(xx)
            if not typ:
                online.remove(int(idx[0]))
                heappush(offline, (t+60, int(idx[0])))
            else:
                for x in idx:
                    if x == 'ALL':
                        extra += 1
                    elif x == 'HERE':
                        for j in online:
                            out[j] += 1
                    else:
                        out[int(x[2:])] += 1

        for i in range(n):
            out[i] += extra
        return out

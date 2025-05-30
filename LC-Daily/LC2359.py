# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        d1 = [n+1 for i in range(n)]
        d, cur = 0, node1
        d1[cur] = d
        while edges[cur] != -1:
            cur = edges[cur]
            d += 1
            if d1[cur] <= d:
                break
            d1[cur] = d

        d2 = [n+1 for i in range(n)]
        d, cur = 0, node2
        d2[cur] = d
        while edges[cur] != -1:
            cur = edges[cur]
            d += 1
            if d2[cur] <= d:
                break
            d2[cur] = d

        out, idx = n+1, -1
        for i in range(n):
            if max(d1[i], d2[i]) < out:
                out = max(d1[i], d2[i])
                idx = i
        return idx

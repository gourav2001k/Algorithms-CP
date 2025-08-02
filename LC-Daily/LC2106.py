# etcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/description/

class Solution:
    def maxTotalFruits(self, arr: List[List[int]], loc: int, k: int) -> int:
        n = len(arr)
        pre = [0 for i in range(n+1)]
        pos = []
        for i in range(n):
            pre[i+1] = pre[i]+arr[i][1]
            pos.append(arr[i][0])

        i, j = bisect_left(pos, loc), bisect_right(pos, loc+k)
        x, y = bisect_right(pos, loc), bisect_left(pos, loc)
        out = pre[j]-pre[i]
        for i in range(n):
            if abs(loc-pos[i]) > k:
                continue
            if loc > pos[i]:
                j = bisect_right(pos, pos[i]+k-(loc-pos[i]))
                out = max(out, pre[max(j, x)]-pre[i])
            else:
                j = bisect_left(pos, pos[i]-(k-(pos[i]-loc)))
                out = max(out, pre[i+1]-pre[min(j, y)])

        return out

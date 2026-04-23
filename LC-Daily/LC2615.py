# https://leetcode.com/problems/sum-of-distances/description/

class Solution:
    def distance(self, arr: List[int]) -> List[int]:
        n = len(arr)

        loc = defaultdict(list)
        pre = defaultdict(list)
        for i in range(n):
            loc[arr[i]].append(i+1)
            if not pre[arr[i]]:
                pre[arr[i]].append(0)
            pre[arr[i]].append(pre[arr[i]][-1]+i+1)

        out = [0 for i in range(n)]

        for i in range(n):
            idxs = loc[arr[i]]
            preSum = pre[arr[i]]
            x = bisect_left(idxs, i+1)
            l = (i+1)*x-preSum[x]
            r = (preSum[-1]-preSum[x])-(len(idxs)-x)*(i+1)
            out[i] = l+r
        return out

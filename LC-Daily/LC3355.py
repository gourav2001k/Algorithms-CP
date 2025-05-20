class Solution:
    def isZeroArray(self, arr: List[int], queries: List[List[int]]) -> bool:
        n = len(arr)
        pre = [0 for i in range(n+1)]
        for l, r in queries:
            pre[l] += 1
            pre[r+1] -= 1

        for i in range(n):
            pre[i+1] += pre[i]
            if pre[i] < arr[i]:
                return False
        return True

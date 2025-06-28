# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution:
    def maxSubsequence(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        for i in range(n):
            if len(heap) < k:
                heappush(heap, (arr[i], i))
            elif heap[0][0] < arr[i]:
                heappushpop(heap, (arr[i], i))

        taken = [0 for i in range(n)]
        while heap:
            x, i = heappop(heap)
            taken[i] = 1
        return [arr[i] for i in range(n) if taken[i]]

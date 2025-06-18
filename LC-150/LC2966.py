# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution:
    def divideArray(self, arr: List[int], k: int) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        out = []
        for i in range(0, n, 3):
            if arr[i+2]-arr[i] > k:
                return []
            out.append((arr[i], arr[i+1], arr[i+2]))
        return out

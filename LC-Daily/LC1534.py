# https://leetcode.com/problems/count-good-triplets/description/

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        out = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if abs(arr[i]-arr[j]) > a:
                        continue
                    if abs(arr[j]-arr[k]) > b:
                        continue
                    if abs(arr[k]-arr[i]) > c:
                        continue
                    out += 1
        return out

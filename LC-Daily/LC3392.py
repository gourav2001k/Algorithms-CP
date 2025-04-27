# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description

class Solution:
    def countSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        out = 0
        for i in range(1, n-1):
            if arr[i] == (arr[i-1]+arr[i+1]) << 1:
                out += 1
        return out

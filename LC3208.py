# https://leetcode.com/problems/alternating-groups-ii
class Solution:
    def numberOfAlternatingGroups(self, arr: List[int], k: int) -> int:
        n = len(arr)
        arr += arr
        out, c = 0, 1
        for i in range(1, 2*n):
            if i-k == n-1:
                return out
            if arr[i] == arr[i-1]:
                c = 1
            else:
                c += 1
                if c > k:
                    c = k
                if c == k:
                    out += 1
        return out

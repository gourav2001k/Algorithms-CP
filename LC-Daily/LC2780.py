# https://leetcode.com/problems/minimum-index-of-a-valid-split/description/

class Solution:
    def minimumIndex(self, arr: List[int]) -> int:
        n = len(arr)
        count = Counter(arr)
        x = -1
        for i in count:
            if count[i] > n >> 1:
                x = i
                break
        if x == -1:
            return x
        xC = 0
        for i in range(n-1):
            if arr[i] == x:
                xC += 1
            if xC > (i+1) >> 1 and count[x]-xC > (n-i-1) >> 1:
                return i
        return -1

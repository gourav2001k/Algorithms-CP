# https://leetcode.com/problems/sum-of-k-mirror-numbers/

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        out = 0
        cur = [0]
        while n:
            cur = self.nxt(cur)
            x = self.arrToInt(cur)
            if self.convK(x, k):
                out += x
                n -= 1
        return out

    def nxt(self, arr):
        n = len(arr)
        idx = n >> 1
        if n & 1:
            if arr[idx] < 9:
                arr[idx] += 1
                return arr
            arr[idx] = 0
        idx -= 1

        while idx >= 0 and arr[idx] == 9:
            arr[idx] = 0
            arr[n-1-idx] = 0
            idx -= 1
        if idx >= 0:
            arr[idx] += 1
            arr[n-1-idx] += 1
            return arr

        arr.append(0)
        arr[0] = 1
        arr[n] = 1
        return arr

    def arrToInt(self, arr):
        out = 0
        for x in arr:
            out *= 10
            out += x
        return out

    def convK(self, x, k):
        arr = []
        while x:
            arr.append(x % k)
            x //= k
        n = len(arr)
        for i in range(n//2):
            if arr[i] != arr[n-1-i]:
                return False
        return True

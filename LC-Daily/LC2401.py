# https://leetcode.com/problems/longest-nice-subarray/description

# Sliding window(fixed size) + Binary search for optimisation
class Solution:
    def longestNiceSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        def check(bitCount):
            for i in bitCount:
                if i > 1:
                    return False
            return True

        def good(k):
            bitCount = [0 for i in range(32)]
            for i in range(k):
                for j in range(32):
                    if (1 << j) & arr[i]:
                        bitCount[j] += 1
            if check(bitCount):
                return True
            for i in range(k, n):
                for j in range(32):
                    if (1 << j) & arr[i]:
                        bitCount[j] += 1
                    if (1 << j) & arr[i-k]:
                        bitCount[j] -= 1
                if check(bitCount):
                    return True
            return False

        l, r = 1, min(n, 32)+1
        while l+1 < r:
            m = (l+r) >> 1
            if good(m):
                l = m
            else:
                r = m
        return l


# Approach 2: Sliding window/Two pointer (dynamic size)

class Solution:
    def longestNiceSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        curBits = [-1 for i in range(32)]
        prev, out = -1, 0
        for i in range(n):
            for j in range(32):
                if (1 << j) & arr[i]:
                    if curBits[j] != -1:
                        prev = max(prev, curBits[j])
                    curBits[j] = i
            out = max(i-prev, out)
        return out

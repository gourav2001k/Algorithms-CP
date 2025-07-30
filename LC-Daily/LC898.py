# https://leetcode.com/problems/bitwise-ors-of-subarrays/description/

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        bits = [n for i in range(32)]

        def generate(bits):
            ans = set()
            lis = sorted(enumerate(bits), key=lambda x: x[1])
            i, x = 0, 0
            while i < 32 and lis[i][1] != n:
                while i+1 < 32 and lis[i][1] == lis[i+1][1]:
                    x |= 1 << lis[i][0]
                    i += 1
                x |= 1 << lis[i][0]
                ans.add(x)
                i += 1
            return ans

        out = set()
        for i in range(n-1, -1, -1):
            if not arr[i]:
                out.add(arr[i])
            for j in range(32):
                if arr[i] & (1 << j):
                    bits[j] = i
            for x in generate(bits):
                out.add(x)
        return len(out)

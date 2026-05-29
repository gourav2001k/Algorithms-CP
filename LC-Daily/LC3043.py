# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pre1 = set()
        for x in arr1:
            while x:
                pre1.add(x)
                x //= 10
        pre2 = set()
        for x in arr2:
            while x:
                pre2.add(x)
                x //= 10

        out = pre1.intersection(pre2)

        ans = 0
        for x in out:
            k = 0
            while x:
                k += 1
                x //= 10
            ans = max(k, ans)
        return ans

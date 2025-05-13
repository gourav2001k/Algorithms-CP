# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9+7
        count = Counter(s)
        arr = [0 for i in range(26)]
        for x in count:
            arr[ord(x)-97] += count[x]

        while t:
            n = [0]+arr
            n[0] = arr[-1]
            n[1] = (n[1]+arr[-1]) % mod
            arr = n[:-1]
            t -= 1

        out = 0
        for x in arr:
            out += x
            out %= mod
        return out

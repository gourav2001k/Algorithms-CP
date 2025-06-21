# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        n = len(word)
        count = Counter(word)
        arr = list(sorted(count.values()))
        l = len(arr)
        out, prev = n, 0
        for i in range(l):
            t = prev
            for j in range(i+1, l):
                if arr[j] > arr[i]+k:
                    t += arr[j]-arr[i]-k
            prev += arr[i]
            out = min(out, t)
        return out

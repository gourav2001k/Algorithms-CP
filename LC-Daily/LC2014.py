# https://leetcode.com/problems/longest-subsequence-repeated-k-times/description/

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        candidates = [c for c, w in Counter(s).items() if w >= k]
        candidates.sort(reverse=True)
        out = ''
        q = deque(candidates)
        while q:
            nxt = q.popleft()
            if len(nxt) > len(out):
                out = nxt
            for x in candidates:
                potential = nxt+x
                if self.check(s, potential, k):
                    q.append(potential)
        return out

    def check(self, s, p, k):
        n, m = len(s), len(p)
        x, j = 0, 0
        for i in range(n):
            if s[i] != p[j]:
                continue
            j += 1
            if j == m:
                j = 0
                x += 1
        return x >= k

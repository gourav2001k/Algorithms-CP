class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        # keeping a mask of 26 length to represent characters till that point
        l, r = [0 for i in range(n+1)], [0 for i in range(n+1)]
        for i in range(n):
            l[i+1] = l[i] | (1 << (ord(s[i])-97))
            r[n-1-i] = r[n-i] | (1 << (ord(s[n-1-i])-97))

        out = set()
        for i in range(1, n-1):
            for j in range(26):
                if l[i] & (1 << j) and r[i+1] & (1 << j):
                    out.add(chr(97+j)+s[i]+chr(97+j))

        return len(out)

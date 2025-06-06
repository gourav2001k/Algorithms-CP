# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description/

class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        out, t = [], []
        c = Counter(s)

        def check(x):
            for i in c:
                if c[i] and i < x:
                    return False
            return True

        for i in range(n):
            while t and check(t[-1]):
                out.append(t.pop())
            t.append(s[i])
            c[s[i]] -= 1
        out += t[::-1]
        return "".join(out)

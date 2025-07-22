# https://leetcode.com/problems/maximum-score-from-removing-substrings/description/

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s[::-1]
            x, y = y, x
        out1, s = self.helper(s, x)
        out2, s = self.helper(s[::-1], y)
        return out1+out2

    def helper(self, s, c):
        out, n = 0, len(s)
        stack = []
        for i in range(n):
            if s[i] == 'b' and stack and stack[-1] == 'a':
                out += c
                stack.pop()
            else:
                stack.append(s[i])
        return out, ''.join(stack)

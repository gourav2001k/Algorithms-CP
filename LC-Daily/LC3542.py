# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/description/

class Solution:
    def minOperations(self, arr: List[int]) -> int:
        out = 0
        stack = []
        for x in arr:
            while stack and stack[-1] > x:
                stack.pop()
            if not x:
                continue
            if not stack or stack[-1] < x:
                out += 1
            stack.append(x)
        return out

# https://leetcode.com/problems/maximal-rectangle/description/

class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        n = len(mat)
        if n == 0:
            return 0
        if len(mat[0]) == 0:
            return 0
        m = len(mat[0])
        for i in range(n):
            mat[i] = list(map(int, mat[i]))
        # For 1D Histogram

        def helper(arr):
            n = len(arr)
            left, right = [-1], [n]
            stack = [0]
            for i in range(1, n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if stack:
                    left.append(stack[-1])
                else:
                    left.append(-1)
                stack.append(i)
            stack = [n-1]
            for i in range(n-2, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if stack:
                    right.append(stack[-1])
                else:
                    right.append(n)
                stack.append(i)
            right.reverse()
            out = 0
            for i in range(n):
                out = max(arr[i]*(right[i]-left[i]-1), out)
            return out
        prev = mat[0]
        out = helper(prev)
        for i in range(1, n):
            for j in range(m):
                if mat[i][j]:
                    prev[j] += 1
                else:
                    prev[j] = 0
            out = max(out, helper(prev))
        return out

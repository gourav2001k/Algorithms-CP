# https://leetcode.com/problems/push-dominoes/description

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        arr = list(dominoes)
        n = len(arr)

        def change(x, y):
            while x < y:
                arr[x] = 'R'
                arr[y] = 'L'
                x += 1
                y -= 1

        def left(j):
            while j >= 0 and arr[j] == ".":
                arr[j] = 'L'
                j -= 1

        def right(r, i):
            while r < i:
                arr[r] = "R"
                r += 1
        r = -1
        for i in range(n):
            if arr[i] == ".":
                continue
            if arr[i] == 'L':
                if r >= 0:
                    change(r, i)
                else:
                    left(i-1)
                r = -1
            else:
                if r >= 0:
                    right(r, i)
                r = i
        if r >= 0:
            right(r, n)
        return "".join(arr)

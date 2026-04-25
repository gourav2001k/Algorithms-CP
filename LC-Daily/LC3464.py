# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/description/

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        n = len(points)

        def transform(x, y):
            if y == 0:
                return x
            if x == side:
                return side+y
            if y == side:
                return 3*side-x
            return 4*side-y

        arr = []
        for x, y in points:
            arr.append(transform(x, y))
        arr.sort()

        def check(x):
            p = side*4
            for i in range(n):
                c = 1
                st, end = arr[i], p+arr[i]-x
                cur = arr[i]
                while c < k:
                    idx = bisect_left(arr, cur+x)
                    if idx == n:
                        break
                    if arr[idx] > end:
                        break
                    c += 1
                    cur = arr[idx]
                if c >= k:
                    return True
            return False

        l, r = 0, side+1
        while l+1 < r:
            m = (l+r) >> 1
            if check(m):
                l = m
            else:
                r = m
        return l

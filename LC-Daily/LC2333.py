# https://leetcode.com/problems/minimum-sum-of-squared-difference


class Solution:
    def minSumSquareDiff(self, arr1: list[int], arr2: list[int], k1: int, k2: int) -> int:
        n = len(arr1)
        arr = []
        t = k1+k2
        for i in range(n):
            arr.append(abs(arr1[i]-arr2[i]))
        arr.sort(reverse=True)
        arr.append(0)

        process = False
        for i in range(1, n+1):
            d = arr[i-1]-arr[i]
            x = i*d
            if x <= t:
                t -= x
                arr[i-1] = arr[i]
                continue
            q, r = t//i, t % i
            for j in range(i):
                arr[j] = arr[i-1]-q
                if j < r:
                    arr[j] -= 1
            process, t = True, 0
            break

        if t or not process:
            return 0
        return sum(x**2 for x in arr)

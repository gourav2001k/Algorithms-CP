# https://leetcode.com/problems/set-intersection-size-at-least-two/description/?

class Solution:
    def intersectionSizeTwo(self, arr: List[List[int]]) -> int:
        n = len(arr)
        arr.sort()
        heap, out = [], set()
        done = [0 for i in range(n)]
        for i in range(n):
            a, b = arr[i]
            while heap and heap[0][0] < a:
                x, idx = heappop(heap)
                if done[idx] >= 2:
                    continue
                if x in out:
                    x -= 1
                out.add(x)
                for j in range(n):
                    if arr[j][0] <= x <= arr[j][1]:
                        done[j] += 1
                if done[idx] == 1:
                    x -= 1
                    out.add(x)
                    for j in range(n):
                        if arr[j][0] <= x <= arr[j][1]:
                            done[j] += 1
            heappush(heap, (b, i))

        while heap:
            x, idx = heappop(heap)
            if done[idx] >= 2:
                continue
            if x in out:
                x -= 1
            out.add(x)
            for j in range(n):
                if arr[j][0] <= x <= arr[j][1]:
                    done[j] += 1
            if done[idx] == 1:
                x -= 1
                out.add(x)
                for j in range(n):
                    if arr[j][0] <= x <= arr[j][1]:
                        done[j] += 1
        return len(out)


# Cleaner
class Solution:
    def intersectionSizeTwo(self, arr: List[List[int]]) -> int:
        n = len(arr)
        arr.sort(key=lambda x: (x[0], -x[1]))
        remaining = [2 for i in range(n)]
        out = 0
        for i in range(n-1, -1, -1):
            x, y = arr[i]
            r = remaining[i]
            for k in range(x, x+r):
                remaining[i] -= 1
                out += 1
                for j in range(i):
                    if arr[j][1] >= k:
                        remaining[j] -= 1
        return out

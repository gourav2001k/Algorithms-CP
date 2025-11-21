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

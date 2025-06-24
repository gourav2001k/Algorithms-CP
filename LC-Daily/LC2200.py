class Solution:
    def findKDistantIndices(self, arr: List[int], key: int, k: int) -> List[int]:
        n = len(arr)
        intervals = []
        for i in range(n):
            if arr[i] != key:
                continue
            intervals.append([max(i-k, 0), min(i+k, n-1)])

        merged = self.merge(intervals)
        out = []
        for a, b in merged:
            while a <= b:
                out.append(a)
                a += 1
        return out

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        a, b = intervals[0]
        out = [[a, b]]
        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if out[-1][1] >= a:
                out[-1][1] = max(out[-1][1], b)
            else:
                out.append([a, b])
        return out

class Solution:
    def maximumLength(self, arr: List[int]) -> int:
        n = len(arr)
        o, e = 0, 0
        prev, x = 0, 1
        if arr[0] & 1:
            o += 1
            prev = 1
        else:
            e += 1

        for i in range(1, n):
            if arr[i] & 1:
                o += 1
            else:
                e += 1
            if (arr[i] & 1) ^ prev:
                x += 1
                prev ^= 1

        return max(o, e, x)

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            if arr and arr[-1] == i:
                continue
            arr.append(i)

        n = len(arr)
        out = 0
        for i in range(1, n-1):
            if arr[i] > max(arr[i-1], arr[i+1]):
                out += 1
            if arr[i] < min(arr[i-1], arr[i+1]):
                out += 1
        return out

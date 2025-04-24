# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description

class Solution:
    def countCompleteSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        distinct = len(set(arr))
        prev, out = -1, 0
        count = Counter()
        for i in range(n):
            count[arr[i]] += 1
            while len(count) == distinct:
                out += n-i
                prev += 1
                count[arr[prev]] -= 1
                if not count[arr[prev]]:
                    del count[arr[prev]]
        return out

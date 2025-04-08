# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/

class Solution:
    def minimumOperations(self, arr: List[int]) -> int:
        n = len(arr)
        count = Counter(arr)
        for i in range(0, n-2, 3):
            if len(count) == n-i:
                return i//3
            count[arr[i]] -= 1
            count[arr[i+1]] -= 1
            count[arr[i+2]] -= 1
            if not count[arr[i]]:
                del count[arr[i]]
            if not count[arr[i+1]]:
                del count[arr[i+1]]
            if not count[arr[i+2]]:
                del count[arr[i+2]]
        if len(count) == n % 3:
            return n//3
        return (n//3)+1

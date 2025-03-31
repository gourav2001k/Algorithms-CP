# https://leetcode.com/problems/put-marbles-in-bags/description

class Solution:
    def putMarbles(self, arr: List[int], k: int) -> int:
        if k == 1:
            return 0
        n = len(arr)
        newArr = []
        for i in range(1, n):
            newArr.append(arr[i]+arr[i-1])
        newArr.sort()
        return sum(newArr[-k+1:])-sum(newArr[:k-1])

# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        out = -1
        for x in count:
            if count[x] == x and x > out:
                out = x
        return out
